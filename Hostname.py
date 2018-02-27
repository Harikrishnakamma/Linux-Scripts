#!/usr/bin/python3
import os, sys, subprocess
HOST = subprocess.call(['hostname'], shell=True, universal_newlines=True)
print(HOST)
