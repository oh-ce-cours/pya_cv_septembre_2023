import pprint

caras='fsml fjm slf xmlqj gfmjq mlqks jdnfq ybsd pofza'
par_lettre={}
for cara in caras:
    if cara not in par_lettre:
        par_lettre[cara]=0
    par_lettre[cara]=par_lettre[cara]+1
pprint.pprint(par_lettre)