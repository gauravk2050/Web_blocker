from time import sleep
ip = "127.0.0.1"
loop = True
while(loop):
    choice = str(input("Enter the choice\n1.Block a website\n2.unblock a website\n>> "))
    if choice == "1" :
        website = input("Enter the website you want to block>> ")
        with open("C:\Windows\System32\drivers\etc\hosts",'a') as file:
            file.write("\n"+ip+" "+website)
        loop = False
        print(website,"successfully blocked")
    elif choice == "2":
        try:
            website = input("Enter the website you want to unblock>> ")
            block_website=ip+" "+website
            with open("C:\Windows\System32\drivers\etc\hosts","r") as f:
                lines = f.readlines()
            with open("C:\Windows\System32\drivers\etc\hosts","w") as f:
                for line in lines:
                    if line.strip("\n") != block_website:
                        f.write(line)
        except exceptions as e:
            print(e)
        print(website,"successfully unblock")
        loop = False
    else:
        print("Wrong choice Try again!!!")
    
