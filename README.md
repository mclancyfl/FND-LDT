FND-LDT
=======

Python script that takes a csv with Resp info and writes out a LDT file that can be loaded via FNDLOAD.

The ldt.db file is a sqlite db file and is not used.

Check the cvs file in the dat directory for any new resps to be formed.

Run readin.py and choose option one. Enter the Prefix and then find the output file ldtout.ldt in the dat directory.

move the file to the FND_TOP on the Oracle R12.

Run the following command FNDLOAD apps/biggie O Y UPLOAD $FND_TOP/patch/115/import/afscursp.lct ldtout.ldt 

Check the logs for errors and then check the newly created Resps in Oracle.
