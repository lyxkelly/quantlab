import csv

with open('input.csv', 'r') as csvfile:
    csv_reader = csv.reader(csvfile)

    # create dictionary to sum quantities of each symbol#
    a = dict()
    for line in csv_reader:
        if line[1] in a:
            num = int(a.get(line[1])) + int(line[2])
            a[line[1]] = num
        else:
            a[line[1]] = int(line[2])  # store symbol in map with quantities


    csvfile.seek(0)
    # create dictionary to find max trade price#
    b = dict()
    for line in csv_reader:
        if line[1] in b:
            if int(line[3]) > int(b.get(line[1])):
                b[line[1]] = int(line[3])
        else:
            b[line[1]] = int(line[3])


    csvfile.seek(0)
    # create dictionary to find weighted avg price#
    c = dict()
    for line in csv_reader:
        if line[1] in c:
            c[line[1]] = int(c.get(line[1])) + (int(line[3]) * int(line[2]))
        else:
            c[line[1]] = int(line[3]) * int(line[2])
    for k in c:
        c[k] = int(c.get(k))//int(a.get(k))  # weighted sum / total quantity floor

    csvfile.seek(0)
    # create dictionary to find max time gap#
    d = dict() # keep track of last time stamp
    e = dict() # keep track of max gap
    for line in csv_reader:
        if not line[1] in d:
            d[line[1]] = line[0]
            e[line[1]] = 0
        else:
            if int(line[0]) - int(d.get(line[1])) > int(e.get(line[1])):
                e[line[1]] = int(line[0]) - int(d.get(line[1]))
            d[line[1]] = line[0]

    # store into output CSV file
    with open('output.csv', 'w') as csvoutput:
        csv_writer = csv.writer(csvoutput)
        for key in sorted(a.keys()):
            temp = []
            temp.append(key)
            temp.append(e.get(key))
            temp.append(a.get(key))
            temp.append(c.get(key))
            temp.append(b.get(key))
            csv_writer.writerow(temp)






