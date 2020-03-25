import bs4 as BeautifulSoup
import urllib.request


sourcePage = "https://www.metrolyrics.com/drake-alpage-"
sourcePageEnding = ".html"
pages = 7
exportfile = open("LyricsGeneratorFlask/static/LyricsGenerator_pkg/g=drakeLyrics.txt","w+")



def getAllLinks(numOfPages):
    linklist = list()
    #Navigates between  all pages of the site
    for i in range (0, numOfPages + 1):
        source = urllib.request.urlopen(sourcePage + str(i) + sourcePageEnding)
        soup = BeautifulSoup.BeautifulSoup(source, "html.parser")
        links = soup.find_all("a", attrs={"class":"title hasvidtable"})
        #gets the links to the lyrics page for every song
        for item in links:
            x = item.get('href', None)
            #excludes songss that drake is featured in
            if x !="https://www.metrolyrics.com/sicko-mode-lyrics-travis-scott.html"  and x != "https://www.metrolyrics.com/work-lyrics-rihanna.html" and x != "https://www.metrolyrics.com/yes-indeed-lyrics-lil-baby.html" and x != "https://www.metrolyrics.com/bedrock-lyrics-lil-wayne.html" and x != "https://www.metrolyrics.com/whats-my-name-lyrics-rihanna.html" and x != "https://www.metrolyrics.com/only-lyrics-nicki-minaj.html" and x != "https://www.metrolyrics.com/unthinkable-lyrics-alicia-keys.html" and x != "https://www.metrolyrics.com/moment-for-life-lyrics-nicki-minaj.html" and x != "https://www.metrolyrics.com/walk-it-talk-it-lyrics-migos.html" and x != "https://www.metrolyrics.com/im-on-one-lyrics-dj-khaled.html" and x != "https://www.metrolyrics.com/come-and-see-me-lyrics-party-next-door.html" and x != "https://www.metrolyrics.com/moment-4-life-lyrics-nicki-minaj.html" and x != "https://www.metrolyrics.com/truffle-butter-lyrics-nicki-minaj.html" and x != "https://www.metrolyrics.com/im-goin-in-lyrics-lil-wayne.html":
                linklist.append(x)
    return linklist

def songPageToLyrics(website):
    source = urllib.request.urlopen(website)
    soup = BeautifulSoup.BeautifulSoup(source, 'html.parser')
    #Add all verse containers to the text file for a specific song
    lyrics = soup.find_all("p", attrs={"class": "verse"})
    lyricsText = ""
    for i in lyrics:
         current = i.text.strip()
         lyricsText +=  current

    exportfile.write(lyricsText)


for current_link in getAllLinks(7):
    songPageToLyrics(current_link)
exportfile.close()