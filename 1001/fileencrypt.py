from cryptography.fernet import Fernet
def encrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it encrypts the file and write it
    """
    f = Fernet(key)

    with open(filename, "rb") as file:
        # read all file data
        file_data = file.read()
    
     # encrypt data
    encrypted_data = f.encrypt(file_data)
        # write the encrypted file
    with open(filename+"_encrypted", "wb") as file:
        file.write(encrypted_data)
    

def decrypt(filename, key):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    f = Fernet(key)
    with open(filename, "rb") as file:
        # read the encrypted data
        encrypted_data = file.read()
    # decrypt data
    decrypted_data = f.decrypt(encrypted_data)
    # write the original file
    with open(filename+'_decrypted', "wb") as file:
        file.write(decrypted_data)
    
def write_key():
    """
    Generates a key and save it into a file
    """
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    
    
    
def load_key():
    """
    Loads the key from the current directory named `key.key`
    """
    return open("key.key", "rb").read()


# generate and write a new key
write_key()

# load the previously generated key
key = load_key()

encrypt('Assignment 1-android dev..PNG', key)
decrypt('Assignment 1-android dev..PNG_encrypted', key)
#https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python