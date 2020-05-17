#!/usr/bin/python
import os
import requests
import tldextract
import signal
from optparse import OptionParser
from colorama import *


def banner():
    print(
        Style.BRIGHT
        + Fore.YELLOW
        + """
           ___   ___   __                   __
          ||  | ||  | || |_    ___   ____  || |_    ___   __ __
          ||  | ||  | ||  _|  //  \ // __| ||  _|  //  \ || '__|
          ||  | ||=-  || |_  ||---- \__  \ || |_  ||---- || |
          ||__| ||  |  \___|  \____ ||___/  \___|  \____ ||_|

                                 [ Leon (geek_pwn@protonmail.com) ]
                                          [ twitter.com/leonmugen ]
        """
        + Style.RESET_ALL
    )


def main():
    os.system("clear")
    banner()
    usage = "Usage: python %prog [-h] -u 'URL' -f [file]"

    parser = OptionParser(usage=usage)
    parser.add_option("-u", "--url", dest="url", help="target URL")
    parser.add_option("-f", "--file", dest="file", help="payloads file")

    (options, args) = parser.parse_args()
    if options.url is None:
        parser.print_help()
        exit()

    # Payloads file
    if options.file is True:
        s.addOption("file", True)

    # Replace string in payloads file
    urlD = options.url
    info = tldextract.extract(urlD)
    domain_name = info.registered_domain
    payloadlist = open("payloads.list", "r").readlines()
    newlist = open("all.list", "w")
    for line in payloadlist:
        if line.count("example") == 1 or line.count("example") == 2:
            l = line.replace("example.com", domain_name)
            newlist.write(l)
        else:
            newlist.write(line)
    newlist.close()

    # Open file
    with open(options.file) as f:
        for payload in f:
            payloadF = payload.strip()
            urlF = options.url + payloadF
            print(urlF)

            # Get the response(200,400,404).
            response = requests.head(urlF)

            # ===Process to find an open redirect===.
            if response.history:
                # Compare the destination url with Bing's url.
                if (
                    str(response.url)[0:19] == "http://www.bing.com"
                    or str(response.url)[0:20] == "https://www.bing.com"
                ):

                    print(
                        Style.BRIGHT
                        + Fore.YELLOW
                        + "Open Redirect Vulnerability found!"
                        + Style.RESET_ALL
                    )
                    print(Fore.YELLOW + "Redirected to: " + response.url)
                    print(
                        Style.BRIGHT
                        + Fore.BLUE
                        + "Payload ---> "
                        + payloadF
                        + Style.RESET_ALL
                    )
                    exit()
                else:
                    print(
                        Fore.YELLOW + "Redirected to: " + response.url + Style.RESET_ALL
                    )

            else:
                print(
                    "Request was not redirected. Check manually because it might be a redirect using javascript. b\n"
                )


# Press ctrl+c to finish
def ctrl_c(signum, rfm):
    print("\nSee you soon!\n")
    exit()


signal.signal(signal.SIGINT, ctrl_c)

try:
    main()
    print(Fore.YELLOW + "RESULT: " + Style.RESET_ALL + "No Open Redirect Found!")
except (TypeError):
    print("Usage: python ordetector.py -u 'URL' -f [file]\n")
