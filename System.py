import random
print("\033[0;37m  \n")
devices = [ ["Toaster", "Blender", "Mouse", "Dishwasher", "Keyboard"], ["Phone", "PC", "C202", "Micro:Bit", "Eniac"]]
if  len(devices[0]) == len(devices[1]):
        print("In this quiz, Your device will give you some devices.")
        print("You must say if a device is embedded or not.")
        print("(0 = Embedded/Dedicated, 1 = General-Purpose)")
        score = 0
        loop = 0
        while loop==0:

            DType = 0 #random.randint(0, len(devices)-1)
            TDevice = 1 #random.randint(0, len(devices[1])-1)
            print(devices[DType][TDevice])
            ans = int(input("0 or 1?"))
            print(DType)
            if ans == DType:
                print("\033[0;32m Correct!  \n")
                print("\033[0;37m Next Question! \n")
                score = score+1

            else:
                loop = 1
                print("\033[0;31m Incorrect  \n")
                print("\033[0;31m Quiz Over!!!  \n")
                print("\033[0;32m your score is:  \n")
                print(score)
                print("\033[0;37m  \n")
else:
    print("\033[0;31m Error  \n")
