set1 = {1,2,3}
set2 = {2,4,6}
set3 = set1.union(set2)
print(set3)

set1 = {1,2,3}
set2 = {2,4,6}
set1.update(set2)
print(set1)

data_diri = {
"nama":"Reza",
"matpel":"DDP"}
data_diri["semester"] = 1
print(data_diri["nama"])
if('nama' in data_diri):
    print('nama ada di data_diri')

zoo = ('python', 'elephant', 'penguin')
print('Number of animals in the zoo is', len(zoo))
new_zoo = 'monkey', 'camel', zoo 
print('Number of cages in the new zoo is', len(new_zoo))
print('All animals in new zoo are', new_zoo)
print('Animals brought from old zoo are', new_zoo[2])
print('Last animal brought from old zoo is', new_zoo[2][2])
print('Number of animals in the new zoo is', len(new_zoo)-
1+len(new_zoo[2]))