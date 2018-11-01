import hashlib
import time
import random
import string

start_time = time.time()
pw_hash = "du6447D55EFA5B134B577F196A20ED2E89CE59C7B6"
salt = pw_hash[:2]
N = 4
counter = 0

while True:
    pw = ''.join(random.choice(string.digits) for _ in range(N))
    pw = salt + pw
    hash = hashlib.sha1(pw).hexdigest().upper()

    # Debug
    if counter % 10000 == 1:
        print(pw + " " + hash)

    # Found
    if salt + hash == pw_hash:
        print("Password cracked: " + pw)
        print("Hash: " + hash)
        print("--- %s seconds ---" % (time.time() - start_time))
        break

    counter += 1
