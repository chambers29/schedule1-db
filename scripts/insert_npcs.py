with open(r'data\npcs.txt') as file:
    file.readline()
    npcs = file.readlines()

print('INSERT INTO npcs\nVALUES')

area_id = 1
idx = 1

for npc in npcs:

    npc = npc.strip()
    npc = npc.split('\t')

    if len(npc) == 1:
        area_id += 1
        npc.pop()
        continue

    if npc[-1] == 'Customer':
        is_customer = 'TRUE'
        role = '1'
    elif npc[-1] == 'Dealer':
        is_customer = 'FALSE'
        role = '2'
    else:
        is_customer = 'FALSE'
        role = '3'
    if '\t'.join(npc) == npcs[-1]:
        end_symbol = ';'
    else: end_symbol = ','
    print(f"\t({idx},'{npc[0]}',{area_id},{is_customer},{role}){end_symbol}")
    idx += 1