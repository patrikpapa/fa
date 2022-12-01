import random

file=open('fa.txt','w')
fakit=[]
dátum=20
for i in range(0,31):
    fakit.append(random.randrange(50,101))
print('')
legnagyobb=0
legnagyobb=fakit[0]
for nap in fakit:
    if nap > legnagyobb:
        legnagyobb=nap
print(f'{legnagyobb}m3 volt a legnagyobb t!')
file.write(f'{legnagyobb}m3 volt a legnagyobb t!\n')
legkisebb=0
legkisebb=fakit[0]
for nap in fakit:
    if nap < legkisebb:
        legkisebb=nap
print(f'{legkisebb}m3 volt a legkevesebb t!')
file.write(f'{legkisebb}m3 volt a legkevesebb t!\n')
print('')
alkalom = 0
for i in range(0,len(fakit)):
    if fakit[i] > 82:
        alkalom+=1
print(f'{alkalom} alkalommal volt több a napi termelésmint 82m3!')
print(f"{dátum}. -án : {fakit[dátum+1]}m3 fát termeltek!")
file.write(f'{dátum}. -án : {fakit[dátum+1]}m3 fát termeltek!\n')
átlag = 0
for i in range(0,len(fakit)):
    átlag = átlag+fakit[i]
átlag = átlag/len(fakit)
print(f'{átlag} volt az átlag fa termelés!')
file.write(f'{átlag} volt az átlag fa termelés!\n')
