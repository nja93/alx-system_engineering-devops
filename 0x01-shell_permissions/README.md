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
chmod +R +111 */ OR chmod -R +X  -script that adds execute permission to all subdirectories of the current directory for the owner, the group owner and all other users. Regular files should not be changed
mkdir -m 751 my_dir -creates a directory called my_dir with permissions 751 in the working directory
chgrp school hello script that changes the group owner to school for the file hello
chown vincent:staff * -script that changes the owner to vincent and the group owner to staff for all the files and directories in the working directory.chown  --from=guillaume betty hello -script that changes the owner of the file hello to betty only if it is owned by the user guillaume
chown -h vincent:staff _hello- script that changes the owner and the group owner of _hello to vincent and staff respectively.
telnet towel.blinkenlights.nl - script that will play the StarWars IV episode in the terminal. 
