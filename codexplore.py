def emailProcess(email):
        email_username = email[0:email.index("@")]
        email_domail = email[email.index("@")+1:]
        return [email_username, email_domail]

def printMsg(email_username, email_domail):
    print(f"Username is {email_username}; Email domail is {email_domail}")

def main ():
       email =  input("please enter your email address").strip()
       email_username, email_domail =  emailProcess(email)
       printMsg(email_username, email_domail)

if __name__ == "__main__":
        main()