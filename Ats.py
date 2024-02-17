import sys
import PyPDF2
import re
import mysql.connector as mysql

try:
    Ats_score = 0
    # Connect to the MySQL server
    mydb = mysql.connect(
        host="localhost",
        user="root",
        password="12345",
        database="science_day"  # Add your database name here
    )
    mycursor = mydb.cursor()

    # Execute a SELECT query
    role = 'front end development'
    query = "SELECT Keyword1, Keyword2, Keyword3, Keyword4, Keyword5 FROM science_day.keyword_role WHERE Role='{}'".format(role)
    mycursor.execute(query)  # Add your table name here

    # Fetch all rows
    result = mycursor.fetchall()

    # Print the retrieved data
    tuple_values = result[0]

    # Creating a list to store the split values
    result_list = []

    # Splitting each value in the tuple and adding to the result list
    for value in tuple_values:
        result_list.extend(value.split())

    val = "python"
    vueb = []
    extracted = " "
    pdfFileObj = open('check.pdf', 'rb')
    indian_mobile_pattern = re.compile(r'(\+91|0)?[\s-]?[789]\d{9}')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    pdfReader = PyPDF2.PdfReader(pdfFileObj)

    # Get the number of pages in the PDF
    num_pages = len(pdfReader.pages)

    # Extract text from all pages
    for i in range(num_pages):
        pageObj = pdfReader.pages[i]
        extracted_text = pageObj.extract_text().lower()
        extracted_text = extracted_text.replace("/", "").replace("\xa0", "").replace("\n", " ")
        extracted += extracted_text
        vueb.extend(extracted.split())  # Adding In List
        mobile_numbers = indian_mobile_pattern.findall(extracted)
        email_addresses = email_pattern.findall(extracted)
        email = str(email_addresses)
        mb_num = str(mobile_numbers)

    if (mobile_numbers and email_addresses == []):
        sys.exit("No mobile numbers or email addresses found in the PDF.")

    for b in result_list:
        if b in vueb:
            Ats_score += 1

    if (email_addresses == []):
        email = "xyz"
        cid = mb_num
    elif (mobile_numbers == []):
        cid = email
        mb_num = 12456

    if Ats_score >= 4:
        insert_query1 = "INSERT INTO slected_canditate (email,mobile_number,cid) VALUES (%s, %s, %s)"
        # Execute the update query with values
        mycursor.execute(insert_query1, (email, mb_num, cid))
        # Commit the changes
        mydb.commit()

    else:
        insert_query2 = "INSERT INTO rejected_canditate (email,mobile_number,cid) VALUES (%s, %s, %s)"
        mycursor.execute(insert_query2, (email, mb_num, cid))
        mydb.commit()

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    pdfFileObj.close()
    mycursor.close()
    mydb.close()
