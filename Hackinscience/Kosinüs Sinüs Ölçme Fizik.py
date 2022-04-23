import math
#Cosinüs
def acos(x):
    if ac == int(45):
        x=0.7
    if ac == int(37):
        x=0.8
    if ac == int(53):
        x=0.6
    if ac == int(60):
        x=0.5
    if ac == int(30):
        x=0.87
    return x
def bcos(x):
    if bc == int(45):
        x=0.7
    if bc == int(37):
        x=0.8
    if bc == int(53):
        x=0.6
    if bc == int(60):
        x=0.5
    if bc == int(30):
        x=0.87
    return x
def ccos(x):
    if cc == int(45):
        x=0.7
    if cc == int(37):
        x=0.8
    if cc == int(53):
        x=0.6
    if cc == int(60):
        x=0.5
    if cc == int(30):
        x=0.87
    return x
def dcos(x):
    if dc == int(45):
        x=0.7
    if dc == int(37):
        x=0.8
    if dc == int(53):
        x=0.6
    if dc == int(60):
        x=0.5
    if dc == int(30):
        x=0.87
    return x
def ecos(x):
    if ec == int(45):
        x=0.7
    if ec == int(37):
        x=0.8
    if ec == int(53):
        x=0.6
    if ec == int(60):
        x=0.5
    if ec == int(30):
        x=0.87
    return x    
def asin(y):
    if ac == int(45):
        y=0.7
    if ac == int(37):
        y=0.6
    if ac == int(53):
        y=0.8
    if ac == int(60):
        y=0.87
    if ac == int(30):
        y=0.5
    return y
def bsin(y):
    if bc == int(45):
        y=0.7
    if bc == int(37):
        y=0.6
    if bc == int(53):
        y=0.8
    if bc == int(60):
        y=0.87
    if bc == int(30):
        y=0.5
    return y
def csin(y):
    if cc == int(45):
        y=0.7
    if cc == int(37):
        y=0.6
    if cc == int(53):
        y=0.8
    if cc == int(60):
        y=0.87
    if cc == int(30):
        y=0.5
    return y
def dsin(y):
    if dc == int(45):
        y=0.7
    if dc == int(37):
        y=0.6
    if dc == int(53):
        y=0.8
    if dc == int(60):
        y=0.87
    if dc == int(30):
        y=0.5
    return y
def esin(y):
    if ec == int(45):
        y=0.7
    if ec == int(37):
        y=0.6
    if ec == int(53):
        y=0.8
    if ec == int(60):
        y=0.87
    if ec == int(30):
        y=0.5
    return y    

ac = int(input("A Açı gir:",))
bc = int(input("B Açı gir:",))
cc = int(input("C Açı gir:",))
dc = int(input("D Açı gir:",))
ec = int(input("E Açı gir:",))


acc = acos(ac)
bcc = bcos(bc)
ccc = ccos(cc)
dcc = dcos(dc)
ecc = ecos(ec)

ass = asin(ac)
bss = bsin(bc)
css = csin(cc)
dss = dsin(dc)
ess = esin(ec)

ax = int(input("ax değeri gir:",))
bx = int(input("bx değeri gir:",))
cx = int(input("cx değeri gir:",))
dx = int(input("dx değeri gir:",))
ex = int(input("ex değeri gir:",))
ay = int(input("ay değeri gir:",))
by = int(input("by değeri gir:",))
cy = int(input("cy değeri gir:",))
dy = int(input("dy değeri gir:",))
ey = int(input("ey değeri gir:",))

Ax = ax*acc
Bx = bx*bcc
Cx = cx*ccc
Dx = dx*dcc
Ex = ex*ecc

Ay = ay*ass
By = by*bss
Cy = cy*css
Dy = dy*dss
Ey = ey*ess

Rx = Ax+Bx+Cx+Dx+Ex
Ry = Ay+By+Cy+Dy+Ey
RDY= Ry/Rx

T  = Ry/Rx
print("Ax Newton değeri :",Ax,"   Bx Newton değeri :",Bx,"  Cx Newton değeri :",Cx,"   Dx Newton değeri :",Dx,
    "   Ex Newton değeri :",Ex)
print("Rx değeri :",Rx,"Newton")
print("Ay Newton değeri :",Ay,"   By Newton değeri :",By,"  Cy Newton değeri :",Cy,"   Dy Newton değeri :",Dy,
    "   Ey Newton değeri :",Ey)
print("Ry değeri :",Ry,"Newton")
print("R değeri :",math.sqrt((Rx**2)+(Ry**2)))
print("Tanjant :",Ry/Rx)
if RDY > 0:
    RDY1 = RDY * 100
    RDY2 = RDY1 // 10 ** (int(math.log(RDY1, 10)) - 2 + 1)
    RDY3 = RDY2 / 100
    print("Tanjant Delta :",math.atan(RDY3)*180/math.pi)



##import math
##a = math.cos(math.radians(45)) #Cosinüs 45 gösterir
##b = math.radians(45) # 45 Derecenin radyanını alır
##c = math.degrees(45) # 45 Derece açı
##d = round(math.cos(math.radians(45))) #Cosinüs 45 yuvarlamasını gösterir
##e = math.cos(45) #Radyan 45 gösterir
##f = math.cos(math.pi / 4) #Cosinüs 45 gösterir
##print("a:",a,"b:",b,"c:",c,"d:",d,"e:",e,"f:",f)