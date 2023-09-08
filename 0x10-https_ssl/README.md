0x10. HTTPS SSL
DevOps
SysAdmin
Security
 By: Sylvain Kalache, co-founder at Holberton School
 Weight: 1
 Ongoing second chance project - started Sep 7, 2023 6:00 AM, must end by Sep 9, 2023 6:00 AM
 An auto review will be launched at the deadline
In a nutshell…
Auto QA review: 0.0/8 mandatory & 0.0/1 optional
Altogether:  0.0%
Mandatory: 0.0%
Optional: 0.0%
Calculation:  0.0% + (0.0% * 0.0%)  == 0.0%
Concepts
For this project, we expect you to look at these concepts:

DNS
Web stack debugging


Background Context
What happens when you don’t secure your website traffic?


Resources
Read or watch:

What is HTTPS?
What are the 2 main elements that SSL is providing
HAProxy SSL termination on Ubuntu16.04
SSL termination
Bash function
man or help:

awk
dig
Learning Objectives
At the end of this project, you are expected to be able to explain to anyone, without the help of Google:

General
What is HTTPS SSL 2 main roles
What is the purpose encrypting traffic
What SSL termination means
Requirements
General
Allowed editors: vi, vim, emacs
All your files will be interpreted on Ubuntu 16.04 LTS
All your files should end with a new line
A README.md file, at the root of the folder of the project, is mandatory
All your Bash script files must be executable
Your Bash script must pass Shellcheck (version 0.3.7) without any error
The first line of all your Bash scripts should be exactly #!/usr/bin/env bash
The second line of all your Bash scripts should be a comment explaining what is the script doing
# Script that configure an Nginx server redirect_me

# run bash script from task 1
./1-install_nginx_web_server

# 404 error display
echo "Ceci n'est pas une page" | sudo tee /etc/nginx/html/404.html

# create the error file
sudo mkdir /etc/nginx/html/

# configure the server
printf %s "server {
    listen 80;
    listen [::]:80 default_server;
    root   /etc/nginx/html;
    index  index.html index.htm;

    location /redirect_me {
        return 301 https://www.youtube.com/watch?v=QH2-TGUlwu4;
    }

    error_page 404 /404.html;
    location /404 {
      root /etc/nginx/html;
      internal;      
    }
}" | sudo tee /etc/nginx/sites-available/default

# restart nginx
sudo service nginx restart

