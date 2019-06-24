import csv
from datetime import datetime
import os

def open_csv_file():
    csv_file = open('data.csv', 'w', encoding='utf-8', newline='')
    wr = csv.writer(csv_file)
    return (csv_file, wr)

def close_csv_file(csv_file):
    csv_file.close()

def make_new_list(newlist, list, wr, head, content):
    content = content.strip()
    newlist.insert(0, head)
    newlist.insert(0, content)
    wr.writerow(newlist)
    del newlist[1] ,newlist[0]

def parsing(filename,wr,header):
    file = open(filename, 'r')
    dic = {}

    while True:
        line = file.readline()
        if line == '\n':
            break
        if line != '':
            if line.find(':') == -1:
                value = dic[key]
                dic[key] = value + line.strip()
                continue

            # key parsing
            key = line.split(':')[0]
            # print(key)

            # value parsing
            value = line.replace(key, "")[:-1]
            value = value[1:].lstrip()
            # print(value)
            dic[key] = value

    list = []

    for head in header:
        if head in ('To', 'Cc', 'Bcc'):
            continue

        if dic.get(head) != None:
            if head == "Date":
                t = datetime.strptime(dic.get(head)[:-6],
                                      '%a, %d %b %Y %H:%M:%S %z')
                list.append(t.strftime("%Y-%m-%d %H:%M:%S"))
            else:
                list.append(dic.get(head))
        else:
            list.append("")

    for head in header:
        if head in ('To', 'Cc', 'Bcc'):
            content = dic.get(head)
            if content != None:
                if content.find(',') == None:
                    newlist = list
                    make_new_list(newlist, list, wr, head, content)
                else :
                    contentlist = content.split(',')
                    for content in contentlist:
                        newlist = list
                        make_new_list(newlist, list, wr, head, content)
    file.close()

def search(dirname,wr,header):
    filenames = os.listdir(dirname)
    for filename in filenames:
        full_filename = os.path.join(dirname, filename)
        # print (full_filename)
        # wr.writerow([filename])
        parsing(full_filename,wr,header)

if __name__ == "__main__":

    csv_file, wr = open_csv_file()

    header = ["Message-ID", "Date", "From", "To", "Subject", "Cc",
              "Mime-Version", "Content-Type", "Content-Transfer-Encoding",
              "Bcc", "X-From", "X-To", "X-cc", "X-bcc", "X-Folder",
              "X-Origin", "X-FileName"]

    newheader = ["Recipient", "Recipient-type", "Message-ID", "Date", "From",
                 "Subject", "Mime-Version", "Content-Type",
                 "Content-Transfer-Encoding", "X-From", "X-To", "X-cc",
                 "X-bcc", "X-Folder", "X-Origin", "X-FileName"]

    wr.writerow(newheader)
    search("c:/enron_email/emails/",wr, header)
    close_csv_file(csv_file)