#!/bin/bash -x
#
# Purpose: Re-run backups after hours 
#
# Written By: Dantae Hopson 12/14/2022
#

# Check to see if disk is attached, the script will only continue if the result passes  

fdisk -l | grep /dev/loop0

result=$?

if [ $result -eq 0 ]; then 
    echo "Drive exists Continuing"
     
else
    echo "Drive is not inserted. Exiting script"
    exit 1 
fi 

# See if partition is mounted, if the partition does not exist it will mount it 
df -h | grep /dev/loop0


result=$?

if [ $result -eq 0 ]; then 
    echo "Partition is connected Continuing"
     
else
    echo "Partition is not mounted Mounting"
    mount /tmp/flash / 
fi 

# See if the backup process is running, if it is the script will exit 
sclock=/opt/microlite/backupedge/lists/simple_job/schedule.lck
lock=/opt/microlite/backupedge/system/mnt/af0/fsp0/lck
ps -el | grep edge


result=$?

if [ $result -eq 0 ]; then
    echo "BackupEdge is writing data"
    echo "Script now exiting"
    exit 1 
else
    echo "BackupEdge is not writing data..."

    # Delete the lock files if any so the backup can run again 
    if [ -f $sclock ]; then
        echo "Removing $sclock"
        rm -f $sclock

    else
        echo "$sclock does not exist"

    fi


    if [ -f $lock ]; then
        echo "Removing $lock"
        rm -f $lock

    else
        echo "/opt/microlite/backupedge/system/mnt/af0/fsp0/lck does not exist"

    fi

    # Run the backup 
    nohup /usr/lib/edge/bin/edge.action -c $hostname:schent/simple_job $hostname:action/simple_job &
fi

ps -el | grep edge 