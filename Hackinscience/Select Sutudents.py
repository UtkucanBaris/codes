def select_student(students, threshold):
    d=dict()
    for i in students:
        if i[-1] > threshold and i not in B and i not in A:
            A.append(i)
        if i[-1] < threshold and i not in A and i not in B:
            B.append(i)
    C=sorted(A,key=lambda x:x[1],reverse=True)
    D=sorted(B,key=lambda x:x[1])
    d["Accepted"]=C
    d["Refused"] =D
    return d
D=[]
C=[]
A=[]
B=[]

# SONUNDAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA
if __name__ == "__main__":

    assert select_student(
        [
            ["Kermit Wade", 27],
            ["Hattie Schleusner", 67],
            ["Ben Ball", 5],
            ["William Lee", 2],
        ],
        20,
    ) == {
        "Accepted": [["Hattie Schleusner", 67], ["Kermit Wade", 27]],
        "Refused": [["William Lee", 2], ["Ben Ball", 5]],
    }