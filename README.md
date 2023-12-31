# squidlet 🦑
Squid Pivoting Open Port Scanner - v2

## What is it? 🤷🏼‍♂️

Just an updated version of this tool - https://github.com/aancw/spose which a squid proxy port scanner. It detects open ports behind squid proxy for CTF and pentest purpose using http proxy method.

All credit to the original author. Updated with love and chatgpt <3

## Why is it better? 💡

Its faster. Plus it scans all ports by default. You shouldnt have to mess with the code to find all the open ports. Plus you can ctrl-c to kill it which you cant do with spose.

### Scientific Testing 🤣
**squidlet** takes 328 seconds to scan the full 65535 port range. 

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

**spose** takes ***** seconds to scan the top 1000 ports, which you have to add manually. 

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
**nmap** can take over an hour in some cases...crazy

```bash
┌──(root㉿kali)-[/opt/squidlet]
└─# time proxychains -q nmap -p- 10.10.92.243 -Pn -sTV -n
Starting Nmap 7.94 ( https://nmap.org ) at 2023-07-07 16:50 BST
Stats: 0:00:02 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 0.05% done
Stats: 0:02:36 elapsed; 0 hosts completed (1 up), 1 undergoing Connect Scan
Connect Scan Timing: About 3.69% done; ETC: 18:01 (1:07:50 remaining)
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



