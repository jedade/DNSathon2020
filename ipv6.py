import os
import argparse
import urllib.request
import sys

parser = argparse.ArgumentParser()
parser.add_argument("domain", type=str, help="le domaine")
args = parser.parse_args()
domain = args.domain

def CheckIpv6(domain):
        result=os.popen(f"dig {domain} AAAA +short")
        result=result.read()
        if result != " ":
                print(f"IPV6: {result}")

CheckIpv6(domain)

de