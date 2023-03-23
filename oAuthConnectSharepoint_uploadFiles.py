#Connect to sharepoint site
# and upload each file in a dir

import os
import requests
from office365.runtime.auth.client_credential import ClientCredential
from office365.sharepoint.client_context import ClientContext
    
def getSharepointContext():
    sharepointUrl = 'https://site.sharepoint.com/site/folder/path'
    clientCredentials = ClientCredential('a79f867e-3138-45de-9cd2-11ccccccccccc', '_vp8Qxxxxxxxt..Andepr3EMyCb_gQppjen8czP')
    ctx = ClientContext(sharepointUrl).with_credentials(clientCredentials)
    targetFolder = ctx.web.get_folder_by_server_relative_url(sharepointUrl)
    #print(targetFolder)
    uploadFiles(targetFolder)

def uploadFiles(targetFolder):
    wd = os.getcwd()
    #source dir ex. projectDir/toUpload
    td = wd+'/toUpload'
    for fn in os.listdir(td):
        f = os.path.join(td, fn)
        if os.path.isfile(f):
            with open(f, 'rb') as k:
                file_content = k.read()
                targetFolder.upload_file(k, file_content).execute_query()

# check a folder for contents to upload
def checkUploadFolder():
    workingDir = os.getcwd()
    if len(os.listdir(workingDir+'/toUpload')) == 0:
        return
    else:
        getSharepointContext()
    
    
    
if __name__ == "__main__":
    #checkUploadFolder()
    getSharepointContext()
