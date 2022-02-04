import logging
logging.basicConfig(level=logging.INFO, format=' %(asctime)s - %(levelname)s - %(message)s')
logging.disable()
logging.info("Start of program.")


def ATM(lis):


    l,s=User(lis)
    bal=int(l[2])
    logging.info(bal)
    l[1]=Card(l[1])
    while (True):
        print ("Authentication successful! \n1) Check balance\n2) Deposit\n3)Withdrawal\n4) Change pin\n5) Exit")
        logging.info("Pin authenticated")
        try:
            n=int(input(("Enter the serial number.")))
        except ValueError:
            print("Enter an integer from 1 to 5.")
            continue
        if (n<1 or n>5):
            print("Enter an integer from 1 to 5.")
            continue
        if (n==5):
            print("Thank you for using this ATM")
            break
        l[1],l[2]=Account(n,s,l,lis)


        x=int(input("Do you want to exit? Enter 0 if yes and 1 if no."))
        if (x!=0 and x!=1):
            print("Invalid choice.")
            continue

        if (x==0):
            print("Thank you for using this ATM.")
            break


def User(lis):

    li=[]

    user = input("Enter username.")

    for s in range(len(lis)):
        i=lis[s]
        li=i.split(sep=",")

        if (li[0]==user):
            logging.info("Username authenticated.")

            return(li,s)
    print("Invalid username.")
    return User(lis)
def Card(pi):
    pin=0
    pi=int(pi)
    if (pi==0):
        while (True):
            try:
                pin=int(input("Enter a new pin."))
            except ValueError:
                print("Enter a 4 digit integer.")
                continue
            if (pin<1000 or pin>9999):
                print("Enter a 4 digit integer.")
                continue
            break
    else:
        while (True):
            try:
                pin=int(input("Enter the pin."))
            except ValueError:
                print("Enter a 4 digit integer.")
                continue
            break
        if (pi!=pin):
            print("Invalid pin")
            Card(pi)
    return (pin)
def Account(n,s,l,lis):
    bal=int(l[2])
    pin=l[1]
    logging.info(bal)
    if (n==3):
        while (True):
            try:
                d=int(input("How much do you want to withdraw."))
            except ValueError:
                print("Enter a positive integer.")
                continue
            break
        if (d>bal):
            print ("Account balance is insufficient.")

        else:
            bal-=d

    if (n==2):
        while (True):
            try:
                p=int(input("How much money do you want to deposit?"))
            except ValueError:
                print("Enter a positive integer.")
                continue
            break
        bal+=p

    if (n==4):
        while(True):
            try:
                l[1] = int(input("Enter the new pin."))
            except ValueError:
                print("Enter a 4 digit integer.")
                continue
            if (pin < 1000 or pin > 9999):
                print("Enter a 4 digit integer.")
                continue
            break
    else:
        print("Account balance: ", bal)
    l[2]=bal
    st=str(l[0])+","+str(l[1])+","+str(l[2])
    file = open("Data.txt", "w+")
    for i in range(len(lis)):
        if (i!=s):
            file.write(lis[i])
        else:
            file.write(st+"\n")

    return (pin,bal)



def main():
    f = open("Data.txt", "r+")
    lis=[]
    lis = f.readlines()

    ATM(lis)
    logging.info("End of program")
main()


