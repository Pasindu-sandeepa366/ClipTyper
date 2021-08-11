import clipboard as cp
from pynput.keyboard import Key,Listener 
import pyautogui

class process:
    def __init__(self):
        self.esc = 0
        self.keyhis = '     ' #set history
    
    def espupdate(self):
        if self.esc == 0:
            self.esc = 1
        else:
            self.esc = 0

    def his(self,key):
        if len(str(key)) == 3:
            replace_key = str(key).replace("'","")
            self.keyhis = f"{str(self.keyhis)[1:]}{replace_key}"
            #print(f'update > {self.keyhis}')
        else:
            pass
process_var = process()
def check(process):
    command = {}
    with open('data.txt','r') as data:
        dataRead = data.readlines()
        
    for i in range(len(dataRead)):
        if dataRead[i][-1:] == '\n':
            dataRead[i] = dataRead[i][0:-1]
        else:
            pass
        if True:
            #print(dataRead[i])
            if ':' in dataRead[i]:
                dataLine = dataRead[i].split(':')
            else:
                print('Command list not support..!')
                quit()
            try:
                #print(dataLine[0])
                if len(dataLine[0]) > 5:
                    print('Please use less than 5 character in command')
                    quit()
                command[dataLine[0]] = dataLine[1]
            except:
                print('Command list not support..!')
                quit()
    for i in command:
        if i in process.keyhis:
            count = 0
            while count < len(i):
                pyautogui.press('backspace')
                count += 1
            print(f'{i} > {command[i]}')
            cliphis = cp.paste()
            cp.copy(command[i])
            pyautogui.keyDown('ctrl')
            pyautogui.press('v')
            pyautogui.keyUp('ctrl')
            cp.copy(cliphis)
            process.keyhis = process.keyhis.replace(i,' '*len(i))
            #print(process.keyhis)
        
def onPress(key,process = process_var):
    if key == Key.esc:
        process.espupdate()
        if process.esc == 1:
            print("Runing...")
        else:
            print('Pause ||')

def onRelease(key,process = process_var):
    if process.esc == 1:
        process.his(key)
        check(process)
    else:
        pass        

print('''
           ClipTyper1.0
    [+]Coded_by_Pasindu_Sandeepa
    [@]bombtiktiktik54321@gmail.com

''')
try:
    with Listener(on_press = onPress, on_release = onRelease ) as listner:
        listner.join()
except KeyboardInterrupt:
    print("User terminated programme")
