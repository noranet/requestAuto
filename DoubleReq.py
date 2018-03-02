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
    cookie='_ga=GA1.2.339485442.1513573245; _ntes_nnid=1db72e7fc13cd14b9b9cdfc37f427bd3,1513576237636; pt_50a6ef75=uid=8ePfke93YNC5XjzTKKnDBg&nid=0&vid=TsjSjqJBigjGB31-3AbUVQ&vn=1&pvn=2&sact=1516688300616&to_flag=0&pl=D-gLTZxFk5rBsNe51KAUYw*pt*1516688300616; mp_35257208c2d3aa7f0909365ac5efd966_mixpanel=%7B%22distinct_id%22%3A%20%22wanglinlin02%22%2C%22%24initial_referrer%22%3A%20%22%24direct%22%2C%22%24initial_referring_domain%22%3A%20%22%24direct%22%7D; mp_MA-AD34-9A6039CC647F_hubble=%7B%22sessionReferrer%22%3A%20%22https%3A%2F%2Fhubble.netease.com%2Fanalytics%2Foverview%22%2C%22updatedTime%22%3A%201516688300677%2C%22sessionStartTime%22%3A%201516688257490%2C%22deviceUdid%22%3A%20%22ec991614-3c3f-42eb-8af6-55988e493557%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referring_domain%22%3A%20%22%24direct%22%2C%22persistedTime%22%3A%201516688257487%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_u_login%22%2C%22time%22%3A%201516688300677%7D%2C%22sessionUuid%22%3A%20%228651b3a8-6b46-4e31-a133-c05b0a9d033e%22%2C%22user_id%22%3A%20%22wanglinlin02%40corp.netease.com%22%7D; _gid=GA1.2.1890386284.1519866700; SESSION=30cb9f80-be10-4738-825f-aab6f1970f2b; userCorp=wanglinlin02%40corp.netease.com; mp_MA-9438-8597C22442CD_hubble=%7B%22deviceUdid%22%3A%20%22459ea099-5725-4fa4-b2ba-a607c708bc75%22%2C%22updatedTime%22%3A%201519886630093%2C%22sessionStartTime%22%3A%201519884888450%2C%22sessionReferrer%22%3A%20%22http%3A%2F%2Fovermind.hz.netease.com%2Fstatic%2Fdata%22%2C%22sessionUuid%22%3A%20%22e59aac02-b7e7-449c-9855-29c5d7a54b90%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referring_domain%22%3A%20%22%24direct%22%2C%22persistedTime%22%3A%201519875351886%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201519886630093%7D%2C%22currentReferrer%22%3A%20%22http%3A%2F%2Fovermind.hz.netease.com%2Fversions%2Flist%22%2C%22user_id%22%3A%20%22H13584%22%7D; mp_MA-86C3-45D0463FDCC0_hubble=%7B%22deviceUdid%22%3A%20%223b614544-e30f-4e87-b189-9bf895c819fa%22%2C%22updatedTime%22%3A%201519889516755%2C%22sessionStartTime%22%3A%201519889516759%2C%22sessionReferrer%22%3A%20%22http%3A%2F%2Fovermind-test.hz.netease.com%2Fapplication%2Flist%2F531%2Fdesc%22%2C%22sessionUuid%22%3A%20%22baf19874-ee0e-4ec8-8369-83573b48a096%22%2C%22initial_referrer%22%3A%20%22%24direct%22%2C%22initial_referring_domain%22%3A%20%22%24direct%22%2C%22persistedTime%22%3A%201519873968159%2C%22LASTEVENT%22%3A%20%7B%22eventId%22%3A%20%22da_screen%22%2C%22time%22%3A%201519889516764%7D%2C%22currentReferrer%22%3A%20%22http%3A%2F%2Fovermind-test.hz.netease.com%2Fapplication%2Flist%2F531%2Fdesc%22%2C%22user_id%22%3A%20%22H13584%22%7D'
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