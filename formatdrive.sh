#!/bin/bash -x

vg=450G

#formatting /dev/xvdb

mkdir -p /data 
read -p "formatting drive press ENTER to continue"

(
echo n
echo p
echo 1
echo
echo
echo t
echo 8e
echo w

) | fdisk /dev/xvdb

# Creating  a virtual group and logical group with {x} amount of space

read -p "creating volume group and logical volume, volume size currently = $vg is this correct? CTRL+C if is not"
vgcreate VolGroup01 /dev/xvdb1
wait
lvcreate --size ${vg} -n data VolGroup01


# Formatting the file system and mounting the drive

mkfs.ext4 -F /dev/mapper/VolGroup01-data
read -p "mounting the drive ENTER to continue"
mount /dev/mapper/VolGroup01-data /data

# Appending the information to fstab file

echo "/dev/mapper/VolGroup01-data       /data   ext4    defaults        1 2" >> /etc/fstab
read -p "FSTAB HAS BEEN UPDATED"

# Reloading daemon and checking the mounted drives
systemctl daemon-reload

df -lah

read -p "This has now been completed press enter when ready for the next part"
read -p " Make sure that you have a v4 or v3 setup on the VM"


v4=$(find /tmp -print | egrep 'V4'\|'V3')

unzip $v4

v3=$(find /tmp -print | egrep 'V4'\|'V3')

cd $v3
echo " Please run ** bash ./setup.sh county state type ** "
