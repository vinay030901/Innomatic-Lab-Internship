def print_formatted(number):
    l=len(bin(number)[2:])
    for i in range(1,number+1):
        dec=str(i)
        octal=oct(i)
        hexadec=hex(i)
        binary=bin(i)
        print(dec.rjust(l,' '),octal[2:].rjust(l,' '),hexadec[2:].upper().rjust(l,' '),binary[2:].rjust(l,' '))

if __name__ == '__main__':