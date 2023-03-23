import oAuthConnect
import imaplib
import msal

def acquireToken():
  app = msal.ConfidentialClientApplication(
      #app id
      'a79f867e-3138-45de-9cd2-xxxxxxxxxfe3',
      authority='https://login.microsoftonline.com/c6d01ab1-3b9a-4f65-acdd-xxxxxxx9dd',
      #secret
      client_credential='_vp8Q~05OeJNDt..Andepr3EMyCb_xxxxxxxxxP'
  )
  result = app.acquire_token_for_client(scopes=['https://outlook.office365.com/.default'])
  return result

def generate_auth_string(user, token):
    return 'user=%s\1auth=Bearer %s\1\1' % (user, token)

def connectMailbox():
    token = acquireToken()
    mailserver = 'outlook.office365.com'
    mailBox = 'noco@eco-maxx.com'
    imapport = 993
    imap = imaplib.IMAP4_SSL(mailserver,imapport)
    imap.debug = 4
    imap.authenticate('XOAUTH2', lambda x: generate_auth_string(mailBox, token['access_token']))
    
    #print(token)
    #print(imap.list())
    #print(imap.select("INBOX"))
    #if(token['access_token']):
    return imap

if __name__ == "__main__":
    connectMailbox()
