#!/usr/bin/env python3
# -*- coding: UTF-8 -*-
#-----------------------
#Fast & Powerful hash cracker script
#Install it and use them enywhere!

#With command: xCracker -t [hash-type] -H [hash-value] -w [wordlist] -v [enable-verbose]
#With command: xCracker -t [hash-type] -H [hash-value] -w [wordlist] <without verbosity>

#Follow me on github:
#https://github.com/C-PyLx
#Report bugs to:
#https://t.me/Ac3ess
#gmail: cpylxlearning@gmail.com

#Modules:
import os
import sys
import time
import hashlib
import argparse

#Terminal colors code:
green = '\033[0;32m'
red = '\033[0;31m'
blue = '\033[0;34m'
cyan = '\033[0;96m'
end = '\033[0m'

#Functions:
def logo():    
    os.system('clear')
    print (red + """-- --   ???? ?? ?? ??????  ???? ??  ??
 \-/ _ ??    ???   ??__?? ??    ????
 /-\   ??    ??    ??  ?? ??    ????
-- --   ???? ??    ??  ??  ???? ??  ??""", end)
    print (cyan + """     < Coded by: Learning :~# >
          < Version: 2.0 >
    < https://github.com/C-PyLx >
""", end)

def Usage():
    print ('''[ ~ ] Usage commands & supports:
--------------
\033[0;96mex(1): python3 xCracker.py -t [hash-type] -H [hash-value] -w [wordlist] -v [enable-verbose]\033[0m
\033[0;96mex(2): python3 xCracker.py -t [hash-type] -H [hash-value] -w [wordlist]\033[0m
--------------
\033[0;92mus(1): python3 xCracker.py -t md5 -H e710bd5c9954d75a973406effb384095 -w wordlist.txt -v\033[0m
\033[0;92mus(2): python3 xCracker.py -t sha1 -H 11f6ad8ec52a2984abaafd7c3b516503785c2072 -w passlist.txt\033[0m
''')

class Program:

    def xCracker(typest, value, word, verbose=False):
        start = time.time()
        counter = 0

        if typest == 'md5':
            mod = hashlib.md5
        elif typest == 'sha1':
            mod = hashlib.sha1
        elif typest == 'sha224':
            mod = hashlib.sha224
        elif typest == 'sha256':
            mod = hashlib.sha256
        elif typest == 'sha384':
            mod = hashlib.sha384
        elif typest == 'sha512':
            mod = hashlib.sha512
        else:
            print (red + '[ ! ] Unsupported hash type!', end)
            Usage()
            sys.exit()

        logo()
        try:
            inFile = open(word, 'rU')
        except IOError:
            print (red + '\n[ X ] Can not open wordlist !', end)
            sys.exit()
        except FileNotFoundError:
            print (red + '\n[ X ] Wordlist not found !', end)
            sys.exit()

        for line in inFile:
            line = line.strip()
            wordHash = mod(line.encode()).hexdigest()

            if verbose:
                sys.stdout.write(cyan + '\r' + '[ ~ ] Trying word: { ' + str(line) + ' }' + ' '*18 + end)
                sys.stdout.flush()
                
            if wordHash == value:
                endTime = time.time()

                print (red + '\n\n~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~', end)
                print (green + '[ * ] Hash-Word: { %s }' %wordHash, end)
                print (green + '[ * ] Pass-Word: { %s }' %line, end)
                print (red + '~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~:~', end)
                print (cyan + '\n[ + ] Words tried: { %s }' %counter, end)
                print (cyan + '[ + ] Time elapsed: { %s } seconds.' %round(endTime-start, 2), end)
                print ()
                sys.exit()
                
            else:
                counter += 1
        endTime = time.time()

        print (red + '\n[ X ] Password not cracked!', end)
        print (cyan + '[ + ] Words tried: { %s }' %counter, end)
        print (red + '[ ! ] Try another wordlist.', end)
        print (cyan + '\n[ + ] Time elapsed: { %s } seconds.' %round(endTime-start, 2), end)
        print ()
        sys.exit()

    def main():
        parser = argparse.ArgumentParser(
            formatter_class=argparse.RawTextHelpFormatter,
            description=green+'Python fast & powerful hash cracker.'+end,
            usage=Usage())
        
        parser.add_argument('-t', '--type',
        help=cyan+'hash type (See supported hashes)!'+end,
        type=str,
        default='md5')
        parser.add_argument('-H', '--hash',
        help=cyan+'hash value (hash sums)!'+end,
        type=str,
        default='e710bd5c9954d75a973406effb384095')
        parser.add_argument('-w', '--word',
        help=cyan+'wordlist filepath (ex:words.txt)!'+end,
        type=str,
        default='words.txt')
        parser.add_argument('-v', '--verbose',
        help=cyan+'enable verbosity (Slow cracking)!'+end,
        action='store_true',
        default=False)

        args = parser.parse_args()
        Program.xCracker(args.type, args.hash, args.word, args.verbose)

if __name__ == '__main__':
    Program.main()

else:
    sys.exit()