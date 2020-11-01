# importing csv module 
import csv
import difflib
  
# csv file name 
filename = "inventory.csv"
  
# initializing the titles and rows list 
fields = [] 
rows = [] 

BOOK = 0
TITLE = 1
AUTHOR = 2
BINDING = 3
PUBDATE = 4
PUBLISHER = 5
ISBN10 = 6
ISBN13 = 7
CONDITION = 8
DUSTJACKET = 9
SIGNED = 10
EDITION = 11
PRICE = 12
DESCR = 13
SYNOPSIS = 14
ABOUT_AUTH = 15
  
# reading csv file 
with open(filename, 'r') as csvfile: 
    # creating a csv reader object 
    csvreader = csv.reader(csvfile) 
      
    # extracting field names through first row 
    fields = next(csvreader) 
  
    # extracting each data row one by one 
    for row in csvreader: 
        rows.append(row)
  
# AUTHOR
for row in rows:
    author_field = row[AUTHOR]
    author_field = author_field.title()
    if ';' in author_field:
        author_field = author_field.split(';')[0]
    if '&' in author_field:
        author_field = author_field.split(';')[0]
    # check for 'first, last' format
    if ',' in author_field:
        split = author_field.split(',')
        first = split[1][1:]
        last = split[0]
    else:
        split = author_field.split(' ')
        if len(split) > 1:
            first = ' '.join(split[:-1])
            last = split[-1]
        else:
            last = split[0]
            first = 'NA'
    first = first.strip()
    last = last.strip()
    row[AUTHOR] = f'{last},{first}'

# BINDING
VALID_BINDINGS = ['NA', 'Paperback', 'Single Issue', 'Hard Cover', 'Leather Bound', 'Library Binding', 'Cloth', 'Pock']
for row in rows:
    binding_field = row[BINDING].title()
    if binding_field == 'Na':
        binding_field = 'NA'
    if 'unknown' in binding_field.lower():
        binding_field = 'NA'
    if 'single' in binding_field.lower():
        binding_field = 'Single Issue Magazine'
    if 'mass' in binding_field.lower():
        binding_field = 'Paperback'
    if 'soft' in binding_field.lower():
        binding_field = 'Paperback'
    if 'paper' in binding_field.lower():
        binding_field = 'Paperback'
    if 'hard' in binding_field.lower():
        binding_field = 'Hard Cover'
    if 'leather' in binding_field.lower():
        binding_field = 'Leather Bound'
    if 'cloth' in binding_field.lower():
        binding_field = 'Cloth'
    if 'library' in binding_field.lower():
        binding_field = 'Library Binding'
    if 'magazine' in binding_field.lower():
        binding_field = 'Paperback'
    if 'pock' in binding_field.lower():
        binding_field = 'Pock'
    if binding_field not in VALID_BINDINGS:
        binding_field = 'NA'
    row[BINDING] = binding_field
        
# PRICE
for row in rows:
    price_field = row[PRICE]
    if len(price_field) > 4:
        price_field = price_field[4:]
    else:
        price_field = 'NA'
    row[PRICE] = price_field

with open('cleaned.csv', 'w', newline='') as csvfile:
    writer = csv.writer(csvfile, delimiter=',', quotechar='"', quoting=csv.QUOTE_ALL)
    writer.writerow(fields)
    for row in rows:
        writer.writerow(row)
