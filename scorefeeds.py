import feedparser

Leagues={"Bundesliga":"http://rss.kicker.de/live/bundesliga","2.Bundesliga":"http://rss.kicker.de/live/2bundesliga",
        "DFB-Pokal":"http://rss.kicker.de/live/dfbpokal","Premier League":"http://rss.kicker.de/live/premierleague",
        "England Championship":"http://rss.kicker.de/live/thecocacolafootballleaguechampionship",
        "France":"http://rss.kicker.de/live/ligue1orange","Italy":"http://rss.kicker.de/live/serieatim",
        "Netherlands":"http://rss.kicker.de/live/eredivisie","Scotland":"http://rss.kicker.de/live/schottland",
        "Spain":"http://rss.kicker.de/live/primeradivision", "News": "http://rss.kicker.de/news/aktuell","Switzerland": "http://rss.kicker.de/live/axposuperleague"}

league_list = [i for i in Leagues]
def scores(league):
    res=''
    feed=feedparser.parse(league)
    for i in feed['entries']:
        res += i.get('title') + '\n'
    return res

def description(league):
    res = ''
    feed = feedparser.parse(league)
    for i in feed['entries']:
        res += i.get('title') + '\n'
        res += i.get('description') + '\n\n'
    return res



