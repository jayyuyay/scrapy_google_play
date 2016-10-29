#! /usr/bin/env bash
export PATH=$PATH:/usr/local/bin
cd /home/hgPro/gp/app/
nohup scrapy crawl google -s JOBDIR=app/jobs >> /home/hgPro/gp/google.log 2>&1 &
