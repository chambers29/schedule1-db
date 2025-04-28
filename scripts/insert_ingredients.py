with open(r'data\ingredients.txt','r') as file:
    text = file.read()

sql_namelist = []
sql_pricelist = []
sql_effectlist = []

text = text.split('\n\n')
for i in text:
    i = i.strip()

    name = i.split('\t')[0]
    cost = i.split('\t')[1]
    effect = i.split('\t')[4]

    sql_namelist.append(name)
    sql_pricelist.append(cost)
    sql_effectlist.append(effect)

print(f'INSERT INTO ingredients \nVALUES')
for idx, ingredient in enumerate(sql_namelist, start=1):
    last_line = idx == len(sql_namelist)
    if last_line:
        end_symbol = ';'
    else: end_symbol = ','
    print(f'\t({idx}, \'{ingredient}\', {sql_pricelist[idx-1][1:]}, (SELECT effect_id FROM effects WHERE name=\'{sql_effectlist[idx-1]}\')){end_symbol}')