import codecs
import requests
import ftfy
import w3lib.html
import csv
import pandas as pd
from pyparsing import replace_html_entity

#Search with every element in a list =================================================================
def searchByList(keywordList: list):
    for keyword in keywordList:
        search(keyword)

#Search with multiple of arguments ===================================================================
def searchByArgs(*args):
    for arg in args:
        search(arg)

#Search keyword on Google and write to a new html file. UTF-8 Encoding and replace HTML entities =====
def search(keyword: str):
    keyword = keyword.replace(' ', '+')
    url = 'https://www.google.com/search?q=' + keyword
    htmlOutputName = keyword + '.html'

    req = requests.get(url, 'html.parser')

    with codecs.open(htmlOutputName, 'w', "utf-8") as f: #UTF-8 Encoding
        htmlOutputContent = w3lib.html.replace_entities(req.text) #Replace HTML entities
        f.write(htmlOutputContent)
        print(htmlOutputName + ' was created successfully!')
    
    html_processor(keyword + '.html')

#Process the html file and write to a new CSV file ===================================================
def html_processor(htmlFileName: str):
    #Open and read html file: ---------------------------------------------------------
    fileData = ''
    with codecs.open(htmlFileName, 'r', 'utf-8') as f: #UTF-8 Encoding
        fileData = f.read()
        print(htmlFileName + ' was read successfully!')

    #Detach data: ---------------------------------------------------------------------
    data = {
        "WebTitle": [],
        "WebDomain": [],
        "WebDir": []
    }
    #class="Gx5Zad fP1Qef xpd EtOod pkphOe" (Search results):
    htmlClass0 = '<div class="Gx5Zad fP1Qef xpd EtOod pkphOe">'
    class0List = fileData.split(htmlClass0)
    for i in range(1, len(class0List)-1):
        #class="BNeawe vvjwJb AP7Wnd" (Website name) AND MUST RETREIVE FROM INDEX 1:
        class1List = class0List[i].split('<div class="BNeawe vvjwJb AP7Wnd">')
        class1List.pop(0)
        class1 = class1List[0]
        class1 = class1.split('</div>')[0]
        #class="BNeawe UPmit AP7Wnd" (Website URL):
        class2List = class1List[0].split('<div class="BNeawe UPmit AP7Wnd">')
        class2List.pop(0)
        class2 = class2List[0]
        class2 = class2.split('</div>')[0]
        #class="BNeawe s3v9rd AP7Wnd" (Description):
        #...

        data["WebTitle"].append(class1)
        data["WebDomain"].append(class2.split(' › ')[0])
        data["WebDir"].append(class2)
    
    #Write to a new CSV file: -----------------------------------------------------------
    df = pd.DataFrame(data)
    df.to_csv(htmlFileName.replace('.html', '.csv'), index=False)
    print(htmlFileName + ' was created successfully!')

def main():
    #TYPE KEYWORDS TO SEARCH ON GOOGLE!
    keywordList = [
        'python', 
        'hóa dược', 
        'công nghệ thông tin', 
        'bill gates', 
        'shopee', 
        '2022', 
        '3d', 
        'đồ họa máy tính', 
        'timpani'
        ]

    #Do the processing
    searchByList(keywordList)
    
    #Read from CSV file
    for keyword in keywordList:
        df = pd.read_csv(keyword.replace(' ','+') + '.csv')
        print('\n===== Google results for: {} ====='.format(keyword))
        print(df)
        print()

if __name__ == '__main__':
    main()