import struct, hashlib, time, os, random, string
import sys
from Crypto.Cipher import AES
from Crypto.PublicKey import RSA
from Crypto.Hash import SHA256 as SHA
from Crypto.Signature import PKCS1_v1_5
from Crypto.Cipher import PKCS1_OAEP

def aes_en(inputfile, pri_key_file, pub_key_file):
    output = "cryaes"
    iv = ""
    aes_key = ""
    for i in range(16):
        iv += random.choice(string.ascii_letters + string.digits)
    for i in range(32):
        aes_key += random.choice(string.ascii_letters + string.digits)
    print(aes_key)
    encry = AES.new(aes_key.encode("utf8"), AES.MODE_CBC, iv.encode("utf8"))
    size = os.path.getsize(inputfile)
    tmp = os.path.basename(inputfile)
    with open(inputfile, "rb") as plain:
        with open(output, "wb") as chiper:
            chiper.write(struct.pack("<Q",size))
            chiper.write(struct.pack("<Q",len(tmp.encode("utf8"))))
            chiper.write(tmp.encode("utf8"))
            chiper.write(iv.encode("utf8"))
            while True:
                block = plain.read()
                if len(block) == 0:
                    break
                elif len(block) % 16 != 0:
                    block += " ".encode("utf8") * (16 - len(block) % 16)
                chiper.write(encry.encrypt(block))
        with open(output, "rb") as tmp:
            print(tmp.read())
    sign(pri_key_file, pub_key_file, output, os.path.getsize(output), aes_key)
    #os.remove(inputfile)'''

def aes_de(inputfile, pub_key_file, pri_key_file):
    with open(pub_key_file, "rb") as pub:
        try:
            pub_key = RSA.importKey(pub.read())
        except ValueError:
            print("올바른 형태의 공개키가 아닙니다.")
            #sys.exit()

    with open(pri_key_file, "rb") as pri:
        try:
            pri_key = RSA.importKey(pri.read())
        except ValueError:
            print("올바른 형태의 개인키가 아닙니다.")
            #sys.exit()
        
    key = verify(pub_key, pri_key, inputfile)
    
    with open(inputfile, "rb") as chiper:
        size = struct.unpack("<Q",chiper.read(struct.calcsize("Q")))[0]
        namelen = struct.unpack("<Q",chiper.read(struct.calcsize("Q")))[0]
        file_name = chiper.read(namelen).decode("utf8")
        iv = chiper.read(16)
        decry = AES.new(key, AES.MODE_CBC, iv)
        tmp = os.path.dirname(inputfile)
        with open(tmp+"//"+file_name, "wb") as plain:
            while True:
                block = chiper.read()
                if len(block) == 0:
                    break
                plain.write(decry.decrypt(block))
            plain.truncate(size)
    #os.remove(inputfile)

def sign(pri_key, pub_key, inputfile, size, aes_key):
    with open(pri_key, "rb") as pri:
        try:
            my_key = RSA.importKey(pri.read())
        except ValueError:
            print("올바른 형태의 개인키가 아닙니다.")
            #os.remove(inputfile)
            #sys.exit()
        
    with open(pub_key, "rb") as pub:
        try:
            op_key = RSA.importKey(pub.read())
        except ValueError:
            print("올바른 형태의 공개키가 아닙니다.")
            os.remove(inputfile)
            #sys.exit()
        
    with open(inputfile, "rb") as file:
        hash = SHA.new(file.read())
       # print(hash)

    try:
        sign = PKCS1_v1_5.new(my_key).sign(hash)
    except TypeError:
        print("개인키 형태의 파일이 아닙니다.")
        os.remove(inputfile)
        #sys.exit()

    en = PKCS1_OAEP.new(op_key)
    endata = en.encrypt(aes_key.encode("utf-8"))

    with open(inputfile, "ab") as file:
        file.write(sign)
        file.write(struct.pack("<Q",size))
        file.write(endata)
        file.write(struct.pack("<Q",len(endata)))

def verify(pub_key, pri_key, inputfile):
    
    with open(inputfile, "ab+") as file:
        file.seek(-struct.calcsize("Q"),2)
        size = struct.unpack("<Q",file.read())[0]
      
        try:
            file.seek(-(size+struct.calcsize("Q")),2)
        except OSError:
            print("파일의 내용 수정되었습니다.")
            #sys.exit()
        endata = file.read(size)
        de = PKCS1_OAEP.new(pri_key)
        try:
            dedata = de.decrypt(endata)
        except ValueError:
            print("올바른 개인키가 아닙니다.")
            sys.exit()
        except TypeError:
            print("개인키 형태의 파일이 아닙니다.")
            #sys.exit()
        file.seek(-(size+struct.calcsize("Q")),2)
        file.truncate()
        file.seek(-struct.calcsize("Q"),2)
        size = struct.unpack("<Q",file.read())[0]
        file.seek(0)
        msg = file.read(size)
        file.seek(-struct.calcsize("Q"),2)
        file.truncate()
        file.seek(size)
        sign = file.read()
   
    veri = PKCS1_v1_5.new(pub_key)
    hash = SHA.new(msg)
    try:
        veri.verify(hash, sign)

    except:
        print("파일의 내용이 수정되었습니다.")


    return dedata
