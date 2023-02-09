#!/bin/bash
su -give temporary access to superuser's privileges
whoami -prints the effective username of the current user
groups-  prints all the groups the current user is part of
chown betty hello -changes the owner of the file hello to the user betty
touch-to create and empty file
chmod u+x hello adds execute permission to the owner of the file hello
chmod 754- adds execute permission to the owner and the group owner, and read permission to other user
chmod 751- adds execution permission to the owner, the group owner and the other users, to the file
chmod 007- Owner: no permission at all Group: no permission at all Other users: all the permissions
chmod 753- -rwxr-x-wx to the file hello
chmod --reference=olleh hello  -script that sets the mode of the file hello the same as olleh’s mode. 
