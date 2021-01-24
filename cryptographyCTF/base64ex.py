from itertools import permutations, combinations
import base64
baselist = ['wNT', 'jgw', 'ODM', 'gxM']

for i in permutations(baselist, 4):
    string = ""
    for combi in i:
        string += combi
    string += "Mw=="
    data = base64.b64decode(string)
    print(data)
