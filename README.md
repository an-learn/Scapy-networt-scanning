# Scapy-networt-scanning
SNS is a network scanning framework based on python scapy.And it is my first works, wish one day I can make better.

Hello ,I am anlearn. After I finish the network scanning course of teacher YuanFanghong, I want to write my own tool.
The SNS is the result of my work. It is only 476KB which won't take you too much space.
Which surprised me is  the UDP_scanning is a little faster than nmap, even the else part take more time than nmap.

I hope you would like to help in this program to make it faster and function more,   
Any suggest or opinion contact me `jiangjiexiang@foxmail.com`

You can use it in a very easy way,follow the step(on kali):  
do this part only once:

    cd SNS

    chmod +x setup.sh

    ./setup.sh
To start:

    ./main.py
What you need to do is just:

    select an number, then push "Enter"
    
    "bk" to go back
    
    "show" to show choice
    
    "exit" to exit the program
You can see:

    ################################
    #                              #
    #    Scapy Network Scanning    #
    #            V1.0              #
    #         by Anlearn           #
    #                              #
    ################################


    Select An Option from the Menu:

    1.Discovery Scanning

    2.Port Scanning

    3.Firewall Scanning

    4.Fingerprinting

    5.More

    [main] Select > 
Enter a number an push "Enter"(such as "1"):  
you can see:

    [main] Select > 1
    ===========================

    Choose a type of Discovery Scanning:


    ------ layer 2 ------

    1.ARP Ping

    ------ layer 3 ------

    2.Ping

    ------ layer 4 ------

    3.TCP SYN Ping

    4.TCP ACK Ping

    5.TCP SYN+ACK Ping

    6.UDP Ping

    ------- other -------

    7.All but ARP Ping

    [discovery] Select > 
Enter a number an push "Enter"(such as "2"):  
you can see:

    [discovery] Select > 2
    ===========================

    1.Enter IP address
      1.1 Normal
      1.2 Neatly (when IP too much,a little slow)

    2.Select a file

    [ping] Select >  
Enter a number an push "Enter"(such as "1.1"):  
you can see:

    [ping] Select > 1.1
    ===========================

    Separate IP address by "," (support "1-254")

    [ping] IP > 
Enter IP an push "Enter":  
Remeber !!!  
Remeber !!!  
Remeber !!!  
Three times for important ting ^_^

    Separate IP address by ","
    As: 192.168.1.1
        192.168.1.1,192.168.1.2
        192.168.1.1-100
        192.168.1.1,192.168.1.50-100
        not support "0/24" now
wait for a few seconds,you can see

    [ping] IP > 192.168.1.1,192.168.1.100-120
    ===========================

     Alive:
    192.168.1.113

    192.168.1.101

    192.168.1.109

    192.168.1.1

    192.168.1.105

    finish in 0:00:08.771630
    ---------------------------
    [ping] IP > 
If you enter the wrong IP, SNS can distinguish:

    [ping] IP > 192.168.1
    ===========================

    Include incorrect IP format: 192.168.1
    Try again

    [ping] IP > 
!!! Don't enter wrong interface in ARP-Ping,there is no distinguish. !!!
