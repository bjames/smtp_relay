**Usage**
1. Add the submodule using 'git submodule add git@github.com:bjames/smtp_relay.git'
2. Import the submodule into your python projects as follows: 'from smtp_relay.smtp_relay import send_email'
3. When ready, commit your changes and include the submodule: "git commit -am 'added smtp_relay submodule'"
4. Push the changes 'git push origin master'
5. Git will automatically update the submodules when you 'git fetch'/'git merge origin/master' or you can manually update only the submodule with 'git submodule update --remote'

**send_email**

This function supports several keyword arguments. Most are pretty self explanitory, but some are explained below. They all have default values provided by the function, but probably not the values you want. 

- timeout: This is the timeout when connecting to the smtp server. By default the python smtplib doesn't have a timeout. 
- pre_wrap: This module sends HTML emails. The decision to do this was based on outlook not using monospaced fonts for plain text emails by default. If pre_wrap is set to true, then the body of the email is wrapped in pre tags forcing it to be printed with a monospaced font. This is useful for emailing tables that rely on monospace text formatting. 
- generate_file_on_fail: If this is set to true, an HTML file is generated if the script cannot connect to an SMTP server. 

Basic example 

```
subject = 'some subject'
body = '<p>An HTML email body<p>'
receipient = 'brandon@brandonsjames.com'
send_email(subject=subject, body=body, receipient=receipient)
```

More information on git submodules can be found here: https://git-scm.com/book/en/v2/Git-Tools-Submodules
