effect_id_map = {
    "Anti-Gravity"  :	1,
    "Athletic"      :   2,
    "Balding"       :   3,
    "Bright-Eyed"   :	4,
    "Calming"       :	5,
    "Calorie-Dense" :	6,
    "Cyclopean" 	:   7,
    "Disorienting"  :	8,
    "Electrifying"  :	9,
    "Energizing"    :	10,
    "Euphoric"      :	11,
    "Explosive"	    :   12,
    "Focused"	    :   13,
    "Foggy"	        :   14,
    "Gingeritis"    :	15,
    "Glowing"	    :   16,
    "Jennerising"   :	17,
    "Laxative"	    :   18,
    "Lethal"	    :   19,
    "Long Faced"	:   20,
    "Munchies"      :	21,
    "Paranoia"	    :   22,
    "Refreshing"    :	23,
    "Schizophrenic" :	24,
    "Sedating"      :	25,
    "Seizure-Inducing":	26,
    "Shrinking"     :	27,
    "Slippery"      :	28,
    "Smelly"        :	29,
    "Sneaky"        :	30,
    "Spicy"         :	31,
    "Thought-Provoking":32,
    "Toxic"         :   33,
    "Tropic Thunder":	34,
    "Zombifying"    :	35
}

#copied from:
# SELECT
# 	npc_id
# FROM npcs
# WHERE
# 	is_customer = TRUE
customers = """1	"Austin Steiner"
2	"Beth Penn"
3	"Chloe Bowers"
4	"Donna Martin"
5	"Geraldine Poon"
6	"Jessi Waters"
7	"Kathy Henderson"
8	"Kyle Cooley"
9	"Ludwig Meyer"
10	"Mick Lubbin"
11	"Mrs. Ming"
12	"Peggy Myers"
13	"Peter File"
14	"Sam Thompson"
17	"Trent Sherman"
18	"Meg Cooley"
19	"Joyce Ball"
20	"Keith Wagner"
21	"Doris Lubbin"
22	"Jerry Montero"
23	"Kim Delaney"
24	"Charles Rowland"
25	"Dean Webster"
26	"George Greene"
29	"Elizabeth Homley"
30	"Jennifer Rivera"
31	"Lucy Pennington"
32	"Philip Wentworth"
33	"Kevin Oakley"
34	"Randy Caulfield"
35	"Louis Fourier"
36	"Eugene Buckley"
37	"Jeff Gilmore"
38	"Greg Figgle"
40	"Anna Chesterfield"
41	"Cranky Frank"
42	"Genghis Barn"
43	"Javier Perez"
44	"Lisa Gardener"
45	"Melissa Wood"
46	"Marco Barone"
47	"Billy Kramer"
48	"Mac Cooper"
51	"Chris Sullivan"
52	"Alison Knight"
53	"Karen Kennedy"
54	"Carl Bundy"
55	"Jeremy Wilkinson"
56	"Hank Stevenson"
57	"Jack Knight"
58	"Harold Colt"
59	"Jackie Stevenson"
60	"Dennis Kennedy"
62	"Lily Turner"
63	"Fiona Hancock"
64	"Walter Cussler"
65	"Jen Heard"
66	"Ray Hoffman"
67	"Pearl Moore"
68	"Herbert Bleuball"
69	"Tobas Wentworth"
70	"Michael Boog"
"""
customers = [(customers.replace('\n',','))]
customers = customers[0].split(',')
person_id = {}
for customer in customers:
    if customer == '':
        continue
    customer = customer.replace('"','')
    customer = customer.split('\t')
    person_id[customer[1]] = customer[0]
# print(person_id)

with open(r'data\npcs.txt') as file:
    file.readline()
    text = []

    for line in file.readlines():
        line = line.strip()
        if line == '':
            continue
        line = line.split('\t')
        text.append(line)

person_and_effect = []
for person in text:
    if len(person[2]) > 1:
        person_and_effect.append([person[0],person[2]])

paedict = {}
for pae in person_and_effect:
    paedict[pae[0]] = pae[1].split(',')
# print(paedict)

npc_effect = {}
for npc in paedict:
    npc_effect[person_id[npc]] = []
    for effect in paedict[npc]:
        effect = effect.strip()
        npc_effect[person_id[npc]].append(effect_id_map[effect])

print('INSERT INTO effects_npc\nVALUES')
for e in npc_effect:
    for v in npc_effect[e]:
        if e == list(npc_effect)[-1] and v == list(npc_effect.values())[-1][-1]:
            end = ';'
        else: end = ','
        print(f'\t({v},{e}){end}')