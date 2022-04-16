
from ast import While
import email
from pdb import run
import runpy
from time import sleep
import psutil    #pip install psutil
from playsound import playsound

import smtplib
import yagmail
import keyring

yagmail.register('from@gmail.com', '')
keyring.set_password("yagmail", 'from', '')
yag = yagmail.SMTP('from@gmail.com', '')
message = "Please start charging - Hi Team, Not sufficiently charged Please check" 
message1 = "Please stop charging - Hi Team, Battery is sufficiently charged"

#content = ['This is the body, and here is just text http://somedomain/image.png',
#           'You can find an audio file attached.', '/local/path/song.mp3']
yag.send('to@gmail.com', 'subject', message)
receivers = ['to@gmail.com']
sender = 'from@gmail.com'
yagmail.SMTP(sender).send(receivers, 'subject', message)


battery  = psutil.sensors_battery()
percent_battery = str(battery.percent)

send = 'a'
MAX = 80
MIN = 25

# checking if the charger is plugged
if battery.power_plugged:
    print("Charging: ", battery.percent)
    
    if battery.percent > MAX:
        print("Sufficietly Charged: ", battery.percent)
        run([send, f'Battery above {MAX}%, stop charging.'])
    elif battery.percent < MIN:
        print("Not Sufficient Battery: ", battery.percent)
        #run([send, f'Battery below {MIN}%, start charging.'])
        try:
            print('hello')
            session = smtplib.SMTP('smtp.gmail.com',587)
            session.ehlo()
            session.starttls()
            session.ehlo()
            session.login(sender,'')
            session.sendmail(sender,receivers,message)
            session.quit()
            
        except smtplib.SMTPException:
            print('Error')
else:
    print("Not Charging", battery.percent ,"%")
    print( "Discharge time ", int(battery.secsleft)," sec_lft")
    if battery.percent < MIN:
        print("Not Sufficient Battery: ", battery.percent)
        yagmail.SMTP(sender).send(receivers, 'subject', message)
sleep(300)
# checking if the charger is plugged
try:
    while(psutil.sensors_battery().power_plugged):
        if int(psutil.sensors_battery().percent)==70:
            playsound('a.mp3')
            
# close the program when charger removed            
except Exception as e:
    exit()
