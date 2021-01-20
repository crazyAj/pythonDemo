import smtplib
import traceback
from email.header import Header
from email.mime.text import MIMEText

# 授权码
auth = "HJYEPEPIHOVMTSOU"
sender = "yangwenjiemail@163.com"
receiver = "389130663@qq.com"


def send():
    html = """
        <p>测试 HTML 邮件内容</p>
        <a>https://www.baidu.com</a>
    """
    message = MIMEText(html, 'html', 'utf-8')
    message['From'] = sender
    message['To'] = receiver
    message['Subject'] = Header('Python 测试 HTML 邮件！', 'utf-8')
    try:
        smtpObj = smtplib.SMTP()
        smtpObj.connect('smtp.163.com', 25)
        smtpObj.login(sender, auth)
        smtpObj.sendmail(sender, receiver, message.as_string())
        smtpObj.quit()
        print('邮件已发送')
    except:
        print(traceback.format_exc())


if __name__ == '__main__':
    send()
