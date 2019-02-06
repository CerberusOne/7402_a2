#!/usr/bin/env python3

import sys, getopt, detectEnglish, trdecode


def usage():
    print('Usage: a1.py -i <inputfile> -k <max key size>')
    print('Usage: a1.py -s <inputstring> -k <max key size>')

def check_dictionary(inputstring, max_key):
    for key in range (1, max_key):
        result = trdecode.decryptMessage(key, inputstring)
        print("Key:", key, "String: ", result)

        if detectEnglish.FindEnglish(result):
           answer = input("Continue? (y/n)")
           if answer == "n":
               return True

    return False

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
        found = False

        for key in range (1, max_key):
            #make new empty list of key size length
            print("trying keysize: ", key)

            with open(inputfile) as f:
                while True:
                    #get keysize number of characters
                    c = f.read(key)

                    #go to next keysize of EOF is found
                    if c == '':
                        print ("Found: EOF")
                        break

                    found = check_dictionary(c, key)

                    if found:
                        break
            if found:
                break;


    elif (is_inputstring == True):              #check only string from command line
        check_dictionary(inputstring, max_key)
    else:
        print(usage())

if __name__ == "__main__":
    main (sys.argv[1:])
