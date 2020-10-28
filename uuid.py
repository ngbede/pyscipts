import numpy as np

# format
# Sample uuid: 123e4567-e89b-12d3-a456-426614174000
#     xxxxxxxx-xxxx-Mxxx-Nxxx-xxxxxxxxxxxx
def uuid_generator():
    alphabets = ["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    id_lst = []
    uuid = ""
    for i in range(0,36): # length of uuid
        if (i == 0):
            idx = np.random.randint(0,10)
            id_lst.append(str(idx))
        elif (i == 8 or i == 13 or i == 18 or i == 23):
            id_lst.append("-")
        elif (i > 23):
            idx = np.random.randint(0,10)
            id_lst.append(str(idx))
        else:
            j = np.random.randint(2,6)
            if (j % 2 == 0):
                idx = np.random.randint(0,10)
                id_lst.append(str(idx))
            else:
                idx = np.random.randint(0,26)
                id_lst.append(alphabets[idx])
    uuid = uuid.join(id_lst)
    return uuid

# generate uuids with the function    
for i in range(0,20):
    print(uuid_generator())
