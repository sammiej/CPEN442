import hashlib
import time
import random
import string

start_time = time.time()
pw_options = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890!@#$%^&*()_+-="
pw_hash = "DI880764E28FA39D0324DE7CBFC2442C6919BC0268"
salt = pw_hash[:2]
N = 6
counter = 0

while True:
    pw = ''.join(random.choice(pw_options) for _ in range(N))
    pw = salt + pw
    hash = hashlib.sha1(pw).hexdigest().upper()

    if counter % 10000 == 1:
        print(pw + " " + hash)

    if salt + hash == pw_hash:
        print("Password cracked: " + pw)
        print("Hash: " + hash)
        print("--- %s seconds ---" % (time.time() - start_time))
        break

    counter += 1
