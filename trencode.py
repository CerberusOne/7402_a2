#!/usr/bin/python3.5

# Transposition Cipher Encryption
#myMessage = 'A wilderness of mirrors'
#myKey = 12

import sys, getopt

def main (argv):
    is_file = False
    is_outfile = False
    plaintext = ''
    keylen = 0

    try:
        opts, args = getopt.getopt (argv, "ht:k:i:o:",["ptext=", "keysize=", "ifile=", "ofile="])

    except getopt.getoptError:
        sys.exit (1)

    if len (sys.argv[1:]) < 4:
        print ('Usage: ./trencode.py -t <plaintext> -k <keysize>')
        sys.exit(2)
    for opt, arg in opts:
        if opt == '-h':
            print ('Usage: ./trencode.py -t <plaintext> -k <keysize>')
            sys.exit ()
        elif opt in ("-t", "--ptext"):
            plaintext = arg
        elif opt in ("-i", "--pfile"):
            inputfile = arg
            is_file = True
        elif opt in ("-o", "--ofile"):
            outputfile = arg
            is_outfile = True
        elif opt in ("-k", "--keysize"):
            keylen = int (arg)

    if is_file and is_outfile:
        with open(inputfile, 'r') as i:
            inputstring = i.read()
            inputstring = inputstring.rstrip()
            ciphertext = encryptMessage(keylen, inputstring)

        with open(outputfile, 'w') as o:
            o.write(ciphertext)

        i.close
        o.close

    else:
        # call the crypto function
        ciphertext = encryptMessage (keylen, plaintext)

    # Print the ciphertext
    print(ciphertext)


def encryptMessage (key, message):

    # Each string in ciphertext represents a column in the grid.
    ciphertext = [''] * key

    # Iterate through each column in ciphertext.
    for col in range (key):
        pointer = col

        # process the complete length of the plaintext
        while pointer < len (message):
            # Place the character at pointer in message at the end of the
            # current column in the ciphertext list.
            ciphertext[col] += message[pointer]

            # move pointer over
            pointer += key

    # Convert the ciphertext list into a single string value and return it.
    return ''.join (ciphertext)


# If transpositionEncrypt.py is run (instead of imported as a module) call
# the main() function.
if __name__ == "__main__":
    main (sys.argv[1:])
