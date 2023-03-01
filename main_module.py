from codexplore import emailProcess, printMsg

def main ():
    emails = ["bui@gmail.com", "xuan@gmail.com", "huan@gmail.com"]
    for email in emails:
        usename, email_domail = emailProcess(email)
        printMsg(usename, email_domail)
if __name__ == "__main__":
               main()