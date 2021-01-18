# HETZNER SERVER RESET AUTOMATION

![download-removebg-preview](https://user-images.githubusercontent.com/39710677/104828506-61788c80-586a-11eb-8ffd-a68bf7d3db00.png)

This bot is made with Selenium and helps anyone to manage their servers.
If you have a lot of servers and need to launch an automatic hardware reset each single day to clean your machines, this is the right place.
No need to connect again and again in order to do a manual login and reset.

This bot does it for you.

RULES OF THE BOT :

1. UPDATE THE HETZNER FILE (hetzner.py) BY CHANGING THE PARAMETERS OF THIS FUNCTION WITH YOUR INFOS

![Capture d’écran 2021-01-17 à 02 25 51](https://user-images.githubusercontent.com/39710677/104828583-435f5c00-586b-11eb-8b96-d9fd6665c2af.png)

In this function called site_login(email,pwd,server_line), you need to enter the email and password linked with your HETZNER account.
The third argument is server_line : 

![104828665-29724900-586c-11eb-8727-f4c27c3c7883](https://user-images.githubusercontent.com/39710677/104843050-fc07b880-58c8-11eb-9acf-796d917adfb4.png)


Locate the server you want to reset 

                => if it's on the 1st line => server_line = 1
                => if it's on the 2nd line => server_line = 2
                => and so on .... (here I have only 2 servers by the way)



HOW TO RUN THE BOT : 

```
git clone https://github.com/naelob/hetzner-server-reset.git

python3 hetzner.py

```
