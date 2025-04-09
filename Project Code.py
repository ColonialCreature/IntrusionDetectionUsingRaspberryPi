import RPi.GPIO as GPIO 
import me 
import cv2 
import smtplib 
from email.mime.image import MIMEImage 
from email.mime.mul part import MIMEMul part 
from email.mime.text import MIMEText 
 
# GPIO pin connected to the PIR sensor's OUT pin 
PIR_PIN = 17 
 
# Email se ngs 
SMTP_SERVER = 'smtp.gmail.com'  # Gmail's SMTP server 
SMTP_PORT = 587  # Port for TLS 
SMTP_USERNAME = 'colonial.raspi@gmail.com' 
SMTP_APP_PASSWORD = 'ycadmehsmkjsyydq'  # Generate an App Password from your 
Google account 
RECIPIENT_EMAIL = '202000584@vupune.ac.in' 
 
def send_email(image_path): 
    msg = MIMEMul part() 
    msg['From'] = SMTP_USERNAME 
    msg['To'] = RECIPIENT_EMAIL 
    msg['Subject'] = 'Intrusion Detected' 
 
    text = MIMEText('Mo on detected. Images a ached.') 
    msg.a ach(text) 
    with open(image_path, 'rb') as fp: 
        img = MIMEImage(fp.read()) 
        msg.a ach(img) 
 
    server = smtplib.SMTP(SMTP_SERVER, SMTP_PORT) 
    server.star ls() 
    server.login(SMTP_USERNAME, SMTP_APP_PASSWORD) 
    server.sendmail(SMTP_USERNAME, RECIPIENT_EMAIL, msg.as_string()) 
    server.quit() 
 
def main(): 
    GPIO.setmode(GPIO.BCM) 
    GPIO.setup(PIR_PIN, GPIO.IN) 
     
    try: 
        print("Intrusion Detec on System Running...") 
        while True: 
            if GPIO.input(PIR_PIN): 
                print("Mo on detected!") 
                mestamp = me.str ime("%Y%m%d%H%M%S") 
                image_path = f"/home/pi_{ mestamp}.jpg" 
                 
                # Ini alize the camera 
                camera = cv2.VideoCapture(0) 
                me.sleep(2)  # Warm-up me 
 
                # Capture an image 
                ret, frame = camera.read() 
                if ret: 
                    cv2.imwrite(image_path, frame) 
                    camera.release() 
                    send_email(image_path) 
                    me.sleep(10)  # Wait 10 seconds before rearming the sensor 
                else: 
                    print("Failed to capture image.") 
                 
            me.sleep(1) 
    except KeyboardInterrupt: 
        print("Exi ng...") 
        GPIO.cleanup() 
 
if __name__ == '__main__': 
    main()