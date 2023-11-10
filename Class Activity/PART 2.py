def histogram(s):
    d=dict()
    for c in s:
        if c not in d:
            d[c]=1
        else:
            d[c]+=1
    return d
h=histogram('brontosaurus')

h.get('c',0)
print(h)