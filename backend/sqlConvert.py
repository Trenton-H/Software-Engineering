import sqlite3
conn = sqlite3.connect('carData.db')
c = conn.cursor()

#creates table
c.execute('''Create TABLE if not exists carTable (year text, make text, model text)''')

#forms lists
#yearList = list()
#makeList = list()
#modelList = list()
ymmList = list()

with open ('data.sql', 'r') as rf:
    for cnt, line in enumerate(rf):
        if cnt > 0:
            ymmList.append(line[1:5],)
            endVal = '\''
            charCount = 8
            while line[charCount] != '\'':
                charCount = charCount + 1
            ymmList.append(line[8:charCount])
            beginCount = charCount + 4
            endCount = beginCount
            while line[endCount] != '\'':
                endCount = endCount + 1
            ymmList.append(line[beginCount:endCount])


#moves lists to database

def data_entry(input = []):
    i = 1
    yearInput = "NULL"
    makeInput = "NULL"
    modelInput = "NULL"
    for data in input:
        if i % 3 == 1:
            modelInput= input.pop()
            i = i+1
        elif i % 3 == 2:
            makeInput = input.pop()
            i = i+1
        else:
            yearInput= input.pop()
            i = i+1
            c.execute("INSERT INTO carTable VALUES(?,?,?)", (yearInput,makeInput,modelInput))

    
data_entry(ymmList)
conn.commit()

c.execute("SELECT * FROM carTable")
rows = c.fetchall()
for row in rows:
    print(row)

conn.close()

#x = 0
#while len(yearList) != 0:
#    year = yearList.pop(x)
#    c.execute("SELECT * FROM carTable WHERE year = '%s'" % year)
#    x = x + 1
