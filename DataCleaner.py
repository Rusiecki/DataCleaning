# coding=utf-8


import pandas as pd
import string
import numpy as np
import random


input_file  = pd.read_csv("input.csv", error_bad_lines=False, low_memory=False, skiprows=0, usecols=[3,4])
output_file = "output.csv"

#
# Done repair iterating loop
# ToDo Writing dataframe to CSV
# Done Array to String
# Todo Count False / True lables for small (300-400) and big models
# Workaround Figure out dataframe -> lamda

# ToDo the Quote Cleaner needs to be accessed first otherwise there will be a massive problem in deleting the actual quote
# ToDo Problem in data cleaning : lastname schrieb am date time <- works
# ToDo But : surname lastname schrieb am date time <- does not work. need to find a cleaner work around
# ToDo Workaround check if after " schrieb am " <- put this first. than comes the cleaning

# 12/14 2.5 s

###
# confusion matrix
# prediction csv
# preprocessing
#


def getrows(file):
    end = len(file)
    return end


# open CSV file

def input(file):
    #try:
        # skip first line / 0 = index /   3 = content / 4 = deleted
        content_ = pd.DataFrame(file)
        processing(content_)
    #except:
     #   print("error reading data")


def processing(data):
    nor = len(data)
    processedData = replaceWords(data, nor)
    processedData = str(processedData)
    print (processedData)



def replaceWords(string, row):
    blackList = ["greetz", "[quote]", "[/quote]", "edge", "\\n", "\\r", "*", "\""]
    bl = len(blackList)
    for x in range(0, row):
        quoteCleaner(string)
        dataString = str(string.iloc[x])
        for y in range (0, bl):
            dataString = dataString.replace(blackList[y], "")
        print(dataString)
    return(dataString)


def timeChecker(string):
    time = str(string)
    len(time)
    print(time)
    if(time.find(":\\") != -1 and len(time) >= 15 ):
        print("found time")
        time = time.replace("\\r\\n\\", "")
        time = time.replace("")
        print("New String : " + time)

def dateChecker(string):
    date = str(string)
    len(date)
    if(date.find(".") != -1 and len(date) == 10 ):
        print("found date")


"""hurghada schrieb am 23.11.2017 20:49:\r\n\r\n[quote]\r\nMan kommt gar nicht auf die Idee - unter neuen, veränderten Bedingungen! - das Volk neu zu befragen. Des Volkes Meinung könnte der Demokratie mit ihren bewährten Institutionen - siehe oben! - zuwiderlaufen ...\r\n[/quote]\r\n\r\nDas Volk kann doch gar nicht die wirklichen Umstände beurteilen da man sie ihn vorenthält, selbst Willy Brandt (Pseudonym) war überrascht als er Kanzler wurde wie die wirklichen Machtverhältnisse liegen.\r\n\r\nDiese vermaledeite Volk könnte eine Regierung aus einer Koalition kleinerer Parteien injizieren, das muss auf jeden Fall verhindert werden, den so eine Regierung würde sich nicht an die 'Gott gewollten' Umstände halten und zuviel offen legen was der Pöbel nie verstehen würde."""

def quoteCleaner(comment):
    containsQuote = False
    myComment = str(comment)
    quoteBegin = ":\r\n\r\n[quote]\r\n"
    quoteEnd = "\\r\\n[/quote]\\r\\n\\r\\n"
    y = myComment.find(quoteBegin)
    x = myComment.find(quoteEnd)
    # get index of x = :\r\n\r\n[quote]\r\n
    # get index of y = \r\n[/quote]\r\n\r\n
    # delete everything between character 0 and y
    # done

    # later we need to check if the next word is a date + time if so we need to delete the name in front of "schrieb am" if there is still a word left kill that too
    if(myComment.find(" schrieb am ") != -1):
        print("entering QuoteCleaner")
        # find gives me the position of "s"chrieb
        containsQuote = True
        myComment = myComment.split(' ')
        schriebIndex = myComment.index("schrieb")
        # dd.mm.yyyy HH:MM:SS
        isDate = myComment[schriebIndex+2] # check if that is date
        isTime = myComment[schriebIndex+3] # check if that is time
        #print(myComment[schriebIndex+3])
        dateChecker(isDate)
        timeChecker(isTime)
        if(schriebIndex == (myComment.index("")+1)):
            print("certainly quote that needs to be deleted")




    if(containsQuote == False):
        return(comment)
    else:
        return(myComment)



def toArrayString(string): # deprecated
    # if sentence contains "schrieb, am Datum Uhrzeit"
    stringArray =  string.split(' ')
    if( stringArray[1] == "schrieb" and stringArray[2] == "am"):
        stringArray[4] = ""
        stringArray[3] = ""
        stringArray[2] = ""
        stringArray[1] = ""
        stringArray[0] = ""
        stringArray = " ".join(stringArray)
        stringArray = stringArray[5:]
        print("replacing: x schrieb, am")
        return stringArray
    else:
        stringArray = " ".join(stringArray)
        return stringArray




# write New CSV file
def writeData(data):
    # write new csv file
    print("Writing to new CSV_file")
    print(data)
    try:
        data.to_csv(file_name, sep='\t')
    except:
        print("error Writing CSV FILE")
    #data.to_csv('output_file.csv')
    # if column is not empty take next column




input(input_file)

#iterrows(input_file)
