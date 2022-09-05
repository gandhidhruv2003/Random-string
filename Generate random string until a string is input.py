try:
    def generate():
        import random
        s = ""
        alp = ["a","b","c","d","e","f","g","h","j","i","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
        num = ["1","2","3","4","5","6","7","8","9","0"]
        spe = ["!","@","#","$","%","^","&","*","(",")","-","_","+","=","[","{","]","}","|",";",":","'","<",",",">",".","?","/","`","~"]
        while(s==""):
            s = str(input("Enter a string: "))
            if(s==""):
                print(str(random.choice(alp)) + str(random.choice(num)) + str(random.choice(spe)))
    generate()
except:
    print("Enter correctly")