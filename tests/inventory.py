#!/usr/bin/python
import argparse
import json
import paramiko
import subprocess
import sys

def parse_args():
  parser = argparse.ArgumentParser(description="Inventory script")
  group = parser.add_mutually_exclusive_group(required=True)
  group.add_argument('--list', action='store_true')
  group.add_argument('--host')
  return parser.parse_args()

def list_hosts():
        hostnames = []
	for i in range(1,10):
	  hostnames.append("new"+str(i))
        cmd = ["echo",",".join(hostnames)]; 
	list = subprocess.check_output(cmd).rstrip()
	hosts = []
	for item in list.split(","):
  	  hosts.append(item)
	return hosts
	
def get_host_details(host):
	return {'ansible_host': host,
	'ansible_port': 22,
	'ansible_user': "root"}
	
def main():
	args = parse_args()
	if args.list:
		hosts = list_hosts()
		json.dump({'tests': hosts}, sys.stdout)
	else:
		details = get_host_details(args.host)
		json.dump(details, sys.stdout)

if __name__ == '__main__':
	main()

