__author__ = 'mclancy'
import datetime


#Variables**********************************
now = datetime.datetime.now()
nli = []
clean = []
keydict = {}
ife = now.minute
army = now.strftime("%Y-%m-%d-%H-%M-%S")
cnt = 0
cnt2 =0
grp1 =[[],[]]
filename = 'out-%s.csv' % army
filename2 = 'out2-%s.dat' % army
#********************************************

#Get the resp file from disk that was exported from Oracle
f = open('/Users/mclancy/Desktop/ldt/all_resp.ldt','r')

#Now we get rid of spaces and serialize the stuff into \
# a two dim list called grp1
for i in f:
    if len(i) > 3:
        if 'BEGIN FND_' in i:
            grp1.append([cnt,i])
        if 'BEGIN FND_' not in i:
            grp1.append([cnt,i])
        if 'END FND_' in i:
            cnt += 1
print cnt

out = open('/Users/mclancy/Desktop/ldt/'+ filename,'w')
# take the line in group 1 and write it to a file.?
for i in grp1:
    if i:
        out.write(str(i[0]) + ',' + str(i[1]))
out.close()
#Now we get the keys from Group one and put them in nli that \
#we turn into a set called set1
for i in grp1:
    if  i:
        nli.append(i[0])
set1 = set(nli)

#Clean up the import and get rid of empties
for rec in grp1:
    if rec:  # get only real records and not empties
        clean.append(rec)  # put them in this clean list

#Create a Set used in aligning the lines in the ldt to a dict \
#using set1 as the key and the line as the value
#We initialize the keydct with the keys so we can assign the \
#values in the loop below
for i in set1:
    keydict[i]=[]
#Add the values to keydict via append
for c in clean:
    keydict[c[0]].append(c[1])
#Push the values data to file for processing in excel
out2 = open('/Users/mclancy/Desktop/ldt/'+ filename2,'w')
for val in keydict:
    out2.write(str(keydict[val])+'\n')
out2.close()