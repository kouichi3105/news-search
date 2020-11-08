from bs4 import BeautifulSoup
import requests

file = "HybridIT.txt"
f = open(file, "w", encoding='utf-8')

title_data = dict()
titleList = list()

res = requests.get('https://cloud.watch.impress.co.jp/')
res.raise_for_status()
soup = BeautifulSoup(res.text, "html.parser")
titles = soup.select('.title a')

for title in titles:
    title_data = dict()
    title_data["title"] = title.getText()
    title_data["URL"] = title.get('href')
    title_data["content"] = None
    titleList.append(title_data)

for i in range(len(titleList)):
    link = titleList[i]["URL"]
    
    if 'https' in link:
        print(link)
        print(titleList[i]["title"])
        title = titleList[i]["title"]
        html = requests.get(link)
        soup = BeautifulSoup(html.text, "html.parser")
        
        contents = soup.select('.main-contents.mainContents')
        for content in contents:
            if 'ハイブリッド' in content.text:
                print("------------")
                print("ハイブリッド")
                print("------------")
                f.write(title + "\n")
                f.write(link + "\n")
                f.write("\n")

    else:
        link = 'https://cloud.watch.impress.co.jp/' + link
        print(link)
        print(titleList[i]["title"])
        title = titleList[i]["title"]
        html = requests.get(link)
        soup = BeautifulSoup(html.text, "html.parser")

        contents = soup.select('.main-contents.mainContents')
        contentsList = list()
        for content in contents:
            if 'ハイブリッド' in content.text:
                print("------------")
                print("ハイブリッド")
                print("------------")
                f.write(title + "\n")
                f.write(link + "\n")
                f.write("\n")


