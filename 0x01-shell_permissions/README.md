#!/bin/bash
su -give temporary access to superuser's privileges
whoami -prints the effective username of the current user
groups-  prints all the groups the current user is part of
chown betty hello -changes the owner of the file hello to the user betty
touch-to create and empty file
chmod u+x hello adds execute permission to the owner of the file hello
chmod 774- adds execute permission to the owner and the group owner, and read permission to other user
