#nested dictonzry

dict = {
    'Aharbal' : {
    "name":"aharbal",
    "pincode":192231,
    "cell":121
    },

    'pahalgam' : {
        "name":'pahalgam',
        'pincode':12341,
        'cell':9596314004
    }
}
print(dict)

# another way
d1 = {
    1 : "malik tawkeer",
    2 : 192231,
    3 : "srinagar",
    4 : "kashmir university"
}
d2 = {
    1 : 'A',
    2 : 'B',
    3 : 'C'
}
d3 = {
    1 : 'ABC',
    2 : 'DEF',
    3 : 'GHI'
}

dic = {
    'd1' : d1,
    'd2' : d2,
    'd3' : d3
}

print(dic.items())

# fromkeys() return specified vals
#print(dic.fromkeys(0,'d2'))


for i in dic:
    print(dic.keys())
