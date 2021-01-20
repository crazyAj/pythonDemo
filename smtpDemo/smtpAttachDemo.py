import smtplib
import traceback
from email.header import Header
from email.mime.application import MIMEApplication
from email.mime.multipart import MIMEMultipart
from email.mime.image import MIMEImage
from email.mime.text import MIMEText

# 授权码
auth = "HJYEPEPIHOVMTSOU"
sender = "yangwenjiemail@163.com"
receiver = "389130663@qq.com"


def send():
    try:
        message = MIMEMultipart()
        message['From'] = sender
        message['To'] = receiver
        message['Subject'] = Header('Python 测试附件上传！', 'utf-8')
        # 邮件正文内容
        html = """
            <p>Python 邮件发送测试...</p>
            <p><a href="http://www.baidu.com">百度</a></p>
            <p>图片演示：</p>
            <p><img src="cid:imgId"></p>
        """
        message.attach(MIMEText(html, 'html', 'utf-8'))

        # HTML 指定图片
        pic =  open(r'D:\aj\soft\wallpager\刺客丶伍陆柒.jpg', 'rb')
        attch = MIMEImage(pic.read())
        pic.close()
        # 定义图片 ID，在 HTML 文本中引用
        attch.add_header('Content-ID', '<imgId>')
        message.attach(attch)

        # 构造附件1 文本
        f1 = open(r'C:\Users\lenovo\Desktop\temp.txt', 'rb')
        att1 = MIMEApplication(f1.read())
        f1.close()
        att1["Content-Type"] = 'application/octet-stream'
        att1["Content-Disposition"] = 'attachment; filename="temp.txt"'
        att1.set_charset('utf-8')
        message.attach(att1)

        # 构造附件2 图片
        f2 = open(r'D:\aj\soft\wallpager\刺客丶伍陆柒.jpg', 'rb')
        att2 = MIMEApplication(f2.read())
        f2.close()
        att2.add_header('Content-Type', 'application/octet-stream')
        att2.add_header('Content-Disposition', 'attachment', filename=('utf-8', '', '刺客丶伍陆柒.jpg'))
        att2.set_charset('utf-8')
        message.attach(att2)

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
