import hashlib

def count(md5_hash):
    for i in range(0,9999999):
        new_value = md5_hash + str(i)
        hashing = hashlib.md5(new_value.encode())
        new_hash = hashing.hexdigest()
        if new_hash[:6] == "000000":
            print(i)
            exit()

if __name__=="__main__":
    md5_hash = "bgvyzdsv"
    count(md5_hash)