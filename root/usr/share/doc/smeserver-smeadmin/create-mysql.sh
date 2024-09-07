#!/bin/sh

#-----------------------------------
#Script to create :
#-Database
#-mysql user
#-tables
#Executed after rpm installation 
#-----------------------------------

#database creation
mysqladmin create smeadmin 2>err 
if [ $? -ne 0 ] 
then 
    echo -n "Error in the creation of the database : " 
    cat err
else
    echo -e "Database creation :\t\t\t[OK]"
fi

PASS=$(/sbin/e-smith/db configuration getprop smeadmind DbPassword)

#user creation
mysql -e " grant all privileges on smeadmin.* \
    to 'smeadmin'@'localhost' \
    identified by '$PASS' " 2>err

if [ $? -ne 0 ]
then
    echo -n "Error in the creation of mysql user : "
    cat err
else
    echo -e "Creation of mysql user :\t\t[OK]"
fi

#table creation 
mysql smeadmin < /usr/share/doc/smeserver-smeadmin/tables.sql 2>err
if [ $? -ne 0 ]
then
    echo -n "Error in the creation of the tables : "
    cat err
else
    echo -e "Creation of tables :\t\t\t[OK]"
fi

rm -f err

#validation des modifications
mysqladmin flush-privileges
