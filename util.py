__author__ = 'mclancy'
# ***********************************************************************************************************************
from cStringIO import StringIO

import numpy as np


class StringBuilder:
    _file_str = None

    def __init__(self):
        self._file_str = StringIO()

    def Append(self, strg):
        self._file_str.write(strg)

    def __str__(self):
        return self._file_str.getvalue()

# region Dictionary containing the k/v pairs for the resp group
global stdgrp
# noinspection PyRedeclaration
stdgrp = {'BEG': 'BEGIN FND_RESPONSIBILITY ', 'L01': '  RESPONSIBILITY_NAME = ', 'L02': '  OWNER = "ORACLE12.1.3"',
          'L03': '  LAST_UPDATE_DATE = "2000/04/25"',
          'L04': '  DATA_GROUP_APP_SHORT_NAME = ', 'L05': '  DATA_GROUP_NAME = ', 'L06': '  MENU_NAME = ',
          'L07': '  START_DATE = "2014/01/01"', 'L08': '  END_DATE = "*NULL*"', 'L09': '  DESCRIPTION = ', 'L10': '  GROUP_APP_SHORT_NAME = ',
          'L11': '  REQUEST_GROUP_NAME = ','L12': '  VERSION = ', 'L13': '  WEB_HOST_NAME = "*NULL*"',
          'L14': '  WEB_AGENT_NAME = "*NULL*"', 'END': 'END FND_RESPONSIBILITY', 'N': '\n'}
# endregion

def printall():

    print '%s' % (stdgrp['BG'])  + '%s' %  'this is a test'
    print '%s' % (stdgrp['L01']) + '%s' % 'this is where resp name goes'
    print '%s' % (stdgrp['L02'])
    print '%s' % (stdgrp['L03'])
    print '%s' % (stdgrp['L04']) +'%s' % 'Datagroup APP short name goes here'
    print '%s' % (stdgrp['L05']) +'%s' % 'Datagroup name goes here'
    print '%s' % (stdgrp['L06']) +'%s' % 'Menu name goes here'
    print '%s' % (stdgrp['L07'])
    print '%s' % (stdgrp['L08'])
    print '%s' % (stdgrp['L09']) +'%s' % 'Description goes here'
    print '%s' % (stdgrp['L10']) +'%s' % 'Group App short name'
    print '%s' % (stdgrp['L11']) +'%s' % 'Group App short name'
    print '%s' % (stdgrp['L12'])
    print '%s' % (stdgrp['L13'])
    print '%s' % (stdgrp['L14']) + '\n'
    print '%s' % (stdgrp['ED'])  + '\n'

# region Layout for the resp group items to be placed in the file
def runlister(resplist,hdrstr,filout):
    wrst=''
    str1=''
    prfx = 'United States'
    for item in resplist:
        lineBEG ='%s' % (stdgrp['BEG']) + '%s "%s-%s" ' % (item['DGSNAME'],prfx, item['BEGINTITLE']) + '\n'
        line01 = '%s' % (stdgrp['L01']) + '"%s-%s"' % (prfx,item['RESPNAME']) + '\n'
        line02 = '%s' % (stdgrp['L02']) + '\n'
        line03 = '%s' % (stdgrp['L03']) + '\n'
        line04 = '%s' % (stdgrp['L04']) + '%s' % item['DGSNAME'] + '\n'
        line05 = '%s' % (stdgrp['L05']) + '%s' % item['DGNAME'] + '\n'
        line06 = '%s' % (stdgrp['L06']) + '%s' % item['MNNAME'] + '\n'
        line07 = '%s' % (stdgrp['L07']) + '\n'
        line08 = '%s' % (stdgrp['L08']) + '\n'
        line09 = '%s' % (stdgrp['L09']) + '"%s-%s"' % (prfx,item['DESC']) + '\n'
        line10 = '%s' % (stdgrp['L10']) + '"%s"' % item['GASNAME'] + '\n'
        line11 = '%s' % (stdgrp['L11']) + '"%s"' % item['REQGNAME'] + '\n'
        line12 = '%s' % (stdgrp['L12']) + '%s' % item['VERSION'] + '\n'
        line13 = '%s' % (stdgrp['L13']) + '\n'
        line14 = '%s' % (stdgrp['L14']) + '\n' + '\n'
        lineEND = '%s' % (stdgrp['END']) + '\n'+ '\n'
            #This is the string aggregator that eventually combines with the header to produce the ouput file
        stragre = [lineBEG,line01, line02, line03, line04, line05, line06, line07, line08, line09, line10, line11,
                   line12, line13, line14, lineEND]

        for i in stragre:
            str1 = str1 +i
    wrstr = hdrstr+str1
    filout.write(wrstr)
    print wrstr


# endregion

#NumPy example *********************************************************************************************************
'''RESPID, BEGINTITLE, RESPNAME, DGSNAME, DGNAME, MNNAME, DESC, GASNAME, REQGNAME = np.loadtxt(
    '/Users/mclancy/Desktop/ldt/resplist.csv', delimiter=',', unpack=True, dtype=str)

for J in range(len(RESPID)):
    print RESPID[J], BEGINTITLE[J], RESPNAME[J], DGSNAME[J], DGNAME[J], MNNAME[J], DESC[J], GASNAME[J], REQGNAME[J]'''

'''
# A test adding the csv dictionary to a list
print 'Heres the test'
tooli =[]
for kl in resplist:
    tooli.append((kl['DGSNAME'], kl['REQGNAME'],kl['RESPID'],kl['MNNAME']))
print type(tooli)'''