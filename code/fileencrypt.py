from cryptography.fernet import Fernet
import mysql.connector as mysql
from mysqlx import DatabaseError

# def add_to_database(name, key1, password):
#     db = mysql.connect(
#         host="localhost",
#         user="root",
#         password="Bapa@2609",
#         database="fileencryptdecrypt"
#     )
#     cur=db.cursor()
#     query="INSERT INTO auth(files, key1, pass)VALUES(?,?,?);"
#     cur.execute(query,(name,key1,password))
#     result=cur.fetchall()
#     db.commit()
#     db.close()
#     cur.close()
    
database1=[]
def encrypt(filename,password):
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
    global database1
    add_to_database=(filename, key, password)
    database1.append(add_to_database)
    

def decrypt(filename,password):
    """
    Given a filename (str) and key (bytes), it decrypts the file and write it
    """
    fileslice=filename[:-10]
    print(database1)
    stop=1
    
    extension=filename[-14:-10]
    for i in database1:
        print(i)
        print(password)
        print(fileslice)
        print(i[2])
        print(i[0])
        
        if(i[2]==password) and (i[0]==fileslice):
            key=i[1]
            
            stop=0
            f = Fernet(key)
            with open(filename, "rb") as file:
                # read the encrypted data
                encrypted_data = file.read()
            # decrypt data
            decrypted_data = f.decrypt(encrypted_data)
            # write the original file
            with open(filename+'_decrypted'+extension, "wb") as file:
                file.write(decrypted_data)

    if(stop==1):
        print("File or Password is wrong")
            
    
# def key_methods(): 
    

# encrypt('assets/Assignment 1-android dev..PNG', key_methods)
# decrypt('assets/Assignment 1-android dev..PNG_encrypted', key_methods)
#https://www.thepythoncode.com/article/encrypt-decrypt-files-symmetric-python