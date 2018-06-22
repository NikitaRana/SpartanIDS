import hashlib
import pickle
import subprocess
import os
import re
import rsa
import conf

def search_files(motif, root_path):
    # search the files
    result = []
    w = os.walk(root_path)
    for (path, dirs, files) in w:
        for f in files:
            if re.compile(motif).search(f):
                # if not a symbolic link
                if not os.path.islink(os.path.join(path, f)):
                    result.append(os.path.join(path, f))
    return result

def hash_file(target_file):
    #hashing
    sha256_hash = hashlib.sha256()
    opened_file = None
    hashed_data = None
    data = None

    try:
        opened_file = open(target_file, "rb")
        data = opened_file.read()
    except Exception as e:
        # The specified file does not exist,
        # remove from the list.
        print(target_file, ":", e)
        globals()['number_of_files_to_scan'] = \
            globals()['number_of_files_to_scan'] - 1
        del list_of_files[list_of_files.index(target_file)]
    finally:
        if data is not None:
            opened_file.close()

    if data is not None:
        sha256_hash.update(data)
        hashed_data = sha256_hash.hexdigest()

    return hashed_data



if __name__ == '__main__':
    # Point of entry in execution mode.
    database = {}
    database["files"] = {}
    database["commands"] = {}

    # load the specific files to scan
    list_of_files = conf.SPECIFIC_FILES_TO_SCAN

    # adding the folders with rules to scan :
    for rules in conf.FOLDER_RULES:
        list_of_files.extend(search_files(rules[0], rules[1]))
    number_of_files_to_scan = len(list_of_files)


    print("Generating database...")

    for a_file in list_of_files:
        hash_value = hash_file(a_file)
        if hash_value is not None:
            line = a_file + ":" + hash_value + ":"
            database["files"][a_file] = hash_value


    for command in conf.COMMANDS:
        proc =  subprocess.Popen((command), stderr=subprocess.STDOUT, stdout=subprocess.PIPE)
        command_output = proc.stdout.read()
        sha256_hash = hashlib.sha256()
        sha256_hash.update(command_output)
        hashed_data = sha256_hash.hexdigest()
        database["commands"][command] = hashed_data

    serialized_database = open(conf.DATABASE, "wb")
    pickle.dump(database, serialized_database)
    serialized_database.close()

    print(number_of_files_to_scan, "files in the database.")

    with open(conf.PRIVATE_KEY, "rb") as private_key_dump:
        private_key = pickle.load(private_key_dump)

    with open(conf.DATABASE, 'rb') as msgfile:
        signature = rsa.sign(msgfile, private_key, 'SHA-256')

    with open(conf.DATABASE_SIG, "wb") as signature_file:
        signature_file.write(signature)
