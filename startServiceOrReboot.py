#Pete Lenhart / 5/24/2023

#!/usr/bin/env python3

import subprocess

services = ["snmpd", "mwg-core", "mwg-coordinator"]

def check_service(service):
    ps_command = subprocess.Popen(['ps', 'aux'], stdout=subprocess.PIPE)
    grep_command = subprocess.Popen(['grep', service], stdin=ps_command.stdout, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    ps_command.stdout.close()
    output, _ = grep_command.communicate()
    return service in output.decode()

def restart_service(service):
    restart_command = subprocess.Popen(['service', service, 'restart'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, error = restart_command.communicate()
    return restart_command.returncode == 0 and not error

def restart_server():
    reboot_command = subprocess.Popen(['reboot'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
    _, error = reboot_command.communicate()
    return reboot_command.returncode == 0 and not error

def main():
    for service in services:
        if not check_service(service):
            if not restart_service(service):
                restart_server()

if __name__ == "__main__":
    main()
