test_str = input("Enter message:")
alphabet = ("a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z")    
arr = []
digits = []
finalArr = []
end = ""
for  i in test_str:
    arr.append(i)
for i in arr:
    try:
        digits.append(int(i))
    except ValueError:
        digits.append(i)
for i in digits:
    if isinstance(i, int):
        for x in range(i):
            finalArr.append(0)
    else:
        for x in range(alphabet.index(str(i)) + 1):
            finalArr.append(1)
for i in finalArr:
    end = end + str(i)
print(''.join(chr(int(end[i*8:i*8+8],2)) for i in range(len(end)//8)))