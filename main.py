from asyncore import write
import os
import time
from colorama import Fore 


#to clear commond prompt > program beauti
os.system("clear")

#to show program name > this will cahanges
print(Fore.CYAN + """
╔╦╗┌─┐┬┬ ┬ ┬  ╦═╗┌─┐┬  ┬┬┌─┐┬ ┬
 ║║├─┤││ └┬┘  ╠╦╝├┤ └┐┌┘│├┤ │││
═╩╝┴ ┴┴┴─┘┴   ╩╚═└─┘ └┘ ┴└─┘└┴┘


""")

# use try to program dont show errors > simple
try :
    note = input(Fore.YELLOW + time.strftime("%y/%m/%d - %A - %l:%M %p \nToday's achievements :\n\n> ") + Fore.WHITE)

    if note == "Nothing" or note == "nothing":
        print ("Just Go and Think Why")
        os.system("sudo shutdown now")

    else:
        datet = time.strftime("------ %y/%m/%d - %A - %l:%M %p ------\n\n")    
        out_file = open("Main.out", "a")
        out_file.write("\n\n\n\n")
        out_file.write(datet)
        out_file.write(note)
        out_file.close()
except: 
    time.sleep(2)
