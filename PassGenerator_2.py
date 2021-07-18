import random
import string

passwordLen = 8
num = 2
spl =2
pun = 2
ucase = 2
lcase = 2

numrepo=string.digits
splrepo=string.punctuation
ignoreSpl = [',','.','[',']','{','}','(',')','/']
for i in range(len(ignoreSpl)):
    splrepo=splrepo.replace(ignoreSpl[i],'')

splrepo=splrepo.replace('.','')
splrepo=splrepo.replace('.','')
splrepo=splrepo.replace('.','')
ucaserepo=string.ascii_lowercase
lcaserepo=string.ascii_uppercase
# print(lcaserepo)
# print(ucaserepo)
print(splrepo)
# print(numrepo)

numTemp = random.sample(numrepo, num)
splTemp = random.sample(splrepo, num)
ucaseTemp = random.sample(ucaserepo, num)
lcaseTemp = random.sample(lcaserepo, num)

tempPass=numTemp+splTemp+ucaseTemp+lcaseTemp
password = ''.join(tempPass)

print(password)