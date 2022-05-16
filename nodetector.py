#! usr/bin/python3

#created by : Mr1-D3CRYPT


# script to detect if a given number has a phone number

def check(nus):
    if nus[0] == '9' and nus[1] == '1':
        return True


text = input("Enter the string u wanna calc :  ")

foundno = False

for s in range(len(text)):
    if text[s] == '+':
        no = text[s + 1:s + 3]
        val = check(no)
        if val == True:
            if text[s + 1:s + 13].isdecimal():
                try:
                    if text[s+14].isdecimal():
                        break
                except Exception:
                    print()
                print("Number found :", text[s:s + 13])
                foundno = True

if not foundno:
    print("Opps!! No not found..")
