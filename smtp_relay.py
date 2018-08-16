import email.utils, smtplib

from email.mime.text import MIMEText


def generate_file(body, subject):

    ''' generates an html file in the current directory '''

    filename = subject + '.html'

    with open(filename, "w+") as html_file:

        html_file.write(body)
        print("Email failed, results logged to " + filename)


def wrap_body(body, pre_wrap):


    ''' returns the body wrapped in <pre> tags '''
    
    if(pre_wrap):
    
        # simply wraps the body in HTML pre tags so that preformatted plan text is rendered correctly
        return """<html><head></head><body><pre>""" + body + """</pre></body></html>"""

    else:

        return """<html><head></head><body>""" + body + """</body></html>"""


def send_email(subject="", body="", recepient="nobody@brandonsjames.com", sender_name="Automation", sender_email="automation@brandonsjames.com", relay_server="mailrelay.home.internal.brandonsjames.com", timeout=30, pre_wrap=False, generate_file_on_fail=True):

    ''' sends an email using an open smtp relay server '''

    body = wrap_body(body, pre_wrap)

    msg = MIMEText(body, 'html')
    msg['To'] = email.utils.formataddr(('Recepient', recepient))
    msg['From'] = email.utils.formataddr((sender_name, sender_email))
    msg['Subject'] = subject

    server = smtplib.SMTP(relay_server, timeout=timeout)

    try:
        server.sendmail(sender_email, [recepient], msg.as_string())
    except:
        if generate_file_on_fail:
            generate_file(body, subject)
    finally:
        server.quit()