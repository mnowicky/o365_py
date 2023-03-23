import oAuthConnect
import imaplib

def generate_auth_string(user, token):
    return 'user=%s\1auth=Bearer %s\1\1' % (user, token)

def connectMailbox():
    token = oAuthConnect.acquireToken()
    mailserver = 'outlook.office365.com'
    mailBox = 'noco@eco-maxx.com'
    imapport = 993
    imap = imaplib.IMAP4_SSL(mailserver,imapport)
    imap.debug = 4
    imap.authenticate('XOAUTH2', lambda x: generate_auth_string(mailBox, token['access_token']))
    
    #print(token)
    #print(imap.list())
    #print(imap.select("INBOX"))
    return imap

if __name__ == "__main__":
    connectMailbox()
