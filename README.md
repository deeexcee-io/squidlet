# squidlet 🦑
Squid Pivoting Open Port Scanner - v2

## What is it? 🤷🏼‍♂️

Just an updated version of this tool - https://github.com/aancw/spose which a squid proxy port scanner.

All credit to the original author. I just ran it through chatgpt, told it to add threading to make it faster and run through the whole 0-65535 port range instead of a handful of ports.

## Why is it better? 💡

Its faster. Plus it scans all ports by default. You shouldnt have to mess with the code to find all the open ports. Plus you can ctrl-c to kill it which you cant do with spose.

### Scientific Testing 🤣
squidlet takes 328 seconds to scan the full 65535 port range. 

```bash
└─# time python3 squidlet.py --proxy http://10.10.121.66:3128 --target 10.10.121.66 --threads 20
Using proxy address http://10.10.121.66:3128
10.10.121.66 22 seems OPEN
10.10.121.66 9195 seems OPEN
10.10.121.66 9192 seems OPEN
10.10.121.66 9191 seems OPEN

real    328.00s
user    128.35s
sys     36.03s
cpu     50%
```

spose takes ***** seconds to scan the top 1000 ports, which you have to add manually. 

I got tired of waiting, its been over 10 minutes now. I cant even ctrl-c it

```bash
┌──(root㉿kali)-[/opt/spose]
└─# time python3 spose.py --proxy http://10.10.121.66:3128 --target 10.10.121.66
Using proxy address http://10.10.121.66:3128
10.10.121.66 22 seems OPEN 
10.10.121.66 9191 seems OPEN 
10.10.121.66 9192 seems OPEN 
10.10.121.66 9195 seems OPEN 


^C^C


```



## Is it Accurate?

You may need to tweak the threads. Obviously the higher the thread count the more prone it is to either missing a port or reporting false positives. I found 20 to be both accurate and fast (enough).

# Install and Useage

```bash
git clone <repo>

└─# python3 squidlet.py                                                                    
usage: Squidlet by Deeexcee, forked and borked from Spose by Petruknisme [-h] [--proxy PROXY] [--target TARGET]
                                                                         [--threads THREADS]

Squid Pivoting Open Port Scanner

options:
  -h, --help         show this help message and exit
  --proxy PROXY      Define proxy address url(http://xxx:3128)
  --target TARGET    Define target IP behind proxy
  --threads THREADS  Number of threads to use for scanning

└─# python3 squidlet.py --proxy http://10.10.121.66:3128 --target 10.10.121.66 --threads 20
```



