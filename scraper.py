# This is a template for a Python scraper on morph.io (https://morph.io)
# including some code snippets below that you should find helpful
#sudo service morph restart
import scraperwiki
import lxml
import urlparse
import urllib2
#import mechanize
import requests
import lxml.html
import sqlite3
import time
import sys
import csv



sys.setrecursionlimit(10000)

#counties = ['adair','alfalfa','appellate','atoka','beaver','beckham','blaine','bryan','caddo','canadian','carter','cherokee','choctaw','cimarron','cleveland','coal','comanche','cotton','craig','creek','bristow','drumright','custer','delaware','dewey','ellis','garfield','garvin','grady','grant','greer','harmon','harper','haskell','hughes','jackson','jefferson','johnston','kay','poncacity','kingfisher','kiowa','latimer','leflore','lincoln','logan','love','major','marshall','mayes','mcclain','mccurtain','mcintosh','murray','muskogee','noble','nowata','okfuskee','oklahoma','okmulgee','henryetta','osage','ottawa','payne','pawnee','pittsburg','pontotoc','pottawatomie','pushmataha','rogermills','rogers','seminole','sequoyah','stephens','texas','tillman','tulsa','wagoner','washington','washita','woods','woodward']
counties = ['tulsa']
#next_link = 0
years = ['2011','2012','2013','2014','2015','2016','2017']
CrimeSeverity = ['CF','CM']

def CaseEndingNumbers():
    for x in range(39, 7110):
        yield '%d' % x
        

def GetOklahomaStateCases():
    for county in counties:
        for CaseEndingNumber in ListOfCaseEndingNumbers:
            for year in years:
                for severity in CrimeSeverity:
                    yield 'http://www.oscn.net/dockets/GetCaseInformation.aspx?db=%s&number=%s-%s-%s' % (county, severity, year, CaseEndingNumber)

def scrape_table(root):
    #create a record to hold the data
    record = {}
    #grab all table rows <tr> in table class="tblSearchResults"
    rows = root.cssselect("table.caseStyle tr")
    #for each row, loop through this
    for row in rows:
        #create a list of all cells <td> in that row
        table_cells = row.cssselect("td")
        if table_cells: 
        #if there is a cell, record the contents in our dataset, the first cell [0] in 'recipient' and so on
            Case_Style = table_cells[0].text_content()
            #print Case_Style
            record['Case Style'] = table_cells[0].text_content()
            record['Date Filed and Judge'] = table_cells[1].text_content()
            #record['Case Number'] = table_cells[0].strong.text_content()
            #this line adds 1 to the ID no. we set at 0 earlier
            #idno=idno+1
            #record['ID'] = idno 
            print record, '------------'
        counts = root.cssselect("div.CountsContainer")
        countstotal = len(counts)
        print "total number of counts:", countstotal
        #countsrange = range(0, countstotal+1)
        #for count in countsrange:
        id=0
        for count in counts:
            id+=1
            if counts: 
                record['Count'+str(id)] = count.text_content()
            '''rows = count.cssselect('div.CountsContainer tr')
            if rows:
                id = 0
                #rowstotal = len(rows)
                #rowsrange = range(0,rowstotal+1)
                #create a record to hold the data
                #record = {}
                #for each row, loop through this
                #for rownum in rowsrange:
                for row in rows:
                    id + 1 
                    record["'Count'+str(id)"] = row[1].text_content()
                    #record['Count'+str(id)+'as disposed:'] = row[2].text_content()
                    #print "scraping row", rownum
                    #create a list of all cells <td> in that row
                    table_cells = row.cssselect("td")
                    if table_cells:
                    #print table_cells
                        record['Charges'] = table_cells[0].text_content()
                        record['Count Description:'] = table_cells[1].text_content()
                        record['Outcome:'] = table_cells[-1].text_content()
                        print record, '------------'
                        # Save the record to the datastore - 'ID' is our unique key - '''
    print 'ALL DATA:', record
    scraperwiki.sqlite.save(unique_keys=['Date Filed and Judge'], data=record)
    '''record = {k: unicode(v).encode("utf-8") for k,v in record.iteritems()}
    with open('OklahomaCasesTest.csv', 'wb') as csv_file:
        writer = csv.writer(csv_file)
        for key, value in record.items():
            writer.writerow([key, value])
    #data.to_csv("/Users/Lucia/Documents/Coding/OklahomaCases.csv")'''
           
            

def scrape_and_look_for_next_link(url):
    #html = scraperwiki.scrape(url)
    page = requests.get(url)
    html = page.content
    #print html
    root = lxml.html.fromstring(html)
    scrape_table(root)
    #CaseEndingNumber += 1
    global i
    i = (i + 1)
    if i < 450:
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if i == 450:
        time.sleep(65)
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if 450 < i < 900:
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if i == 900:
        time.sleep(65)
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if 900 < i < 1350:
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if i == 1350:
        time.sleep(65)
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if 1350 < i < 1800:
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if i == 1800:
        time.sleep(65)
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if 1800 < i < 2250:
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if i == 2250:
        time.sleep(65)
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if 2250 < i < 2700:
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if i == 2700:
        time.sleep(65)
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if 2700 < i < 3150:
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if i == 3150:
        time.sleep(65)
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if 3150 < i < 3600:
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if i == 3600:
        time.sleep(65)
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if 3600 < i < 4050:
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if i == 4050:
        time.sleep(65)
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    if 4050 < i < 4500:
        next_url = ListofOKCases[i]
        print next_url
        record = {}
        record['URL'] = next_url
        scraperwiki.sqlite.save(['URL'], record)
        scrape_and_look_for_next_link(next_url)
    
           
        
        
# ---------------------------------------------------------------------------
# START HERE: define your starting URL - then 
# call a function to scrape the first page in the series.
# ---------------------------------------------------------------------------
base_url = 'http://www.oscn.net/dockets/'
starting_url = urlparse.urljoin(base_url, 'GetCaseInformation.aspx?db=garfield&number=CF-2011-1')
print starting_url
global i
i = 1
#for i in range(0,1):
    #There are 743 cases but 468 appears to be the server request limit
CaseEndingNumbers()
ListOfCaseEndingNumbers = list(CaseEndingNumbers())
GetOklahomaStateCases()
ListofOKCases = list(GetOklahomaStateCases())
scrape_and_look_for_next_link(starting_url)     
    
    
# # Read in a page
# html = scraperwiki.scrape("http://foo.com")
#
# # Find something on the page using css selectors
# root = lxml.html.fromstring(html)
# root.cssselect("div[align='left']")
#
# # Write out to the sqlite database using scraperwiki library
# scraperwiki.sqlite.save(unique_keys=['name'], data={"name": "susan", "occupation": "software developer"})
#
# # An arbitrary query against the database
# scraperwiki.sql.select("* from data where 'name'='peter'")

# You don't have to do things with the ScraperWiki and lxml libraries.
# You can use whatever libraries you want: https://morph.io/documentation/python
# All that matters is that your final data is written to an SQLite database
# called "data.sqlite" in the current working directory which has at least a table
# called "data".
