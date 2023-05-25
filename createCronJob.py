#Pete Lenhart / 5/24/2023

#!/usr/bin/env python3

import os
from crontab import CronTab

def create_cron_job():
    
    cron = CronTab(user=True)
    job = cron.new(command=f"python3 {os.path.abspath('/root/scripts/startServiceOrReboot.py')}")
    job.hour.every(1)  # Run the job every hour
    cron.write()

def main():
    create_cron_job()

if __name__ == "__main__":
    main()
