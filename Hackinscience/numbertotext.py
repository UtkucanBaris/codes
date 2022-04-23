Ones = ["", "One", "Two", "Three", "Four",
        "Five", "Six", "Seven", "Eight", "Nine"]
Tens = ["", "Ten", "Twenty", "Thirty", "Fourty",
        "Fifty", "Sixty", "Seventy", "Eighty", "Ninety"]
Thousands = ["Million", "Thousand", "Hundred", ""]
Specials = ["Ten", "Eleven", "Twelve", "Thirteen", "Fourteen",
            "Fifteen", "Sixteen", "Seventeen", "Eighteen", "Nineteen"]
# "000 000 000"
for x in range(1998, 2002):
    Y = ""
    sayi = str(x)
    sayi1 = (9-len(sayi))
    sayi2 = ""
    for st in range(1, sayi1+1):
        sayi2 += sayi2.join("0")
    sayi = sayi2+sayi
    for i in range(0, 3):
        c1 = int(sayi[i*3])
        c2 = int(sayi[i*3+1])
        c3 = int(sayi[i*3+2])
        if c1 == 0 and Y != "":
            Y = Y+""
        if c1 >= 1:
            Y = Y+Ones[c1]+Thousands[i]
        if c2 == 1:
            Y = Y+Specials[c3]
        if i == 1 and c3 != 0:
            Y = Y+Ones[c3]+Thousands[i]
        else:
            Y = Y+Tens[c2]+Ones[c3]
    print(Y)
