# Ats-Tool-Using-Python
Ats verification tool using the python program and updates the selected candidate to the separate database and rejected canditate in the sepereate repository
Note:
  If AN Canditate is Rejected Means He Could Only Able TO Apply After 100 Days
      To Do Before excution:
             1):  import sys
              import PyPDF2.
              import datetime
              import re
              import mysql.connector as mysql
          Give "pip install module name"
          To Import All This Module
              2:)  Need To Check The Pdf file Present In The Same Directory and Given it's name Correctly
              3:)Databse Should Be Neede To Created By Yourself 
    mydb = mysql.connect(
        host="localhost",
        user="root",  # Give Your Mysql Database User Name
        password="12345",#Give Your Mysql Database Password
        database="science_day" # Give Your Mysql Database  Name )
    mycursor = mydb.cursor()
    # Gets The Cursor Object
    role_query = "SELECT role FROM science_day.keyword_role"
       #Getting The Total Nmber of Available Role From The DataBase
  mycursor.execute(role_query) 
    #This Line Will Excute The Given MYSQL Qury
  role_results=mycursor.fetchall()
  This Line Will Fetch All Data From The DataBase
  
    print("The Available Roles Are")
    for item in range (len(role_results)):
        print(f"Role ID => {item} : {role_results[item][0]}")
    applied_role=int(input("Enter Role Id To Apply :"))
    role=str(role_results[applied_role][0])
    query = "SELECT Keyword1, Keyword2, Keyword3, Keyword4, Keyword5 FROM science_day.keyword_role WHERE Role='{}'".format(role)
  Fetching the Keywords According To The Given Usage

  pdfFileObj = open('check.pdf', 'rb')
  #To Open The Pdf File
    Make Sure to Give PDf File In The ' ' Single or Double Quotes
    Make Sure To Give Your Pdf Directory Correctly
extracted_text = extracted_text.replace("/", "").replace("\xa0", "").replace("\n", " ")#Repalcing the unwanted values

email = ', '.join(email_addresses)
        #Converting the Mail and Mobile Number To Str Format To Update in Database
        mb_num = ', '.join(mobile_numbers)

      indian_mobile_pattern = re.compile(r'(\+91|0)?[\s-]?[789]\d{9}')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    Taking The Mobbile Number And Email ID Seperately Using The Regex 

        if (mobile_numbers and email_addresses == []):
        sys.exit("No mobile numbers or email addresses found in the PDF.")
      Exiting Directly From the Program If There Is no Mail Or Number To Contact

       for b in result_list:
        if b in vueb:
            Ats_score += 1
    if (email_addresses == []):
        email = "xyz"
        cid = mb_num
    elif (mobile_numbers == []):
        cid = email
        mb_num = 12456
    else:
        cid=email
      #CID is An PRIMary Key
    def reject_reterive(cid):
        rejected_query= "SELECT current_year,current_month,current_day FROM science_day.rejected_canditae WHERE cid='{}'".format(cid)
    Reteriving the canditate date if he was rejected Previously
    if Rejected Means He Could Only Able TO apply After The 100 Days

     if(coe):
     The COE Will Be True in Ony 2 Conditions
       1)If The Canditate does not applied for this Previously
                 (OR)
       2)The Canditate Could Apply After 100 of Being Rejected From The ATS Tool
        if Ats_score >= 4:
            insert_query1 = "INSERT INTO slected_canditate (email,mobile_number,cid) VALUES (%s, %s, %s)"
            # Execute the update query with values
            mycursor.execute(insert_query1, (email, mb_num, cid))
            # Commit the changes
            mydb.commit()
        else:
            insert_query2 = "INSERT INTO rejected_canditate (email,mobile_number,cid,current_day,current_month,current_year) VALUES (%s, %s, %s,%s,%s,%s)"
            mycursor.execute(insert_query2, (email, mb_num, cid, current_day, current_month, current_year))
            mydb.commit()
          Selection Or Rejection Will Be Based Upon The ATS Score
            
finally:
    try:
        pdfFileObj.close()
    except NameError:
        pass  # pdfFileObj may not be defined if an exception occurred before it was assigned
    try:
        mycursor.close()
        mydb.close()
    except NameError:
        pass  # mycursor or mydb may not be defined if an exception occurred before they were assigned
Closing All The Opened Objects In The Finally Block
      
