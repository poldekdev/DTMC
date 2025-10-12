# Some imports
import base64
from cryptography.fernet import Fernet
import random_word
import random

r = random_word.RandomWords()


# The very-super-secret obfuscation
def obfuscate(filename: str, strength):
    try:
        f = open(filename, "r", encoding="utf-8")
    except FileNotFoundError:
        print(f"{filename} doesn't exist!")
        exit(1)
    code = f.read().encode("utf-8")
    print(f"[LOG] Loaded {filename}")
    f.close()
    obf_file = open(f"{filename}-obfuscated.py", "w")
    key = Fernet.generate_key()
    x = Fernet(key)
    y = r.get_random_word()
    z = r.get_random_word()
    miss_spell = r.get_random_word()
    base64_enc_code = base64.b64encode(code)
    print(base64_enc_code)
    obf_code = x.encrypt(base64_enc_code)
    obf_code = f"""from cryptography.fernet import Fernet;import base64;x=Fernet("{key.decode("utf-8")}");code=x.decrypt("{obf_code.decode("utf-8")}");base64_dec_code=base64.b64decode(code.decode("utf-8"));exec((base64_dec_code.decode("utf-8")))"""
    ready_code = base64.b64encode(obf_code.encode("utf-8"))
    deployment = f"""from base64 import b64decode as iIiIiI;import os as IiIiII; import random as OoOoOo; import math as UuUuUu; 
def {y}(): 
    oOoOoO = iIiIiI({ready_code})
    exec(oOoOoO.decode('utf-8'))
{y}()
"""
    fun = []
    for i in range(strength):
        random_data = base64.b64encode(random.randbytes(300)).decode("utf-8")
        func_name = r.get_random_word()
        var_name = r.get_random_word()

        funcode = f"""from base64 import b64decode as iIiIiI;import os as IiIiII; import random as OoOoOo; import math as UuUuUu; 
def {func_name}(): 
    oOoOoO = "{random_data}"
    try:
        {var_name} = iIiIiI(oOoOoO)
        exec({var_name}.decode('utf-8'))
    except Exception as DTMC:
        pass
"""

        funcode_2 = f"""from base64 import b64decode as iIiIiI;import os as IiIiII; import random as OoOoOo; import math as UuUuUu; 
def {r.get_random_word()}(): 
    oOoOoO = "{random_data}"
    {r.get_random_word()} = OoOoOo.randint(0, 1000000)
    try:
        exec(iIiIiI(oOoOoO).decode('utf-8'))
    except:
        pass
"""

        funcode_3 = f"""from base64 import b64decode as iIiIiI;import os as IiIiII; import random as OoOoOo; import math as UuUuUu;
def {r.get_random_word()}():
    oOoOoO = "{random_data}"
    PpPpPpP = OoOoOo.randint(0, 999999)
    try:
        exec(iIiIiI(oOoOoO).decode('utf-8'))
    except:
        pass
"""

        gamble = random.randint(1, 3)
        if gamble == 1:
            fun.append(funcode)
        elif gamble == 2:
            fun.append(funcode_2)
        else:
            fun.append(funcode_3)

    file_content = "".join(fun) + "\n" + deployment + "\n" + "".join(fun)
    obf_file.write(file_content)
    obf_file.close()
    print(f"[LOG] Obfuscated {filename}")
    print(f"[LOG] Saved as {filename}-obfuscated.py")


# Nice UI Stuff
def main():
    print("DTMC (Don't touch my code) ver. 1.0")
    print("Developed by poldekdev")
    filename = input("Input your file name: ")
    range = int(
        input("Input obfuscation strength (higher values might cause high file size): ")
    )
    obfuscate(filename, range)


# Runningggggg
if __name__ == "__main__":
    main()
