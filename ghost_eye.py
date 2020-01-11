#!/usr/bin/env/python3
# This Python file uses the following encoding: utf-8

# ===== #
# Jolanda de Koff
# Bulls Eye: https://github.com/BullsEye0
# Website: https://hackingpassion.com
# linkedin: https://www.linkedin.com/in/jolandadekoff
# Facebook: facebook.com/jolandadekoff
# Facebook Page: https://www.facebook.com/ethical.hack.group
# Facebook Group: https://www.facebook.com/groups/hack.passion/
# YouTube: https://www.youtube.com/BullsEyeJolandadeKoff
# ===== #

# ===== #
# Created July 2019 | Copyright (c) 2019 - 2020 Jolanda de Koff.
# ===== #

########################################################################

# A notice to all nerds and n00bs...
# If you will copy the developer's work it will not make you a hacker..!
# Respect all developers, we doing this because it's fun...

########################################################################


from bs4 import BeautifulSoup
from collections import deque
import json
import nmap
import os
import re
import requests
import requests.exceptions
import time
from time import gmtime, strftime
from urllib.error import URLError
from urllib.parse import urlsplit
import urllib3
import urllib.request
from urllib.request import urlopen


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
  `------'  `--' `--'     `-----'  `-----'    `--'          `------'  `--'       `------'
            \033[1;m
        \033[34mGhost Eye - Information Gathering Tool \033[0m
        \033[34mAuthor: Jolanda de Koff https://github.com/BullsEye0 | Bulls Eye \033[0m
        \033[34mWebsite: https://hackingpassion.com \033[0m

              Hi there, Shall we play a game..? """)


def menu():
    print("\n\033[1;34m[+] 1.   Whois Lookup\033[1;m")
    print("\033[1;34m[+] 2.   DNS Lookup\033[1;m")
    print("\033[1;34m[+] 3.   EtherApe – Graphical Network Monitor (root)\033[1;m")
    print("\033[1;34m[+] 4.   Nmap Port Scan\033[1;m")
    print("\033[1;34m[+] 5.   HTTP Header Grabber\033[1;m")
    print("\033[1;34m[+] 6.   Clickjacking Test - X-Frame-Options Header\033[1;m")
    print("\033[1;34m[+] 7.   Robots.txt Scanner\033[1;m")
    print("\033[1;34m[+] 8.   Link Grabber\033[1;m")
    print("\033[1;34m[+] 9.   IP Location Finder\033[1;m")
    print("\033[1;34m[+] 10.  Traceroute\033[1;m")
    print("\033[1;34m[+] 11.  Have I been pwned\033[1;m")
    print("\033[1;34m[x] 12.  Exit\033[1;m\n")


def fun():
    choice = ("1")
    banner()

    while choice != ("12"):
        menu()
        choice = input("\033[1;34m[+]\033[1;m \033[1;91mEnter your choice:\033[1;m ")

        if choice == ("1"):
            try:
                target = input("\033[1;91mEnter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34mSearching for... Whois Lookup: \033[0m".format(target) + target)
                time.sleep(1.5)
                command = ("whois " + target)
                proces = os.popen(command)
                results = str(proces.read())
                print("\033[1;34m" + results + command + "\033[1;m")

            except Exception:
                pass

        elif choice == ("2"):
            try:
                target = input("\033[1;91mEnter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34mSearching for... DNS Lookup: \033[0m".format(target) + target)
                time.sleep(1.5)
                command = ("dig " + target + " +trace ANY")
                proces = os.popen(command)
                results = str(proces.read())
                print("\033[1;34m" + results + command + "\033[1;m")

            except Exception:
                pass

        elif choice == ("3"):
            try:
                os.system("reset")
                os.system("gnome-terminal -e 'bash -c \"sudo etherape; exec bash\"'")

            except Exception:
                pass

        elif choice == ("4"):
            try:
                target = input("\033[1;91mEnter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34mScanning.... Nmap Port Scan: \033[0m" + target)
                print("This will take a moment.\n")
                time.sleep(1.5)

                scanner = nmap.PortScanner()
                command = ("nmap -Pn " + target)
                process = os.popen(command)
                results = str(process.read())
                logPath = "logs/nmap-" + strftime("%Y-%m-%d_%H:%M:%S", gmtime())

                print("\033[34m" + results + command + logPath + "\033[0m")
                print("\033[34mNmap Version: \033[0m", scanner.nmap_version())

            except KeyboardInterrupt:
                    print("\n")
                    print("[-] User Interruption Detected..!")
                    time.sleep(1)

        elif choice == ("5"):
            try:
                target = input("\033[1;91mEnter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34mScanning.... HTTP Header Grabber: \033[0m\n" + target)
                time.sleep(1.5)
                command = ("http -v " + target)
                proces = os.popen(command)
                results = str(proces.read())
                print("\033[1;34m" + results + command + "\033[1;m")

            except Exception:
                pass

        elif choice == ("6"):
            target = input("\033[1;91mEnter the Domain to test: \033[1;m").lower()
            os.system("reset")

            if not (target.startswith("http://") or target.startswith("https://")):
                target = "http://" + target
            print("\033[1;34mTesting...  Clickjacking Test: \033[1;m" + target)
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
                target = input("\033[1;91mEnter Domain: \033[1;m").lower()
                os.system("reset")
                print("\033[34mScanning.... Robots.txt Scanner: \033[0m\n" + target)
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
            try:
                target = input("\033[1;91mEnter Domain: \033[1;m").lower()
                os.system("reset")
                print("\033[34mScanning.... Link Grabber: \033[0m\n" + target)
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

        elif choice == ("9"):
            try:
                target = input("\033[1;91mEnter Domain or IP Address: \033[1;m").lower()
                url = ("http://ip-api.com/json/")
                response = urllib.request.urlopen(url + target)
                data = response.read()
                jso = json.loads(data)
                os.system("reset")
                print("\033[34mSearching.... IP Location Finder: \033[0m".format(url) + target)
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

        elif choice == ("10"):
            try:
                target = input("\033[1;91mEnter Domain or IP Address: \033[1;m").lower()
                os.system("reset")
                print("\033[34mSearching for: Traceroute: \033[0m".format(target) + target)
                print("This will take a moment... Get some coffee :)\n")
                time.sleep(5)
                command = ("mtr " + "-4 -rwc 1 " + target)
                proces = os.popen(command)
                results = str(proces.read())
                print("\033[1;34m" + results + command + "\033[1;m")

            except Exception:
                pass

        elif choice == ("11"):
            try:
                target = input("\033[1;91mEnter email: \033[0m")
                os.system("reset")
                print("\033[34mScanning....Have I been pwned: \033[0m\n" + target)
                time.sleep(1.5)
                url = ("https://haveibeenpwned.com/api/v2/breachedaccount/%s" % target)
                response = requests.get(url)

                if response.status_code == 200:
                    response = response.json()
                    le = len(response)

                    for item in range(le):
                        clas = str(response[item]["DataClasses"])
                        clas = re.sub("\[(?:[^\]|]*\|)?([^\]|]*)\]", r"\1", clas)
                        clas = clas.replace("'", "")

                        print("\n")
                        print("Name:     " + "\033[34m" + str(response[item]["Title"]) + "\033[0m")
                        print("Domain:   " + "\033[34m" + str(response[item]["Domain"]) + "\033[0m")
                        print("Breached: " + "\033[34m" + str(response[item]["BreachDate"]) + "\033[0m")
                        print("Details:  " + "\033[34m" + str(clas) + "\033[0m")
                        print("Verified: " + "\033[34m" + str(response[item]["IsVerified"]) + "\033[0m")
                else:
                    print(" Email NOT Found in Database")

            except Exception:
                print(" \033[1;91mUnable to reach HaveIBeenPwned\033[0m")

        elif choice == ("12"):
            time.sleep(1)
            print("\n\t\033[34mBlue Eye\033[0m DONE... Exiting... \033[34mLike to See Ya Hacking Anywhere ..!\033[0m\n")

        else:
            print("\033[1;31m[-] Invalid option!\033[1;m")


# =====# Main #===== #

if __name__ == "__main__":
    fun()
