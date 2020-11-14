class laptop :
    def __init__(self,price,screen_size,ram,hdd):
        self.price=price
        self.screen_size=screen_size
        self.ram=ram
        self.hdd=hdd

    def details(self):
        print("PRICE = "+str(self.price) +"  RAM = "+str(self.ram)+"  STORAGE = "+str(self.hdd))
        return " "


class mobile(laptop) :

    def __init__(self,price,ram,hdd,battery):
        self.price = price
        self.battery = battery
        self.ram = ram
        self.hdd = hdd


lap0=laptop(55000,15.6,8,1.5)
lap1=laptop(63000,15.6,8,1)
lap2=laptop(53000,14,8,2)
lap3=laptop(39000,15.6,4,1)
lap4=laptop(79000,17.8,32,2)
lap5=laptop(45000,14,4,1)


mob0=mobile(15000,4,64,4000)
mob1=mobile(20000,6,128,4000)
mob2=mobile(18000,6,64,5000)
mob3=mobile(10000,3,32,5000)
mob4=mobile(16000,4,128,5000)
mob5=mobile(50000,8,512,6000)

dvc= [lap0,lap1,lap2,lap3,lap4,lap5,mob0,mob1,mob2,mob3,mob4,mob5]
#price filter
def filter_price(price) :
    if (device==1):

        for i in range(0, 6):
            if (int(dvc[i].price) <= price):
                print("--->LAPTOP-" + str(i))
                print(str(dvc[i].details()))
        return "THE PRIZE FILTER HAS BEEN APPLIED"

    elif(device==2):
        for i in range(6, 12):
            if (int(dvc[i].price) <= price):
                print("--->MOBILE-"  +str(i-6) )
                print(str(dvc[i].details()))
        return "THE PRIZE FILTER HAS BEEN APPLIED"



#ram filter

def filter_ram(ram) :
    if (device == 1):

        for i in range (0,6):
            if (int(dvc[i].ram) >= ram):
                print("--->LAPTOP-" + str(i) )
                print( str(dvc[i].details()))
        return "WE HAVE APPLIED RAM FILTER FOR YOU"

    elif (device == 2):
        for i in range(6, 12):
            if (int(dvc[i].ram) >= ram):
                print("--->MOBILE-" + str(i - 6))
                print(str(dvc[i].details()))
        return "WE HAVE APPLIED RAM FILTER FOR YOU"


#hdd filter
def filter_hdd(hdd) :
    if (device == 1):

        for i in range (0,6):
            if (int(dvc[i].hdd) >= hdd):
                print("--->LAPTOP-" + str(i))
                print(str(dvc[i].details()))
        return "HDD FILTER HAS BEEN APPLIED"

    elif (device==2):

        for i in range (6,12):
            if (int(dvc[i].hdd) >= hdd):
                print("--->MOBILE-" + str(i - 6))
                print(str(dvc[i].details()))
        return "HDD FILTER HAS BEEN APPLIED"



#SCREEN SIZE FILTER

def filter_scrn_sze(scrn_sze) :

    for i in range (0,6):
        if (float(dvc[i].screen_size) >= scrn_sze):
            print("--->LAPTOP-" + str(i))
            print(str(dvc[i].details()) +"SCREEN SIZE = "+ str(dvc[i].screen_size))
    return "SCREEN SIZE FILTER HAS BEEN APPLIED"

#battery capacity filter
def filter_battery (bat):
    for i in range (6,12):
        if (dvc[i].battery >= bat):
            print("--->MOBILE "+ str(i-6)+"BATTERY = "+str(dvc[i].battery))
            print(str(dvc[i].details()))

    return "BATTERY FILTER HAS BEEN APPLIED"



print(      "\n\n\n               ~~~~> WELCOME TO LAPILE-BUY.COM \n             ~~~~> FIND THE LAPTOP OF YOUR CHOICE \n          ~~~~> HAVE A GREAT EXPERIENCE")

device = int(input("HEY !!! LOOKING FOR A MOBILE OR LAPTOP \n FOR LAPTOP ENTER '1' AND FOR MOBILE ENTER '2'   "))
#laptop section
if (device==1):
    print("YOU ARE VIEWING LAPTOP SECTION")



    try:
        PRICE = int(input("ENTER MAXIMUM PRICE : "))
        print(filter_price(PRICE))
    except:
        print("ENTER A VALID INPUT")

    try:
            RAM = int(input("ENTER RAM CAPACITY : "))
            print(filter_ram(RAM))
    except:
            print(" ENTER A VALID RAM CAPACITY ")

    try:
            HDD = int(input("ENTER HDD SIZE in TERA-BYTE {TB}: "))
            print(filter_hdd(HDD))
    except:
            print("ENTER HDD STORAGE CAPACITY IN TB")


    SCREEN_SIZE = float(input("ENTER SCREEN_SIZE : "))
    print(filter_scrn_sze(SCREEN_SIZE))

    print("ENETR A SUITABLE SCREEN SIZE")

    print("Hope you found what you wished for")
    print("~~~~> VISIT AGAIN")
    last=input("ENTER ANY KEY TO CLOSE")

#mobile section
elif (device ==2) :
    print("YOU ARE VIEWING MOBILE SECTION")
    try:
        PRICE = int(input("ENTER MAXIMUM PRICE : "))
        print(filter_price(PRICE))
    except:
        print("ENTER A VALID INPUT")

    try:
        RAM = int(input("ENTER RAM CAPACITY : "))
        print(filter_ram(RAM))
    except:
        print(" ENTER A VALID RAM CAPACITY ")

    try:
        HDD = int(input("ENTER STORAGE SIZE in GIGA-BYTE {GB}: "))
        print(filter_hdd(HDD))
    except:
        print("ENTER STORAGE CAPACITY IN GB")

    try:
        BAT = int(input("ENTER BATTERY CAPACCITY IN mAh"))
        print(filter_battery(BAT))
    except:
        print("ENTER A VALID INPUT")
    print("Hope you found what you wished for")
    print("~~~~> VISIT AGAIN")

    last = input("ENTER ANY KEY TO CLOSE")





