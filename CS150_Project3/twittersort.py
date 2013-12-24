import sys
from scanner import Scanner

TWEETER = 0
TWEET = 1
YEAR = 2
MONTH = 3
DAY = 4
TIME = 5

def main():
    print("Reading files...")

    fileName1 = sys.argv[1]
    fileName2 = sys.argv[2]
    tweets1 = readTable(fileName1)
    tweets2 = readTable(fileName2)

    if len(tweets1) > len(tweets2):
        print(fileName1, "contained the most tweets with", len(tweets1), ".")
    elif len(tweets1) < len(tweets2):
        print(fileName2, "contained the most tweets with", len(tweets2), ".")
    else:
        print("Both", fileName1, "and", fileName2, "contained the equal number of tweets with", len(tweets1), ".")

    print("Merging files...")
    mergedTweets = merge(tweets1, tweets2)

    print("Writing files...")
    writeOutputFile(mergedTweets)

    print("Files Written. Displaying 5 earliest tweeters and tweets.")
    for record in mergedTweets[:5]:
        print(record[TWEETER], record[TWEET])


def readTable(filename):
    s = Scanner(filename)
    table = []
    record = readRecord(s)
    while record != "":
        table.append(record)
        record = readRecord(s)
    s.close()
    return table

def readRecord(s):
    tweeter = s.readtoken()
    if tweeter == "":
        return ""
    tweeter = tweeter[1:]
    tweet = s.readstring()
    year = s.readint()
    month = s.readint()
    day = s.readint()
    time = s.readtoken()

    result = [0, 0, 0, 0, 0, 0]
    result[TWEETER] = tweeter
    result[TWEET] = tweet
    result[YEAR] = year
    result[MONTH] = month
    result[DAY] = day
    result[TIME] = time

    return result

def merge(array1, array2):
    array3 = []
    i = 0
    j = 0
    while i < len(array1) and j < len(array2):
        # If Record1 is recent add record 1 to result array
        if isRecord1Recent(array1[i], array2[j]):
            array3.append(array1[i])
            i += 1
        # Else add record 2 to result array
        else:
            array3.append(array2[j])
            j += 1

    return array3 + array1[i:] + array2[j:]

def isRecord1Recent(record1, record2):
    if record1[YEAR] > record2[YEAR]:
        return True
    if record1[YEAR] < record2[YEAR]:
        return False
    if record1[MONTH] > record2[MONTH]:
        return True
    if record1[MONTH] < record2[MONTH]:
        return False
    if record1[DAY] > record2[DAY]:
        return True
    if record1[DAY] < record2[DAY]:
        return False
    if record1[TIME][0:2] > record2[TIME][0:2]:
        return True
    if record1[TIME][0:2] < record2[TIME][0:2]:
        return False
    if record1[TIME][3:5] > record2[TIME][3:5]:
        return True
    if record1[TIME][3:5] < record2[TIME][3:5]:
        return False
    if record1[TIME][6:8] > record2[TIME][6:8]:
        return True
    if record1[TIME][6:8] < record2[TIME][6:8]:
        return False
    return True

def writeOutputFile(mergedTweets):
    out = open("output.txt", "w")
    for record in mergedTweets:
        out.write(record[TWEETER] + "\t")
        out.write(record[TWEET] + "\t")
        out.write(str(record[YEAR]) + " ")
        out.write(str(record[MONTH]) + " ")
        out.write(str(record[DAY]) + " ")
        out.write(record[TIME] + "\n")

    out.close()

if __name__ == '__main__':
    main()