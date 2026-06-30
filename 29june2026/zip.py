#zip  convert normal data  into zip.
#1]
names=["alice","bob"]
scores=[90,45]
for name,score in zip(names,scores):
    print(f"{name} : {score}")

#2] unzip which convert zipped data into normal form.
names=["alice","bob"]
scores=[90,45]
zipped=zip(names,scores)
unzipped_names,unzipped_scores=zip(*zipped)
print(unzipped_names)
print(unzipped_scores)

# zip longest ( in this itertools library is mandatory)

from itertools import zip_longest
list1=[1,2,3,4,5]
list2=["a","b"]
for num ,letter in zip_longest(list1,list2,fillvalue=None):
    print(f"number:{num} , letter:{letter}")