import csv
import os

udemy_csv = "./resources/web_starter.csv"
#udemy_csv= os.path.join(".","resources","web_starter.csv")

#with open (udemy_csv, "r") as csvfile:
#   csvreader=csv.reader(csvfile, delimiter=",")
#   test=next(csvreader)
#   print(test)

title=[]
price=[]
subscribers=[]
reviews=[]
reviews_percent=[]
length=[]

with open(udemy_csv,"r",encoding="UTF-8") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
#    test = next(csvreader)
    for row in csvreader:
       
    # We want the title, the price, the subscribers
# reviews, percent of review, length
#add title
        title.append(row[1])
#add price
        price.append(row[4])
#add subscribers
        subscribers.append(row[5])
#reviews
        reviews.append(row[6])
#percent of reviews
        percent=round(int(row[6])/int(row[5]),2)
        reviews_percent.append(percent)
#length
        new_length=row[9].split(" ")
        length.append(float(new_length[0]))

#print(test)
#print(title)
#print(length)
#print(reviews_percent)

cleanCsv=zip(title,price,subscribers,reviews,reviews_percent,length)
outputFile=os.path.join("webFinal.csv")
with open(outputFile,"w",newline="\n") as datafile:
    writer=csv.writer(datafile)
    writer.writerow(["Title", "Course Price","Subscribers", "Revies","Percent of Reviews","Length of Course"])
    writer.writerows(cleanCsv)