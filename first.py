import os
import shutil
import zipfile
import requests
import json
import subprocess



def delety():
    shutil.rmtree('site', ignore_errors=True)

def create_site_folder():
    
    os.makedirs('site', exist_ok=True)

def download_and_extract_zip():
    
    url = ''
    zip_file = 'site/websites.zip'
    response = requests.get(url, stream=True)
    with open(zip_file, 'wb') as f:
        for chunk in response.iter_content(chunk_size=128):
            f.write(chunk)

    
    with zipfile.ZipFile(zip_file, 'r') as zip_ref:
        zip_ref.extractall('site')

    
    os.remove(zip_file)

def delete_validate_files():
    
    for root, dirs, files in os.walk('site'):
        for file in files:
            if file == 'validate.php':
                os.remove(os.path.join(root, file))
#delety()
# Call the functions
#create_site_folder()
#download_and_extract_zip()
#delete_validate_files()

