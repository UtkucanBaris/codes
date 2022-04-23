############################################## 66 STEP ################
def love_meet(bob, alice):
    alice1=[]
    for i in alice:
        if i in bob:
            alice1.append(i)
    bob1=set(sorted(alice1))
    return bob1
def affair_meet(bob, alice, silvester):
    aliceandsilvester=[]
    silvester1=[]
    for i in alice:
        if i not in bob:
            aliceandsilvester.append(i)
    for i in aliceandsilvester:
        if i in silvester:
            silvester1.append(i)
    alice1=set(sorted(silvester1))
    return alice1
if __name__ == "__main__":
    assert love_meet(
        ["IV", "III", "II", "XX", "II", "XX"],
        ["II", "IV", "II", "XIX", "XV", "IV", "II"],
    ) == {"II", "IV"}

    assert affair_meet(
        ["IV", "III", "II", "XX", "II", "XX"],
        ["II", "IV", "II", "XIX", "XV", "IV", "II"],
        ["XVIII", "XIX", "III", "I", "III", "XVIII"],
    ) == {"XIX"}
#############################    145 Step      ###########################
def love_meet(bob, alice):
    bobandalice = []
    for i in bob:
        for y in alice:
            if i == y and i not in bobandalice:
                bobandalice.append(i)
    bob1=set(sorted(bobandalice))
    return bob1
def affair_meet(bob, alice, silvester):
    aliceandsilvester=[]
    silvester1=[]
    for i in alice:
        if i not in bob:
            aliceandsilvester.append(i)
    for i in aliceandsilvester:
        if i in silvester:
            silvester1.append(i)
    alice1=set(sorted(silvester1))
    return alice1
if __name__ == "__main__":
    assert love_meet(
        ["IV", "III", "II", "XX", "II", "XX"],
        ["II", "IV", "II", "XIX", "XV", "IV", "II"],
    ) == {"II", "IV"}

    assert affair_meet(
        ["IV", "III", "II", "XX", "II", "XX"],
        ["II", "IV", "II", "XIX", "XV", "IV", "II"],
        ["XVIII", "XIX", "III", "I", "III", "XVIII"],
    ) == {"XIX"}

################################################ 20 step ###########################################
def love_meet(bob, alice):
    ejerc1 = set(alice) & set(bob)
    return ejerc1


def affair_meet(bob, alice, silvester):
    ejerc2 = set(alice) & set(silvester) - set(bob)
    return ejerc2 



if __name__ == "__main__":
    assert love_meet(
        ["IV", "III", "II", "XX", "II", "XX"],
        ["II", "IV", "II", "XIX", "XV", "IV", "II"],
    ) == {"II", "IV"}

    assert affair_meet(
        ["IV", "III", "II", "XX", "II", "XX"],
        ["II", "IV", "II", "XIX", "XV", "IV", "II"],
        ["XVIII", "XIX", "III", "I", "III", "XVIII"],
    ) == {"XIX"}