import csv
import re
import random



csv_path = str(input("Enter full path to file (in quotes), please: ").strip('"'))

reader = csv.reader(open(csv_path, 'rU'))
lines = list(reader)


random.shuffle(lines)

#header_row=lines.pop(0)


print len(lines)

div_files = int(input("Number of chunks "))

it=1
for subset in [lines[i::div_files] for i in range(div_files)]:

	print "Splittin' file #"+str(it)

	write_path = re.sub(r'(\.csv)$',r'_sub'+str(it)+r'\1',csv_path)
	it+=1

	with open(write_path, 'wb') as writefile:
		writer = csv.writer(writefile, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
		#writer.writerow(header_row)
		for row in subset:
			encoded_row=[]
			for data in row:
				encoded_row.append(unicode(data, errors='ignore'))
			writer.writerow(encoded_row)
print ""
print "Tada! The subsets are now in the same directory as your original."
