__author__ = 'mclancy'
import csv
import os
import kivy
from kivy.app import *
from util import *



#***********************************************************************************************************************

#***********************************************************************************************************************

'''
This program takes writes ldt files for responsibilities. It pulls in the header of the ldt file from disk
it then details out the ldt file using lists
'''

#***********************Variables Definition****************************************************************************
path   = 'dat/'
hdrfil = 'hdr-ldt.dat'
outfil = 'ldtout.ldt'
sb     = StringBuilder()
str1=''
filout = open(path+outfil,'w')
kin= {}
#***********************Read Header into String*************************************************************************
hdrin = open(path+hdrfil,'r')
hdrstr = hdrin.read()
#***********************Create the Database*-Un-Comment to use**********************************************************
'''con = None
con = lite.connect('ldt.db')
cur = con.cursor()
with con:
    cur = con.cursor()
    cur.execute("CREATE TABLE RESPS(Id INT, BEGINTITLE TEXT, RESPNAME TEXT, DGSNAME TEXT, DGNAME TEXT,\
                MNNAME TEXT,DESC TEXT,GASNAME TEXT, TEXT,REQGNAME)")'''
#***********************Load the csv of Resps to the database***********************************************************
#open the csv file and load to a list

respcsv = open(path+'resplist.csv','r')
resplist = csv.DictReader(respcsv,dialect='excel')

#runlister(resplist,hdrstr,filout)


def main():
#    class wisi(App):
#        pass
#    wisi().run()
    loop = 1
    while loop==1:
        os.system('clear')
        print 'This is a Menu'
        print '1: To Run Resp Creation'
        print '2: To Print jibberish'
        print '3: To Quit               '
        choice = input('Please choose: ')
        choice = int(choice)
        if choice == 1:
            print "Enter the prefix for the Responsibilities"
	    prfx = raw_input()
            runlister(resplist,hdrstr,filout,prfx)
            print 'Press enter to continue back to menu'
            raw_input()
        if choice == 2:
            print 'this is a reset'*10
        if choice == 3:
            break

    print 'that is is bye bye'

if __name__ == '__main__':
    main()
#***********************************************************************************************************************
