# Some imports
import base64
from cryptography.fernet import Fernet
import random_word
import random

r = random_word.RandomWords()

# The very-super-secret obfuscation
def obfuscate(filename: str):
    try:
        f = open(filename, "r", encoding="utf-8")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
        exit(1)
    code = f.read().encode("utf-8")
    print(f"[LOG] Loaded {filename}")
    f.close()
    obf_file = open(f"{filename}-obfuscated.py", "x")
    key = Fernet.generate_key()
    x = Fernet(key)
    y = r.get_random_word()
    z = r.get_random_word()
    base64_enc_code = base64.b64encode(code)
    print(base64_enc_code)
    obf_code = x.encrypt(base64_enc_code)
    obf_code = f""" 
from cryptography.fernet import Fernet;import base64;x=Fernet("{key.decode("utf-8")}");code=x.decrypt("{obf_code.decode("utf-8")}");base64_dec_code=base64.b64decode(code.decode("utf-8"));exec((base64_dec_code.decode("utf-8")))
"""
    ready_code = base64.b64encode(obf_code.encode("utf-8"))
    deployment = f""" 
from base64 import b64decode as iIiIiI;import os as IiIiII; import random as OoOoOo; import math as UuUuUu; 
def {y}(): 
    oOoOoO = iIiIiI({ready_code})
    exec(oOoOoO.decode('utf-8'))
{y}()
    """
    fun = []
    for i in range(50):
        funcode = f""" 
from base64 import b64decode as iIiIiI;import os as IiIiII; import random as OoOoOo; import math as UuUuUu; 
def {r.get_random_word()}(): 
    oOoOoO = iIiIiI("{base64.b64encode(random.randbytes(100) + random.randbytes(100) + random.randbytes(100) + random.randbytes(100) + random.randbytes(100) + random.randbytes(100))}")
    exec(oOoOoO.decode('utf-8'))
        """
        funcode_2 = f""" 
from base64 import b64decode as iIiIiI;import os as IiIiII; import random as OoOoOo; import math as UuUuUu; 
def {r.get_random_word()}(): 
    oOoOoO = iIiIiI("{base64.b64encode(random.randbytes(100) + random.randbytes(100) + random.randbytes(100) + random.randbytes(100) + random.randbytes(100) + random.randbytes(100))}")
    exec(oOoOoO.decode('utf-8'))
        """
        if random.randint(1, 2) == 1:
            fun.append(funcode)
        else:
            fun.append(funcode_2)
    file_content = "".join(fun) + "" + deployment + "".join(fun)
    obf_file.write(file_content)
    obf_file.close()
    print(f"[LOG] Obfuscated {filename}")
    print(f"[LOG] Saved as {filename}-obfuscated.py")

# Nice UI Stuff
def main():
    print("DTMY (Don't touch my code) ver. 1.0")
    print("Developed by poldekdev")
    filename = input("Input your file name: ")
    obfuscate(filename)

# Runningggggg
if __name__ == "__main__":
    main()
