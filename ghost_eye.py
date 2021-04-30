#!/usr/bin/env/python3
# This Python file uses the following encoding: utf-8

# ===== #
# ▀█████████▄     ▄████████         Websites: HackingPassion.com | Bullseye0.com
#   ███    ███   ███    ███         Author: Jolanda de Koff | Bulls Eye
#   ███    ███   ███    █▀          GitHub: https://github.com/BullsEye0
#  ▄███▄▄▄██▀   ▄███▄▄▄             linkedin: https://www.linkedin.com/in/jolandadekoff
# ▀▀███▀▀▀██▄  ▀▀███▀▀▀             Facebook Group: https://www.facebook.com/groups/hack.passion/
#   ███    ██▄   ███    █▄          Facebook: facebook.com/jolandadekoff
#   ███    ███   ███    ███         Twitter: https://twitter.com/bulls__eye
# ▄█████████▀    ██████████         LBRY: https://lbry.tv/$/invite/@bullseye0:f
# ===== #

# ===== #
# Created July 2019 | Copyright (c) 2019 - 2021 Jolanda de Koff.
# Update April 2021
# ===== #

########################################################################

# A notice to all nerds and n00bs...
# If you will copy the developer's work it will not make you a hacker..!
# Respect all developers, we doing this because it's fun...

########################################################################

# install dnsutils
# install gnome-terminal
# install httpie
# install mtr

# sudo apt install dnsutils gnome-terminal httpie mtr
# sudo pacman -S dnsutils gnome-terminal httpie mtr

########################################################################

from bs4 import BeautifulSoup
import cfscrape
from collections import deque
import json
import nmap
import os
from os import system
import re
import requests
import requests.exceptions
import requests as res
from requests import get
import sys
import time
from time import gmtime, strftime
from urllib.error import URLError
from urllib.parse import urlsplit
import urllib3
import urllib.request
from urllib.request import urlopen
import urllib.parse
import webtech


def banner():
    print(""" \033[1;34m
             ('-. .-.               .-')    .-') _            ('-.                 ('-.
            ( OO )  /     Ghost    ( OO ). (  OO) )         _(  OO)      Eye     _(  OO)
  ,----.    ,--. ,--. .-'),-----. (_)---\_)/     '._       (,------. ,--.   ,--.(,------.
 '  .-./-') |  | |  |( OO'  .-.  '/    _ | |'--...__)       |  .---'  \  `.'  /  |  .---'
 |  |_( O- )|   .|  |/   |  | |  |\  :` `. '--.  .--'       |  |    .-')     /)  |  |
 |  | .--, \|       |\_) |  |\|  | '..`''.)   |  |         (|  '--.(OO  \   /.  (|  '--.
(|  | '. (_/|  .-.  |  \ |  | |  |.-._)   \   |  |          |  .--' |   /  /     |  .--'
 |  '--'  | |  | |  |   `'  '-'  '\       /   |  |          |  `---.`-./  /      |  `---.
  `------'  `--' `--'     `-----'  `-----'    `--' V2       `------'  `--'       `------'
            \033[1;m
        \033[34mGhost Eye - Information Gathering Tool \033[0m
        \033[34mAuthor: Jolanda de Koff aka Bulls Eye \033[0m
        \033[34mGithub:  https://github.com/BullsEye0 \033[0m
        \033[34mWebsite: https://hackingpassion.com \033[0m

              Hi there, Shall we play a game..? 😃 """)


def menu():
    print("\n\033[1;34m[+] 1.   EtherApe – Graphical Network Monitor (root)\033[1;m")
    print("\033[1;34m[+] 2.   DNS Lookup\033[1;m")
    print("\033[1;34m[+] 3.   Whois Lookup \033[1;m")
    print("\033[1;34m[+] 4.   Nmap Port Scan\033[1;m")
    print("\033[1;34m[+] 5.   HTTP Header Grabber\033[1;m")
    print("\033[1;34m[+] 6.   Clickjacking Test - X-Frame-Options Header\033[1;m")
    print("\033[1;34m[+] 7.   Robots.txt Scanner\033[1;m")
    print("\033[1;34m[+] 8.   Cloudflare Cookie scraper\033[1;m")
    print("\033[1;34m[+] 9.   Link Grabber\033[1;m")
    print("\033[1;34m[+] 10.  IP Location Finder\033[1;m")
    print("\033[1;34m[+] 11.  Detecting CMS with Identified Technologies\033[1;m")
    print("\033[1;34m[+] 12.  Traceroute\033[1;m")
    print("\033[1;34m[+] 13.  Crawler target url + Robots.txt\033[1;m")
    print("\033[1;34m[+] 14.  Certificate Transparency log monitor\033[1;m")
    print("\033[1;34m[x] 15.  Exit\033[1;m\n")


def fun():
    choice = ("1")
    banner()

    while choice != ("12"):
        menu()
        choice = input("\033[1;34m[+]\033[1;m \033[1;91mEnter your choice:\033[1;m ")

        if choice == ("3"):
            try:
                target = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34m[~] Searching for Whois Lookup: \033[0m".format(target) + target)
                time.sleep(1.5)
                command = ("whois " + target)
                proces = os.popen(command)
                results = str(proces.read())
                print(results + command)

            except Exception:
                pass

        elif choice == ("2"):
            try:
                target = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34m[~] Searching for DNS Lookup: \033[0m".format(target) + target)
                time.sleep(1.5)
                command = ("dig " + target + " +trace ANY")
                proces = os.popen(command)
                results = str(proces.read())
                print(results + command)

            except Exception:
                pass

        elif choice == ("1"):
            try:
                os.system("reset")
                os.system("gnome-terminal -e 'bash -c \"sudo etherape; exec bash\"'")

            except Exception:
                pass

        elif choice == ("4"):
            try:
                target = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34m[~] Scanning Nmap Port Scan: \033[0m" + target)
                print("This will take a moment... Get some coffee 😃 )\n")
                time.sleep(1.5)

                scanner = nmap.PortScanner()
                command = ("nmap -Pn " + target)
                process = os.popen(command)
                results = str(process.read())
                logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())

                print(results + command + logPath)
                print("\033[34mNmap Version: \033[0m", scanner.nmap_version())

            except KeyboardInterrupt:
                    print("\n")
                    print("[-] User Interruption Detected..!")
                    time.sleep(1)

        elif choice == ("5"):
            try:
                target = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34m[~] Scanning HTTP Header Grabber: \033[0m\n" + target)
                time.sleep(1.5)
                command = ("http -v " + target)
                proces = os.popen(command)
                results = str(proces.read())
                print(results + command)

            except Exception:
                pass

        elif choice == ("6"):
            target = input("\033[1;91m[+] Enter the Domain to test: \033[1;m").lower()
            os.system("reset")

            if not (target.startswith("http://") or target.startswith("https://")):
                target = "http://" + target
            print("\033[1;34m[~] Testing Clickjacking Test: \033[1;m" + target)
            time.sleep(2)
            try:
                resp = requests.get(target)
                headers = resp.headers
                print("\nHeader set are: \n")
                for item, xfr in headers.items():
                    print("\033[1;34m" + item + ":" + xfr + "\033[1;m")

                if "X-Frame-Options" in headers.keys():
                    print("\n[+] \033[1;34mClick Jacking Header is present\033[1;m")
                    print("[+] \033[1;34mYou can't clickjack this site !\033[1;m\n")
                else:
                    print("\n[*] \033[1;34mX-Frame-Options-Header is missing ! \033[1;m")
                    print("[!] \033[1;34mClickjacking is possible,this site is vulnerable to Clickjacking\033[1;m\n")

            except Exception as ex:
                print("\033[1;34mException caught: " + str(ex))

        elif choice == ("7"):
            try:
                target = input("\033[1;91m[+] Enter Domain: \033[1;m").lower()
                os.system("reset")
                print("\033[34m[~] Scanning Robots.txt Scanner: \033[0m\n" + target)
                time.sleep(1.5)

                if not (target.startswith("http://") or target.startswith("https://")):
                    target = "http://" + target
                robot = target + "/robots.txt"

                try:
                    bots = urlopen(robot).read().decode("utf-8")
                    print("\033[34m" + (bots) + "\033[1;m")
                except URLError:
                    print("\033[1;31m[-] Can\'t access to {page}!\033[1;m".format(page=robot))

            except Exception as ex:
                print("\033[1;34mException caught: " + str(ex))

        elif choice == ("8"):
            target = input("\033[1;91m[+] Enter Domain: \033[1;m").lower()
            if not (target.startswith("http://") or target.startswith("https://")):
              	target = "http://" + target
            os.system("reset")
            print("[+] Cloudflare cookie scraper ")
            time.sleep(1.5)

            sess = cfscrape.create_scraper()
            try:
            	print("[+] Target: " + target)
            	request = "GET / HTTP/1.1\r\n"
            	cookie_value, user_agent = cfscrape.get_cookie_string(target)
            	request += "Cookie: %s\r\nUser_Agent: %s\r\n" % (cookie_value, user_agent)
            	data = sess.get(target)
            	out = BeautifulSoup(data.content,'html.parser')
            	print("[+] Print Cookie\n")
            	print(request)
            	os.system('tput setaf 10')
            	print("\n[+] Scraper ")
            	print(out)

            except ValueError:
            	print('[X] Unable to find Cloudflare cookies. This website does not have Cloudflare IUAM enabled.')

        elif choice == ("9"):
            try:
                target = input("\033[1;91m[+] Enter Domain: \033[1;m").lower()
                os.system("reset")
                print("\033[34m[~] Scanning Link Grabber: \033[0m\n" + target)
                time.sleep(2)
                if not (target.startswith("http://") or target.startswith("https://")):
                    target = "http://" + target
                deq = deque([target])
                pro = set()

                try:
                    while len(deq):
                        url = deq.popleft()
                        pro.add(url)
                        parts = urlsplit(url)
                        base = "{0.scheme}://{0.netloc}".format(parts)

                        print("[+] Crawling URL " + "\033[34m" + url + "\033[0m")
                        try:
                            response = requests.get(url)
                        except (requests.exceptions.MissingSchema, requests.exceptions.ConnectionError):
                            continue

                        soup = BeautifulSoup(response.text, "lxml")
                        for anchor in soup.find_all("a"):
                            link = anchor.attrs["href"] if "href" in anchor.attrs else ''
                            if link.startswith("/"):
                                link = base + link
                            if not link in deq and not link in pro:
                                deq.append(link)
                            continue

                except KeyboardInterrupt:
                        print("\n")
                        print("[-] User Interruption Detected..!")
                        time.sleep(1)
                        print("\n \t\033[34m[!] I like to See Ya, Hacking Anywhere ..!\033[0m\n")

            except Exception:
                pass

        elif choice == ("10"):
            try:
                target = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
                url = ("http://ip-api.com/json/")
                response = urllib.request.urlopen(url + target)
                data = response.read()
                jso = json.loads(data)
                os.system("reset")
                print("\033[34m[~] Searching IP Location Finder: \033[0m".format(url) + target)
                time.sleep(1.5)

                print("\n [+] \033[34mUrl: " + target + "\033[0m")
                print(" [+] " + "\033[34m" + "IP: " + jso["query"] + "\033[0m")
                print(" [+] " + "\033[34m" + "Status: " + jso["status"] + "\033[0m")
                print(" [+] " + "\033[34m" + "Region: " + jso["regionName"] + "\033[0m")
                print(" [+] " + "\033[34m" + "Country: " + jso["country"] + "\033[0m")
                print(" [+] " + "\033[34m" + "City: " + jso["city"] + "\033[0m")
                print(" [+] " + "\033[34m" + "ISP: " + jso["isp"] + "\033[0m")
                print(" [+] " + "\033[34m" + "Lat & Lon: " + str(jso['lat']) + " & " + str(jso['lon']) + "\033[0m")
                print(" [+] " + "\033[34m" + "Zipcode: " + jso["zip"] + "\033[0m")
                print(" [+] " + "\033[34m" + "TimeZone: " + jso["timezone"] + "\033[0m")
                print(" [+] " + "\033[34m" + "AS: " + jso["as"] + "\033[0m" + "\n")

            except URLError:
                print("\033[1;31m[-] Please provide a valid IP address!\033[1;m")

        elif choice == ("11"):
            try:
                target = input("\033[1;91m[+] Enter Domain: \033[1;m").lower()
                if not (target.startswith("http://") or target.startswith("https://")):
                 	target = "https://" + target
                os.system("reset")
                print("\033[34m[~] Detecting CMS with Identified Technologies and Custom Headers from target url: \033[0m")
                time.sleep(5)
                command = ("mtr " + "-4 -rwc 1 " + target)
                obj = webtech.WebTech()
                results = obj.start_from_url(target, timeout=1)
                sys.stdout.write(results)

            except Exception:
                pass

        elif choice == ("12"):
            try:
                target = input("\033[1;91m[+] Enter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34m[~] Searching for Traceroute \033[0m".format(target) + target)
                print(">> This will take a moment... Get some coffee << )\n")
                time.sleep(5)
                command = ("mtr " + "-4 -rwc 1 " + target)
                proces = os.popen(command)
                results = str(proces.read())
                print("\033[1;34m" + results + command + "\033[1;m")
                fun()

            except KeyError:
             	pass

        elif choice == ("13"):
            target = input("\033[1;91m[+] Enter Domain: \033[1;m").lower()
            os.system("reset")
            print("\033[34m[~] Start crawler... \033[0m")
            time.sleep(5)
            print("[+] Target: " + target)
            if not (target.startswith("http://") or target.startswith("https://")):
            	target = "http://" + target
            try:
            	content = get(target).text
            	regex_t = re.compile(r"<title>(.*?)<\/title>")
            	tit = re.findall(regex_t, content)

            	regex_l = re.compile(r"http[s]?://(?:[a-zA-Z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-fA-F][0-9a-fA-F]))+")
            	link = re.findall(regex_l, content)

            	robots = get(target + "/robots.txt").text

            	print("[+] Title: "+ ''.join(tit) + "\n")
            	print("[+] Extract links: \n" + '\n'.join(link) + "\n")
            	print("[+] Robots.txt: \n" + robots)

            except KeyError:
             	pass

        elif choice == ("14"):
            target = input("\033[1;91m[+] Enter Domain: \033[0m")
            os.system("reset")
            print("\033[34m[~] Scanning Certificate Transparency log monitor: \033[0m\n" + target)
            time.sleep(1.5)
            print("[+] Target: " + target)
            try:
            	headers = {
            	'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_2) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/62.0.3202.94 Safari/537.36', }
            	results = requests.get('https://api.certspotter.com/v1/issuances?domain='+target+'&expand=dns_names&expand=issuer&expand=cert | jq ".[].dns_names[]" | sed "s/\"//g" | sed "s/\*\.//g" | sort -u | grep '+target,headers=headers)
            	results = results.text.split('\n')
            	print(*results, sep = "\n")

            except KeyError:
             	pass

        elif choice == ("15"):
            time.sleep(1)
            print("\n\t\033[34mBlue Eye\033[0m DONE... Exiting... \033[34mLike to See Ya Hacking Anywhere ..!\033[0m\n")
            sys.exit()

        else:
            os.system("reset")
            print("\033[1;31m[-] Invalid option..! \033[1;m")


# =====# Main #===== #

if __name__ == "__main__":
    fun()
