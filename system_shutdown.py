import os
lists=['shut down','account switcher']
for i in range(len(lists)):
               print(str(i+1)+". "+lists[i])
user_option=int(input("your choice(1/2)"))
if(user_option==1):
               os.system("shutdown /s /t 1")
elif(user_option==2):
    os.system("shutdown /l")
else:
    print("invalid option chosen")
    
    
