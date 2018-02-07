read Source
read Destination
read Time
LOG_FILE=`touch ./creation.log`
while true
do
  filesS=(`ls $Source`)
  for f in ${filesS[*]}
  do
    fileSrc=$Source"/"$f
    fileName=$Destination"/"`basename $f`
    echo $f
    echo $fileSrc
    echo $fileName
    if [ -f $fileName ]
      then
      modifiedDate=`stat -c %y $fileSrc`
      modifiedDataDest=`stat -c %y $fileName`
      if [[ $modifiedDate > $modifiedDataDest ]] 
        then 
        `cp -a $fileSrc $Destination`
        echo "$f Backup done on `date`" >>LOG_FILE
      fi
    else
      `cp -a $fileSrc $Destination`
      echo "$f Backup done on `date`" >>LOG_FILE 
    fi
  done
  sleep $Time
done
