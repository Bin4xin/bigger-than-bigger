#!/bin/bash
# user Auth

if [ $# != 2 ] ; then
   echo "USAGE: $0 username password"
   echo " e.g.: $0 root 111111"
   exit 1;
fi;

uname=`echo $1 | awk -F "" '{for(i=1;i<=NF;i++){if ($i ~ /[a-zA-Z0-9_]/) {str=$i;str1=(str1 str)}}print str1}'`
if [ a"$uname"b != a"$1"b ]; then
   echo the user $1 format is illegal
   echo error:1
   exit 1;
fi

#encrypt=`grep "^ENCRYPT_METHOD" /etc/login.defs | sed 's/ENCRYPT_METHOD//g;s/ //g'`
encrypt=$(passwd -S root | sed -rn 's/.* (\w+) crypt.*/\1/p')
passwd=$2
passwd_shadow=`grep ^$1: /etc/shadow | cut -d ":" -f2`

if [ ! $passwd_shadow ]; then
   echo the user $1 does not exist
   echo error:1
   exit 1;
fi


if [ "$encrypt" == "SHA512" ]
then
	salt=`grep ^$1: /etc/shadow | cut -d "\$" -f3`
	passwd_t=$(python -c "from crypt import crypt;print crypt('$passwd','\$6\$$salt')")
elif [ "$encrypt" == "DES" ]
then
	salt=`grep ^$1: /etc/shadow | cut -d ":" -f 2 | cut -d "/" -f 1`
	passwd_t=$(python -c "from crypt import crypt;print crypt('$passwd','$salt')")
else
	salt=`grep ^$1: /etc/shadow | cut -d "\$" -f3`
	passwd_t=$(python -c "from crypt import crypt;print crypt('$passwd','\$1\$$salt')")
fi

if [ "$passwd_shadow" == "$passwd_t" ]; then
	echo true
else
	echo "incorrect password"
   echo "error:2"
   exit 2;
fi
