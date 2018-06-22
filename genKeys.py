#! /usr/bin/env python
#-*- coding: utf-8 -*-


import pickle
import rsa

import conf
def main():
    print("Generating", conf.NB_BITS, "bits RSA keys ...")
    pub, priv = rsa.newkeys(conf.NB_BITS)

    public_key = open(conf.PUBLIC_KEY, "wb")
    private_key = open(conf.PRIVATE_KEY, "wb")

    print("Dumping Keys")
    pickle.dump(pub, public_key)
    pickle.dump(priv, private_key)

    public_key.close()
    public_key.close()

    print("Done.")
