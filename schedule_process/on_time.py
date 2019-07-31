import schedule
import time
from time import gmtime, strftime ,localtime
from datetime import datetime, timedelta
import defs
import rateget_vib as vib
import rateget_vietcombank as vietcombank
import rateget_aba_kh as aba
import rateget_bot as bot
import rateget_ctbc as ctbc
import rateget_cathay as cathay
import rateget_taiwanbusiness as tb
import rateget_vpbank as vpb
import rateget_sacombank as sacom
# $ timedatectl Linux下管理程式
def job(): 
    try:
        # print(strftime("%Y-%m-%d %H:%M:%S", gmtime()))
        date = strftime("%Y-%m-%d", localtime())
        time = strftime("%H:%M:%S", localtime())

        print(vib.rateget()) #越南VIB
        sql = "insert into bank(date,time,bank,ask,bid) values('%s','%s','%s',%s,%s)" % (
            date,time,"VIB",vib.rateget()[1],vib.rateget()[3])  
        defs.run_mysql(sql)

        print(vietcombank.rateget()) #越南VIETCOMBANK
        sql = "insert into bank(date,time,bank,ask,bid) values('%s','%s','%s',%s,%s)" % (
            date,time,"VietComBank",vietcombank.rateget()[1],vietcombank.rateget()[3])  
        defs.run_mysql(sql)

        print(aba.rateget()) #柬埔寨ABA
        sql = "insert into bank(date,time,bank,ask,bid) values('%s','%s','%s',%s,%s)" % (
            date,time,"ABA",aba.rateget()[1],aba.rateget()[2])  
        defs.run_mysql(sql)

        print(bot.rateget()) #台灣台灣銀行
        sql = "insert into bank(date,time,bank,ask,bid) values('%s','%s','%s',%s,%s)" % (
            date,time,"BOT",bot.rateget()[0],bot.rateget()[1])  
        defs.run_mysql(sql)

        print(ctbc.rateget()) #台灣中國信託
        sql = "insert into bank(date,time,bank,ask,bid) values('%s','%s','%s',%s,%s)" % (
            date,time,"CTBC",ctbc.rateget()[0],ctbc.rateget()[1])  
        defs.run_mysql(sql)

        print(cathay.rateget()) #台灣國泰銀行
        sql = "insert into bank(date,time,bank,ask,bid) values('%s','%s','%s',%s,%s)" % (
            date,time,"CATHAY",cathay.rateget()[0],cathay.rateget()[1])  
        defs.run_mysql(sql)

        print('台灣台灣企銀',tb.rateget()) #台灣台灣企銀
        sql = "insert into bank(date,time,bank,ask,bid) values('%s','%s','%s',%s,%s)" % (
            date,time,"Taiwan Business",tb.rateget()[0],tb.rateget()[1])  
        defs.run_mysql(sql)

        print('VPB',vpb.rateget()) #VPB
        sql = "insert into bank(date,time,bank,ask,bid) values('%s','%s','%s',%s,%s)" % (
            date,time,"VPB",vpb.rateget()[0],vpb.rateget()[2])  
        defs.run_mysql(sql)

        print('SACOM',sacom.rateget()) #VPB
        sql = "insert into bank(date,time,bank,ask,bid) values('%s','%s','%s',%s,%s)" % (
            date,time,"SACOM",sacom.rateget()[1],sacom.rateget()[4])  
        defs.run_mysql(sql)

    except:
        pass

# schedule.every(1/20).minutes.do(job) #可以調整時間
schedule.every(60).minutes.do(job) 
# schedule.every().hour.do(job)
# schedule.every().day.at("10:30").do(job)
# schedule.every(5).to(10).days.do(job)
# schedule.every().monday.do(job)
# schedule.every().wednesday.at("13:15").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)