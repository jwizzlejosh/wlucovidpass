# this program will automatically produce my covid badge and send it to my phone
# written by Joshua Shiman

# CODING BEGINS HERE
# imports
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

# browser initiation
driver = webdriver.Chrome("/usr/local/bin/chromedriver")

# launch site
driver.get('https://wlu.apparmor.com/WebApp/default.aspx?menu=COVID-19+Resources')

time.sleep(0.5)

driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/div[2]/a").click()

time.sleep(2)

# user and password fields
driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[2]/div[2]/div/input[1]").send_keys("your_username")

time.sleep(0.1)

driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div[1]/div[3]/div/div/div/div[4]/div/div/div/div[2]/input").click()

time.sleep(1)

driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div/div[2]/input").send_keys("your_password")

time.sleep(0.5)

driver.find_element_by_xpath("/html/body/div/form[1]/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[4]/div[2]/div/div/div/div/input").click()

time.sleep(0.2)

driver.find_element_by_xpath("/html/body/div/form/div/div/div[2]/div[1]/div/div/div/div/div/div[3]/div/div[2]/div/div[3]/div[2]/div/div/div[1]/input").click()

time.sleep(0.1)
# second page
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/div[2]/a").click()

time.sleep(0.2)

driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/div[2]/input").send_keys("your_phone_number")

time.sleep(0.1)

driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/div[3]/select/option[text()='Brantford']").click()

time.sleep(0.1)

driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/div[4]/input").send_keys("Research and Academic Center")

driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/div[7]/span[1]/input").click()

# third page
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/div[9]/a").click()

time.sleep(0.1)

driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/div[4]/select/option[text()='Yes']").click()

time.sleep(0.2)

driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/div[6]/select/option[2]").click()

driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/div[8]/a").click()

time.sleep(0.1)

# confirm
driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/div[5]/a").click()

time.sleep(0.2)

driver.get('https://wlu.apparmor.com/WebApp/default.aspx?menu=COVID-19+Resources')

time.sleep(0.4)

driver.find_element_by_xpath("/html/body/div/div[2]/form/div[3]/div/div[4]/a").click()

time.sleep(0.2)

driver.save_screenshot("screenshot.png")

# email
Sender_Email = "your_email"
Receiver_Email = "your_email"
Password = "your_password"

msg = MIMEMultipart('alternative')
msg['Subject'] = "Covid Badge"
msg['From'] = Sender_Email
msg['To'] = Receiver_Email

text = MIMEText('<img src="cid:image1">', 'html')
msg.attach(text)

image = MIMEImage(open('/Users/YourUser/PycharmProjects/Covidpass/screenshot.png', 'rb').read())

# Define the image's ID as referenced in the HTML body above
image.add_header('Content-ID', '<image1>')
msg.attach(image)

with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
    smtp.ehlo()
    smtp.starttls()
    smtp.ehlo()
    smtp.login(Sender_Email, Password)
    smtp.sendmail(Sender_Email, Receiver_Email, msg.as_string())

driver.quit()


