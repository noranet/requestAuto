# encoding: utf-8
import sys
import os
reload(sys)
sys.setdefaultencoding("utf-8")
import requests
import json
import threading
import schedule
import time
import datetime

def DoubleReq():
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("double:", nowTime)
    url='http://overmind-test.hz.netease.com/api/application/branch/deploy'
    cookie=''
    headerD={'Cookie':cookie,'Content-Type':'application/json'}
    pramD={"applicationId":531,"branchId":101674,'env':2}
    rD= requests.post(url,headers=headerD,data=json.dumps(pramD))
    print rD.json()
    return rD
def job_task():
    threading.Thread(target=DoubleReq).start()
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('job ready','\n',nowTime)
def job1():
    print("I'm working for job1")
    #time.sleep(2)
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print("job1:", nowTime)
def job_task2():
    threading.Thread(target=job1).start()
    nowTime=datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('job tasks ready','\n',nowTime)
def runT():
    schedule.every().day.at("16:27").do(job_task2)
    schedule.every().day.at("16:27").do(job_task2)
    while True:
        schedule.run_pending()
        time.sleep(1)
if __name__=='__main__':
    runT()
