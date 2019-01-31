#!/usr/bin/env python3

import sys, getopt, detectEnglish, trdecode


def usage():
    print('Usage: a1.py -i <inputfile> -k <max key size>')
    print('Usage: a1.py -s <inputstring> -k <max key size>')

def main(argv):
    is_inputfile = False
    is_inputstring = False
    inputfile = ''
    inputstring = ''
    max_key = 0

    try:
        opts, args = getopt.getopt(argv, "s:i:k:",["inputstring=", "inputfile="])
    except getopt.GetoptError:
        print (usage())
        sys.exit(2)

    for opt, arg in opts:
        if opt in ("-i", "--inputfile"):
            inputfile = arg
            is_inputfile = True
        elif opt in ("-s", "--inputstring"):
            inputstring = arg
            is_inputstring = True
            print("input string: ", arg)
        elif opt in ("-k", "--max_key"):
            max_key = int(arg)
            max_key = max_key + 1
        elif opt in ("-h", "--help"):
            print (usage())


    if (is_inputfile == True) and (is_inputstring == True):
        print(usage())
    elif (is_inputfile == True):                #check entire file
        for key in range (1, max_key):
            print("trying keysize: ", key)

            with open(inputfile) as f:
                while True:
                    c = f.read(key)

                    if not c:
                        print ("EOF")
                        break

                    result = trdecode.decryptMessage(key, c)

                    if detectEnglish.FindEnglish(result):
                       print("Found: ", result)
                       answer = input("Continue? (y/n)")
                       if answer == "n":
                           break

    elif (is_inputstring == True):              #check only string from command line
        for key in range (1, max_key):
            print("trying keysize: ", key)

            result = trdecode.decryptMessage(key, inputstring)
            print("Found: ", result)

            if detectEnglish.FindEnglish(result):
               print("Found: ", result)
               answer = input("Continue? (y/n)")
               if answer == "n":
                   break
    else:
        print(usage())

if __name__ == "__main__":
    main (sys.argv[1:])
