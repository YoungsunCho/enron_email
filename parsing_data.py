import os
import csv

def open_csv_file():
    csv_file = open('data.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(csv_file)
    return (csv_file, wr)

def close_csv_file(csv_file):
    csv_file.close()

def parsing(filename,wr):
    file = open(filename, 'r')
    dic = {}

    while True:
        line = file.readline()
        if line == '\n':
            break
        if line != '':
            # key parsing
            key = line.split(':')[0]
            # print(key)

            # value parsing
            value = line.replace(key, "")[:-1]
            value = value[1:].lstrip()
            # print(value)
            wr.writerow([key, value])
            dic[key] = value

    print(dic)

    file.close()

def search(dirname,wr):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        # print (full_filename)
        wr.writerow([filename])
        parsing(full_filename,wr)


csv_file, wr = open_csv_file()
search("c:/enron_email/emails/",wr)
close_csv_file(csv_file)