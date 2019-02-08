#!/usr/bin/env python3

import sys, getopt, detectEnglish, trdecode


def usage():
    print('Usage: a1.py -i <inputfile> -k <max key size>')
    print('Usage: a1.py -s <inputstring> -k <max key size>')

def decrypt_file(inputfile, key):
    #open input file
    with open(inputfile, 'r') as i:
        #get keysize number of characters
        inputstring = i.read()
        inputstring = inputstring.rstrip()

    #open results file
    with open("results.txt", 'w') as o:
        #decrypt into results file
        o.write(trdecode.decryptMessage(key, inputstring))

    #close files
    i.close()
    o.close()

def check_dictionary(inputstring, max_key):
    #iterate through every possible key size
    for key in range (1, max_key):
        #decrypt with potential key
        result = trdecode.decryptMessage(key, inputstring)
        print("Key:", key, "String: ", result)

        #check if key is potentially right
        if detectEnglish.FindEnglish(result):
            #if user thinks the key is right, decrypt rest of ciphertext
            print("Key: ", key)
            answer = input("Continue? (y/n)")
            if answer == "n":
                return key

    return 0

def main(argv):
    is_inputfile = False
    is_inputstring = False
    is_key = False
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
            is_key = True
            max_key = int(arg)
            max_key = max_key + 1
        elif opt in ("-h", "--help"):
            print (usage())


    if (is_inputfile == True) and (is_inputstring == True):
        print(usage())
    elif (is_inputfile == True):                #check entire file
        found = False

        with open(inputfile, 'r') as f:
            #get keysize number of characters
            c = f.read()
            #c = c.rstrip()

            #go to next keysize of EOF is found
            key_solution = check_dictionary(c, len(c))
            if key_solution != 0:
                decrypt_file(inputfile, key_solution)


    elif (is_inputstring == True):              #check only string from command line
        check_dictionary(inputstring, len(inputstring))
    else:
        print(usage())

if __name__ == "__main__":
    main (sys.argv[1:])
