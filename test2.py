L1 = ['AdmIn','anny','LUCY','sandY','wILl']
def normalize(name):
    return name[0].upper() + name[1:].lower()
L2=list(map(normalize,L1))
print(L2)