def encrypt():
    lines = []
    line = ''
    fileName = 'test.txt'
    case = ''
    listSpecial = []
    listUpper = []

    # loop through lines in list
    # and print the entire string
    with open (fileName) as fh:
        lines = fh.read().splitlines()
        print (lines)
        
        # print out per letter
        for letter in lines:
            if (letter.upper()):
                listUpper += letter.upper()
        
            listSpecial += letter
        
        
            listSpecial += listSpecial[-1]
        return listSpecial

def operation():
    st = encrypt()
    listSpecial = []
    op = 'C'
    
    aLetters = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                'h', 'i', 'j', 'k', 'l', 'm', 'n',
                'o', 'p', 'q', 'r', 's', 't', 'u',
                'v', 'w', 'x', 'y', 'z']
    
    if (op == 'C'):
        print ('Caesar Cipher:')
        for s in st:
            print (s)
           # print (abs(mod))
            # if () > 0):
            #    listSpecial += aLetters[mod+14]
            # else:
            listSpecial += aLetters[s+1]
            print (listSpecial)
    if (op == 'A'):
        for s in st:
            listSpecial += aLetters[13]
        print (listSpecial)
        
operation()