#!/usr/bin/env python3

import os
import sys

def check_reboot():
    '''Returns TRUe if the computer has a pending reboot.'''
    return os.path.exists("/run/reboot-required")

def main():
    if check_reboot():
        print("Pending Reboot.")
        sys.exit(1)
    print("Everything is OK.")
    sys.exit(0)

main()
