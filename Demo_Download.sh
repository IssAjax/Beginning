#!/bin/bash -x

#This will install the most current demo
exclude=$(edge.exclude)
logfile=$(logfile.txt)

#Move files to the tmp folder so that they can be used again once the reinstallation is finished 

mv /etc/$exclude /tmp/
mv /opt/microlite/backupedge/lists/$logfile /tmp/
cd /tmp/

#Find what version the server is so we know what version of backup edge to download 

i=$(gawk '{print $4}' /etc/redhat-release | cut -b -1)
echo $i

if [[ i -ge 8 ]]; then
    wget -O demox40_64.elf https://www.microlite.com/ftp/demos/current/edgelx40_64/edgelx40_64.elf
elif [[ i -ge 7 && i -lt 8 ]]; then
    wget -O demox30_64.elf https://www.microlite.com/ftp/demos/current/edgelx30_64/edgelx30_64.elf
elif [[ i -le 6 ]]; then
    wget -O demox64.elf https://www.microlite.com/ftp/demos/current/edgelx64/edgelx64.elf
fi

# find the newly installed demo, change the permissions, and run the installer 

p=$(find ./ -name 'demo*' | grep -i '.elf')

echo $p
chmod 755 $p

$p

# Find the logfile and edge.exclude file and move them back to where they belong 

if [ -f '/tmp/$exclude' -a -f '/tmp/$logfile']; then 
    echo "$exclude exists, Moving file now"
    echo "$logfile exists, Moving file now"
    mv /tmp/$exclude /etc/$exclude && mv /tmp/$logfile /opt/microlite/backupedge/lists/$logfile
elif [ ! -f '/tmp/$exclude' -a ! -f '/tmp/$logfile' ]; then
    echo "$exclude Does not exist sorry"
    echo "$logfile Does not exist sorry"
fi 

#see if the flash drive is currently attached to the vm 

drive=$(fdisk -l | grep -i 'xvdh')

$drive 

if [[ $? != 0]]; then 
    echo "This Command Has Failed"
elif [[ $drive ]]; then 
    echo "$drive"
else
    echo "No Drive Attached To VM"
fi 
