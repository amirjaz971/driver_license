import math




def round_up(num):
    if num>math.floor(num)+0.00000000000000001:
        return math.floor(num)+1
    else:
        return num





names=[]
name=input('enter your name: ')
names.append(name)
counter=0
name_index=0
other_name=''
other_names=input('enter the other names: ')

for i in other_names:
    counter+=1
    if i==' ':
       names.append(other_name.lower())
       other_name=''
    elif counter==len(other_names):
        other_name+=i
        names.append(other_name.lower())

    else:
        other_name+=i

names.sort()
print(names)
agent_num=int(input('enter the number of the agents:'))

for i in names:
    name_index+=1
    if i==name:
        break

if agent_num>=name_index:
    time=20
elif agent_num<name_index:
    time=round_up(name_index/agent_num)*20
    

print(f'it will take {time} minutes to get your license.')    




