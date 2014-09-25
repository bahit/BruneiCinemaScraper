import scraperwiki
import requests
import lxml.html
import re
import datetime as dt
from datetime import datetime

## TODO
## Second date for Mall movie listing (pull down) not yet implemented
## Soldout time not implemented - class="ShowtimesSessionSoldOutLink"

mallDOM = lxml.html.fromstring(requests.get("http://mall-ticket.com").content)

mall = mallDOM.cssselect('.ShowtimesSummaryRow')

mallAlt = mallDOM.cssselect('.ShowtimesSummaryRowAlt')


## Times Cineplex
timecineplexDOM = lxml.html.fromstring(requests.get("http://timescineplex.com/schedule/").content)

timescineplex = timecineplexDOM.cssselect('.schedule')

counter = 0
idCount = 0

# Now there is a way to get all dates available on Mall Cineplex website
# Using lxml form submission
# The Mall Cineplex website uses javascript to POST to the server different dates
# This requires changing the option field for the drop down menu to change the dates
# The dates are limited and random in number (eg. showing 2 days or more but not consistent)
# Documentation: http://lxml.de/lxmlhtml.html#forms

# First find the available values from the options, I.E the dates that are available

## Prefixing Mall's Date
mallDate = mallDOM.cssselect('.ShowtimesFilterDropDownList')

# We don't know the exact dates available, so available dates can be found using:
# 4/1/2014 Found out that days = len(mallDate) isn't correct, turns out
# it returns a list of 'ddlFilterDate' & 'ddlFilterCinema' - perhaps new update from the
# website thus should be len(mallDate[0])
days = len(mallDate[0])

# Below used for taking current date to be used in the db
currentMallDate1 = (mallDate[0][0].get('value')).split('/')

currentMallDate = dt.date(int(currentMallDate1[2]), int(currentMallDate1[0]), int(currentMallDate1[1]))

# Save data

for i in mall:
    ## Below contains the word "Blockbuster" in movie title name, need to remove them
    movieTitle = ' '.join(mall[counter][0][0][1].text_content().split())
    movieTitle = movieTitle[:movieTitle.find('Blockbuster')]

    runningTime = re.sub("[^0-9]", "", ' '.join(mall[counter][0][0][2].text_content().split()))

    showTime = ' '.join(mall[counter][0][0][3].text_content().split())

    data = {
        'table_id': idCount,
        'cinema_id': 'mall',
        'movie_title': movieTitle,
        'movie_poster': 'null',
        'runningTime': runningTime,
        'showDate1': currentMallDate.strftime('%d %b %Y'),
        'showDate2': 'null',
        'showDate3': 'null',
        'showDate4': 'null',
        'showDate5': 'null',
        'showDate6': 'null',
        'showDate7': 'null',
        'showTimeDay1': showTime,
        'showTimeDay2': 'null',
        'showTimeDay3': 'null',
        'showTimeDay4': 'null',
        'showTimeDay5': 'null',
        'showTimeDay6': 'null',
        'showTimeDay7': 'null'
    }
    idCount += 1
    counter += 1

    scraperwiki.sqlite.save(unique_keys=['table_id'], data=data)

print "Finished Mall"

counter = 0

for i in mallAlt:
    ## Below contains the word "Blockbuster" in movie title name, need to remove them
    movieTitle = ' '.join(mallAlt[counter][0][0][1].text_content().split())
    movieTitle = movieTitle[:movieTitle.find('Blockbuster')]

    runningTime = re.sub("[^0-9]", "", ' '.join(mallAlt[counter][0][0][2].text_content().split()))
    showTime = ' '.join(mallAlt[counter][0][0][3].text_content().split())

    data = {
        'table_id': idCount,
        'cinema_id': 'mall',
        'movie_title': movieTitle,
        'movie_poster': 'null',
        'runningTime': runningTime,
        'showDate1': currentMallDate.strftime('%d %b %Y'),
        'showDate2': 'null',
        'showDate3': 'null',
        'showDate4': 'null',
        'showDate5': 'null',
        'showDate6': 'null',
        'showDate7': 'null',
        'showTimeDay1': showTime,
        'showTimeDay2': 'null',
        'showTimeDay3': 'null',
        'showTimeDay4': 'null',
        'showTimeDay5': 'null',
        'showTimeDay6': 'null',
        'showTimeDay7': 'null'
    }
    idCount += 1
    counter += 1

    scraperwiki.sqlite.save(unique_keys=['table_id'], data=data)

print "Finished Mall Alt"

# # Parsing different dates found on Mall website
# while (days):
#     # mallDOM.forms[0] # contains the only form from mall website
#     mallDOM.forms[0].fields["ddlFilterDate"] = mallDate[0][days-1].get('value')
#     # seems like the field __EVENTTARGET does not exist before sending the form
#     # using extra_values instead
#     # mallDOM.forms[0].fields["__EVENTTARGET"] = "ddlFilterDate"
#     extra_values = {'__EVENTTARGET': "ddlFilterDate"}
#     futureMallDOM = parse(submit_form(page.forms[0])).getroot()

#     mall2 = futureMallDOM.cssselect('.ShowtimesSummaryRow')

#     mallAlt2 = futureMallDOM.cssselect('.ShowtimesSummaryRowAlt')

#     days -= 1




counter = 0

for i in timescineplex:

    movieTitle = timescineplex[counter][1].text_content()[:(timescineplex[counter][1].text_content()).find('\n')]
    runningTime = ""
    moviePoster = timescineplex[counter][0][0][0].get('src')

    ## running time prefix
    ## There are three possibilities:
    ## (1:33hrs)
    ## (91 min)
    ## (2 hours 11 minutes)

    line = timescineplex[counter][1][0].text_content()[(timescineplex[counter][1][0].text_content()).find('(')+1:(timescineplex[counter][1].text_content()).find(')')]
    k = re.findall(r'\d+', line)

    ## Returns a list ['1' ,'33']

    if len(k) == 2:

        runningTime = (int(k[0]) * 60 + int(k[1]))

    if len(k) == 1:

        runningTime = (int(k[0]))

    showDate1 = datetime.strptime(timescineplex[counter][2][0][0][0][0].text_content()[timescineplex[counter][2][0][0][0][0].text_content().find('-')+2:]+" "+datetime.now().strftime('%Y'), "%b %d %Y")
    showDate2 = datetime.strptime(timescineplex[counter][2][0][0][1][0].text_content()[timescineplex[counter][2][0][0][1][0].text_content().find('-')+2:]+" "+datetime.now().strftime('%Y'), "%b %d %Y")
    showDate3 = datetime.strptime(timescineplex[counter][2][0][0][2][0].text_content()[timescineplex[counter][2][0][0][2][0].text_content().find('-')+2:]+" "+datetime.now().strftime('%Y'), "%b %d %Y")
    showDate4 = datetime.strptime(timescineplex[counter][2][0][0][3][0].text_content()[timescineplex[counter][2][0][0][3][0].text_content().find('-')+2:]+" "+datetime.now().strftime('%Y'), "%b %d %Y")
    showDate5 = datetime.strptime(timescineplex[counter][2][0][0][4][0].text_content()[timescineplex[counter][2][0][0][4][0].text_content().find('-')+2:]+" "+datetime.now().strftime('%Y'), "%b %d %Y")
    showDate6 = datetime.strptime(timescineplex[counter][2][0][0][5][0].text_content()[timescineplex[counter][2][0][0][5][0].text_content().find('-')+2:]+" "+datetime.now().strftime('%Y'), "%b %d %Y")
    showDate7 = datetime.strptime(timescineplex[counter][2][0][0][6][0].text_content()[timescineplex[counter][2][0][0][6][0].text_content().find('-')+2:]+" "+datetime.now().strftime('%Y'), "%b %d %Y")

    showTimeDay1 = ' '.join(timescineplex[counter][2][0][0][0][1].text_content().replace("|", "").split())
    showTimeDay2 = ' '.join(timescineplex[counter][2][0][0][1][1].text_content().replace("|", "").split())
    showTimeDay3 = ' '.join(timescineplex[counter][2][0][0][2][1].text_content().replace("|", "").split())
    showTimeDay4 = ' '.join(timescineplex[counter][2][0][0][3][1].text_content().replace("|", "").split())
    showTimeDay5 = ' '.join(timescineplex[counter][2][0][0][4][1].text_content().replace("|", "").split())
    showTimeDay6 = ' '.join(timescineplex[counter][2][0][0][5][1].text_content().replace("|", "").split())
    showTimeDay7 = ' '.join(timescineplex[counter][2][0][0][6][1].text_content().replace("|", "").split())

    data = {
        'table_id': idCount,
        'cinema_id': 'timescineplex',
        'movie_title': movieTitle,
        'movie_poster': moviePoster,
        'runningTime': runningTime,
        'showDate1': showDate1.strftime('%d %b %Y'),
        'showDate2': showDate2.strftime('%d %b %Y'),
        'showDate3': showDate3.strftime('%d %b %Y'),
        'showDate4': showDate4.strftime('%d %b %Y'),
        'showDate5': showDate5.strftime('%d %b %Y'),
        'showDate6': showDate6.strftime('%d %b %Y'),
        'showDate7': showDate7.strftime('%d %b %Y'),
        'showTimeDay1': showTimeDay1,
        'showTimeDay2': showTimeDay2,
        'showTimeDay3': showTimeDay3,
        'showTimeDay4': showTimeDay4,
        'showTimeDay5': showTimeDay5,
        'showTimeDay6': showTimeDay6,
        'showTimeDay7': showTimeDay7
    }
    idCount += 1
    scraperwiki.sqlite.save(unique_keys=['table_id'], data=data)

    counter += 1

print "Finished Times Cineplex"

    # print movieTitle
    # print runningTime
    # print showTime
    # print " "
# ## Mall Movie Details
# title = mall[0][0][0][1].text_content().split()
# runningTime = mall[0][0][0][2].text_content().split()
# showTime = mall[0][0][0][3].text_content().split()
