read Source
read Destination
read Time
`$Time * * * * .$Home/Documentation/backup.sh >> $Home/tmp/out 2>&1`
LOG_FILE=`touch ./creation.log`
for f in `find $Source -type f`
  do
    fileName=$Destination"/"`basename $f`
    echo $fileName
    echo "$fileName"
    if [ -f $fileName ]
      then
      modifiedDate=`stat -c %y $f`
      modifiedDataDest=`stat -c %y $fileName`
      if [[ $modifiedDate > $modifiedDataDest ]] 
        then 
        `cp -a $f $Destination`
        echo "$f Backup done on `date`" >>LOG_FILE
      fi
    else
      `cp -a $f $Destination`
      echo "$f Backup done on `date`" >>LOG_FILE 
    fi
  done
