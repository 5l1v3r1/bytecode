#!/usr/bin/python
# -*- coding: utf-8 -*-

# iran-cyber.net - iraniancoders.ir

# Author = [ IWHH ]
import sys,time,os,random,webbrowser

try:
    from colorama import *
    r = Fore.RED
    g = Fore.GREEN
    w = Fore.WHITE
    b = Fore.BLUE
    y = Fore.YELLOW
    m = Fore.MAGENTA
    res = Style.RESET_ALL
except ImportError:
    linux = 'sudo apt install python-pip ; sudo pip install colorama'
    windows = 'pip install colorama'
    print 'Installing Colorama Module ...\nWhen FInished Run again ...'
    time.sleep(2)
    os.system([linux,windows][os.name == 'nt'])
    sys.exit()

try:
    import py_compile
except ImportError:
    linux = 'sudo apt install python-pip ; sudo pip install py_compile'
    windows = 'pip install py_compile'
    print 'Installing py_compile Module ...\nWhen FInished Run again ...'
    time.sleep(2)
    os.system([linux,windows][os.name == 'nt'])
    sys.exit()

try:
    import uncompyle6
except ImportError:
    linux = 'sudo apt install python-pip ; sudo pip install uncompyle6'
    windows = 'pip install uncompyle6'
    print 'Installing uncompyle6 Module ...\nWhen FInished Run again ...'
    time.sleep(2)
    os.system([linux,windows][os.name == 'nt'])
    sys.exit()

def cls():
    l = 'clear'
    w = 'cls'
    os.system([l,w][os.name == 'nt'])

cls()

def print_logo():
    clear = "\x1b[0m"
    colors = [36, 32, 34, 35, 31, 37]

    x = """
 /$$$$$$$              /$$                /$$$$$$                  /$$
| $$__  $$            | $$               /$$__  $$                | $$
| $$  \ $$ /$$   /$$ /$$$$$$    /$$$$$$ | $$  \__/  /$$$$$$   /$$$$$$$  /$$$$$$
| $$$$$$$ | $$  | $$|_  $$_/   /$$__  $$| $$       /$$__  $$ /$$__  $$ /$$__  $$
| $$__  $$| $$  | $$  | $$    | $$$$$$$$| $$      | $$  \ $$| $$  | $$| $$$$$$$$
| $$  \ $$| $$  | $$  | $$ /$$| $$_____/| $$    $$| $$  | $$| $$  | $$| $$_____/
| $$$$$$$/|  $$$$$$$  |  $$$$/|  $$$$$$$|  $$$$$$/|  $$$$$$/|  $$$$$$$|  $$$$$$$
|_______/  \____  $$   \___/   \_______/ \______/  \______/  \_______/ \_______/
           /$$  | $$      python ByteCode deompile & Compiler v1.0
          |  $$$$$$/
           \______/         github.com/iwhh
                            iraniancoders.ir - iran-cyber.net



    """
    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" %(random.choice(colors), line, clear))
        time.sleep(0.05)
cls()
print_logo()

def ads():
    webbrowser.open('https://t.me/IRCoders')
ads()
def main():
    try:
        choose = sys.argv[1]
    except:
        print Fore.MAGENTA + '\t--------------------------------------------------'
        print y + '\t[' + r + '~' + y + '] ' + w + 'compile --> ' + g + 'python bytecode.py 1\n\t' + y + '[' + r + '~' + y + '] ' + w + 'decompile --> ' + g + 'python bytecode.py 2'
        sys.exit()
    if choose == '1':
        time.sleep(2)
        print y + '\t\t\t-->' + r + ' you Selected Compile ' + y + '<--'
        print Fore.MAGENTA + '\t\t-----------------------------------------'
        user_input = raw_input(y + '\t\t[' + r + '*' + y + '] ' + g + 'Enter Your Filename >>> ')
        try:
            py_compile.compile(user_input)
        except:
            print 'Programm Closed'
            sys.exit()
        time.sleep(2)
        print y + '\t\t[' + r + '!' + y + '] ' + w + str(user_input) + g + ' Compiled to --> ' + w + str(user_input)+'c'
    elif choose == '2':
        time.sleep(2)
        print y + '\t\t\t-->' + r + ' you Selected DeCompile ' + y + '<--'
        print Fore.MAGENTA + '\t\t-----------------------------------------'
        pycfile = raw_input(y + '\t\t[' + r + '*' + y + '] ' + g + 'Enter Your Filename [.pyc] >>> ')
        pyfile = raw_input(y + '\t\t[' + r + '*' + y + '] ' + g + 'Enter .py file to save ' + w + str(pycfile) + ' in them >>> ')
        try:
            with open(pyfile, 'wb') as e:
                uncompyle6.uncompyle_file(pycfile, e)
                print y + '\t\t[' + r + '+' + y + '] ' + g + 'File Saved To --> ' + w + str(pyfile)
        except:
            print y + '[' + r + '-' + y + '] ' + g + 'Unsuccessful'
            sys.exit()
if __name__ == "__main__": main()
