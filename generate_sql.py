# importing csv module 
import csv
import uuid
  
# csv file name 
filename = "test_data.csv"
  
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
JACKET = 9
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

SQL = ''

# set of distinct titles
titles = set()
# set of distinct authors
authors = set()
# set of distinct publishers
publishers = set()
# maps title => synopsis
synopsis = {}
# maps author => about author
author_to_about_author = {}
# maps title => book id
title_to_book_id = {}
# maps title => author id
title_to_author_id = {}
# maps author name => author id
author_to_id = {}
# maps publisher name => publisher id
publisher_to_id = {}
# maps title => publisher id
title_to_pub_id = {}
# maps title => pub date
title_to_pub_date = {}
# incrementing counter
title_id = 1
# incrementing counter
author_id = 1
# incrementing counter
publisher_id = 1

for row in rows:
    if row[AUTHOR] != 'NA':
        if row[AUTHOR] not in authors:
            author_to_id[row[AUTHOR]] = author_id
            author_id += 1
        authors.add(row[AUTHOR])
        # the last encountered 'about author' will be associated with author
        if row[ABOUT_AUTH] != 'NA':
            author_to_about_author[row[AUTHOR]] = row[ABOUT_AUTH]
    if row[PUBLISHER] != 'NA' and row[PUBLISHER] not in publishers:
        publishers.add(row[PUBLISHER])
        publisher_to_id[row[PUBLISHER]] = publisher_id
        publisher_id += 1
    if row[TITLE] != 'NA':
        if row[TITLE] not in titles:
            title_to_book_id[row[TITLE]] = title_id
            title_id += 1
        titles.add(row[TITLE])
        if row[AUTHOR] != 'NA':
            title_to_author_id[row[TITLE]] = author_to_id[row[AUTHOR]]
        # the last encountered synopsis will be associated with title
        if row[SYNOPSIS] != 'NA':
            synopsis[row[TITLE]] = row[SYNOPSIS]
        # the last encountered publisher will be associated with title
        if row[PUBLISHER] != 'NA':
            title_to_pub_id[row[TITLE]] = publisher_to_id[row[PUBLISHER]]
        # the last encountered publication date will be associated with title
        if row[PUBDATE] != 'NA':
            title_to_pub_date[row[TITLE]] = row[PUBDATE]

VALID_GRADES = ['Very Good', 'Good', 'Used']
for grade in VALID_GRADES:
    SQL += f'INSERT INTO GRADE (LABEL) VALUES (\'{grade}\');\n'

VALID_BINDINGS = ['Paperback', 'Hard Cover']
for binding in VALID_BINDINGS:
    SQL += f'INSERT INTO BINDING (BINDING_TYPE) VALUES (\'{binding}\');\n'

for publisher in publishers:
    SQL += f'INSERT INTO PUBLISHER (PUBLISHER_ID, PUBLISHER_NAME) VALUES ({publisher_to_id[publisher]}, \'{publisher}\');\n'

# Generating SQL for authors
for author in authors:
    last, first = author.split(',')
    if author in author_to_about_author:
        about = f"'{author_to_about_author[author]}'"
    else:
        about = 'NULL'
    SQL += f'INSERT INTO AUTHOR (AUTHOR_ID, FIRST_NAME, LAST_NAME, ABOUT) VALUES ({author_to_id[author]}, \'{first}\', \'{last}\', {about});\n'

# Generating SQL for books
for title in titles:
    if title in title_to_pub_id:
        pub_by = f"{title_to_pub_id[title]}"
    else:
        pub_by = 'NULL'
    if title in title_to_pub_date:
        pub_date = f"'{title_to_pub_date[title]}'"
    else:
        pub_date = 'NULL'
    if title in synopsis:
        syn = f"'{synopsis[title]}'"
    else:
        syn = 'NULL'
    SQL += f'INSERT INTO BOOK (BOOK_ID, TITLE, PUBLISHER_ID, PUBLICATION_DATE, SYNOPSIS) VALUES ({title_to_book_id[title]}, \'{title}\', {pub_by}, {pub_date}, {syn});\n'

# Generating SQL for written by
for title, author_id in title_to_author_id.items():
    book_id = title_to_book_id[title]
    SQL += f'INSERT INTO WRITTEN_BY (BOOK_ID, AUTHOR_ID) VALUES ({book_id}, {author_id});\n'

# Generating SQL for copies
for row in rows:
    copy_book = title_to_book_id[row[TITLE]]

    if row[BINDING] != 'NA':
        i = 0
        while i < len(VALID_BINDINGS):
            if VALID_BINDINGS[i] == row[BINDING]:
                copy_binding = i + 1
                break
            i += 1
    else:
        copy_binding = 'NULL'

    if row[CONDITION] != 'NA':
        i = 0
        while i < len(VALID_GRADES):
            if VALID_GRADES[i] == row[CONDITION]:
                copy_grade = i + 1
                break
            i += 1
    else:
        copy_grade = 'NULL'

    if row[JACKET] == 'NA':
        copy_jacket = 'FALSE'
    else:
        copy_jacket = 'TRUE'

    if row[EDITION] == 'NA':
        copy_edition = 'NULL'
    else:
        copy_edition = f"'{row[EDITION]}'"

    if row[ISBN10] == 'NA':
        copy_isbn10 = 'NULL'
    else:
        copy_isbn10 = f"'{row[ISBN10]}'"

    if row[ISBN13] == 'NA':
        copy_isbn13 = 'NULL'
    else:
        copy_isbn13 = f"'{row[ISBN13]}'"

    if row[PRICE] == 'NA':
        copy_price = 'NULL'
    else:
        copy_price = row[PRICE]

    if row[DESCR] == 'NA':
        copy_descr = 'NULL'
    else:
        copy_descr = f"'{row[DESCR]}'"

    if row[SIGNED] == 'NA':
        copy_signed = 'FALSE'
    else:
        copy_signed = 'TRUE'
    
    SQL += f'INSERT INTO COPY (BOOK_ID, BINDING_ID, GRADE_ID, HAS_JACKET, EDITION, ISBN_10, ISBN_13, PRICE, DESCR, SIGNED) VALUES ({copy_book}, {copy_binding}, {copy_grade}, {copy_jacket}, {copy_edition}, {copy_isbn10}, {copy_isbn13}, {copy_price}, {copy_descr}, {copy_signed});\n'
        
with open('book_collection.sql', 'w') as outfile:
    outfile.write(SQL)
