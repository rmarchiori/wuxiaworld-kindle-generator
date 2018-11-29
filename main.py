import requests
from bs4 import BeautifulSoup

urlHome = 'https://www.wuxiaworld.com'
urlNovel = '/novel/against-the-gods'
volumesInput = ['9']

responseMainPage = requests.get(urlHome + urlNovel)

if responseMainPage.status_code != 200:
    sys.exit()

soup = BeautifulSoup(responseMainPage.content, 'html.parser')

volumes = soup.findAll('span', {'class': 'book'})

selectedVolumes = [v for v in volumes if v.text in volumesInput]

for v in selectedVolumes:
    h4PanelTitle = v.parent
    divPanelHeading = h4PanelTitle.parent
    divPanelDefault = divPanelHeading.parent
    divChapters = divPanelHeading.findNext('div')
    linksChapters = divChapters.findAll('a')
    for linksChapter in linksChapters:
        linkChapter = linksChapter.attrs['href']
        titleChapter = linksChapter.text
        urlChapter = urlHome + linkChapter
        print('linkChapter: ' + linkChapter)
        print('titleChapter: ' + titleChapter)
        print('urlChapter: ' + urlChapter)

        responseChapter = requests.get(urlChapter)

        if responseChapter.status_code != 200:
            sys.exit()

        soupChapter = BeautifulSoup(responseChapter.content, 'html.parser')

        divTextChapter = soupChapter.find('div', {'class':'fr-view'})
        pTextChapter = divTextChapter.findAll('p')
        textChapter = ''

        for p in pTextChapter:
            textChapter += p.text

        print('e')


    

print ('end')
