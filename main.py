# VERSION 1.0 (USING PANDAS LIBRARY FOR TABLE DISPLAY, NEXT VERSION USES A SMALLER LIBRARY
# from os import system
# import sys

# try:
#     try:
#         import pandas as pd
#     except ImportError:
#         system("pip install pandas")
#         import pandas as pd
#     try:
#         import mysql.connector as sql
#     except ImportError:
#         system("pip install mysql-connector-python")
#         import mysql.connector as sql
# except: # EITHER IMPORT ERRORS OR INSTALL ERRORS
#     print("ERROR :: DEPENDENCIES COULDN'T BE IMPORTED\n")
#     sys.exit()


# # CALLED EVERYTIME OPTION 'm' IS SELECTED
# def menu():
#     print(f""" \n\t * CURRENT WORKING TABLE : {working_table.upper()} *
# --------------------------------------------------
          
# [1] : CHANGE WORKING TABLE
# [2] : DISPLAY THE TABLE
# [3] : ADD RECORD
# [4] : UPDATE COLUMN
# [5] : DELETE RECORD
          
# [0] : ROLLBACK CHANGES
# [9] : COMMIT CHANGES 

# [M] : MENU
# [Q] : RUN CUSTOM QUERY
# [C] : CLEAR SCREEN
# [X] : EXIT PROGRAM

# """)

# # THIS FUNCTION DISPLAYS THE 'TABLE' THAT IS THE WORKING TABLE
# # THE FIELD_NAMES OF THE WORKING TABLE ARE FETCHED AT THE TIME OF SELECTING THE TABLE IN table_select()
# # USES PANDAS DATAFRAME OBJECT FOR TABULAR PRINTING
# def display_table(cursor):
#     global working_table, field_names;
     
#     try:
#         data = cursor.fetchall() #data for displaying
#         if data == []:
#             print(f"empty table {working_table} : {field_names}")
#             return;
#     except:
#         print("QUERY_ERROR :: DATA FOR THE GIVEN TABLE COULDN'T BE FETCHED\n")

#     # MAPPING FIELD_NAMES AS KEY TO COLUMN WISE VALUES OF DATA LIST
#     # THE FIRST INDEX 'j' (TUPLE / RECORD) INCREASES FASTER WHILE 'i' REMAINS AS LONG AS IT 
#     # TRAVERSES THROUGH THE WHOLE LIST OF RECORD
#     # EACH 'j' INDEX VALUE IS APPENDED TO LIST COLUMN ITEMS, BEFORE INCREMENT OF 'i' 
#     # FIELD_NAMES[i] IS ASSIGNED THAT COLUMN_LIST AND IS CLEARED  
#     try:
#         mapp = {}
#         column_items = []
#         for i in range(len(field_names)):
#             for j in range(0,len(data)):
#                 column_items.append(data[j][i])

#             mapp[field_names[i]] = column_items
#             column_items = []
#     except:
#         print("ERROR :: COUDLN'T MAP COLUMNS TO VALUES...\n")
#         return;
#     print("\n\n"+"---------------"*len(field_names))
#     print(f"{pd.DataFrame(mapp, index = ['' for i in range(0,len(list(mapp.values())[0]))])}")
#     print("---------------"*len(field_names))

# # THIS CHANGES WORKING TABLE AS WELL AS STORES FIELD NAMES
# # THE FIRST FUNCTION THAT RUNS, RETURNS TRUE IF EVERYTHING GOES WELL, ELSE FALSE
# # WHILE LOOP RUNS UNTIL A 'TRUE' VALUE IS RETURNED, WHICH SWITCHES TO FALSE (not True) TO EXIT THE LOOP
# def table_select():
#     global working_table, cur, field_names, cur;

#     cur.execute("show tables;")
#     tables = cur.fetchall();

#     # displaying tables
#     print("\nSELECT WORKING TABLE :")
#     for i in range(len(tables)):
#         print(f"[{i+1}] : {tables[i][0].upper()}", end = "\n")
#     try:
#         option = int(input("\n>>> "))
#         option -= 1
#     except:
#         system('cls');
#         print("ERROR :: OPTION DID NOT MATCH");
#         return False;

#     if option not in  range(len(tables)):
#         system("cls")
#         print("ERROR :: OPTION DID NOT MATCH");
#         return False;

#     working_table = tables[option][0];
#     print(f"TABLE CHANGED TO {working_table.upper()}\n")
#     # GETTING FIELD_NAMES USING DESCRIBE QUERY
#     # EACH IS ENCLOSED IN A TUPLE WHICH IS STORED IN A LIST
#     # GETTING 0th INDEX OF EACH TUPLE
#     cur.execute(f"desc {working_table};")
#     fields = cur.fetchall()
#     field_names = []
#     for field in fields:
#         field_names.append(field[0])
#     return True;

# # A BASIC FUNCTION FOR ADDING DATA PER FIELD FOR A RECORD
# def add_record():
#     global working_table, field_names, cur;
#     tup = ()
#     # ENTER VALUE FOR EACH FIELD
#     while True:
#         try:
#             for field in field_names:
#                 tup += (input(f">>> {field} : "),)
#             cur.execute(f"insert into {working_table} values {tup};")
#             system("cls")

#             q = input("Record added, Continue ? [y,n]\n>>> ")
#             if q.lower() == 'y':
#                 continue;
#             elif q.lower() == 'n':
#                 system("cls")
#                 return;
#             else:
#                 system("cls")
#                 print("ERROR :: OPTIONS DIDN'T MATCH, ENTRIES DISCARDED, ABORTED BY DEFAULT\n")
#                 return;
                
#         except:
#             system("cls")
#             print("ENTRY_ERROR :: THE GIVEN VALUES COULDN'T BE ENTERED INTO THE TABLE\n")
#             return 1;

# # ASKS FOR THE FIELD TO BE UPDATED
# # TAKES 'todo' AS INPUT FOR WHAT HAS TO BE DONE TO THE FIELD
# # CONDTION CAN BE LEFT EMPTY TO UPDATE EVERY RECORD
# def update_column():
#     global working_table, field_names, cur;

#     print("UPDATE WHICH FIELD ? :")
#     for i, field in enumerate(field_names):
#         print(f"{i+1} : {field}",end="    ")
    
#     try:
#         option = int(input(">>> ")) -1
#         todo = str(input(f"SET {field_names[option]} = "))
#         condition = str(input("(OPTIONAL) CONDITION WHERE >>> "))
#         if condition == '':
#             cur.execute(f"UPDATE {working_table} SET {field_names[option]} = {todo};")
#         else:
#             cur.execute(f"UPDATE {working_table} SET {field_names[option]} = {todo} WHERE\
#                          {condition};")
#         print("\nRECORDS UPDATED")
#         return 0;
#     except ValueError:
#         system("cls")
#         print("ERROR :: OPTIONS DID NOT MATCH")
#         return 1;
#     except IndexError:
#         system("cls")
#         print("ERROR :: OPTIONS DID NOT MATCH")
#         return 1;
#     except:
#         system("cls")
#         print("QUERY_ERROR :: QUERY COULDN'T BE PROCESSED, PLEASE CHECK CONDITIONS")
#         return 1;

# # ASKS FOR THE FIELD USING WHICH THE CONDITIONAL DELETION OF A RECORD TAKES PLACE
# def delete_record():
#     global working_table, field_names, cur

#     print("\nDELETE USING WHICH FIELD ? :")
#     for i,field in enumerate(field_names):
#         print(f"{i+1} : {field}" ,end = "    ")
#     print("\n")

#     try:
#         option = int(input(">>> ")) -1
#         condition = str(input(f"WHERE >>> {field_names[option]} = "))
#         cur.execute(f"DELETE FROM {working_table} WHERE {field_names[option]} = {condition};")
#         print("DELETED RECORD\n")
#         return 0;
#     except ValueError:
#         system("cls")
#         print("ERROR :: THE VALUE ENTERED WAS INAPPROPRIATE")
#         return 1;
#     except: #QUERY_ERROR
#         system("cls")
#         print("QUERY_ERROR :: THE QUERY COULDN'T BE PROCESSED, PLEASE CHECK THE CONDITION")
#         return 1;

# # RUN A QUERY YOURSELF, DISPLAY FUNTIONALITY IS UNAVAILABLE
# # JOINS ARE ALSO NOT SUPPORTED
# # CAN ALTER THE DEFINITION OF TABLE AND RECORDS IF NEEDED
# # WORKS FOR TABLES OTHER THAN CURRENT WORKING TABLE AS WELL
# def query():
#     global cur, field_names, working_table;
#     try:
#         qry = str(input("\nQUERY :\n>>> "))

#         # CHECK IF USER TRIES TO CHANGE DATABASE, PERFORMS SELECT QUERY OR SHOW QUERY
#         if qry[0:3].lower() == "use":
#             print("QUERY_ERROR :: CAN'T CHANGE DATABASE\n")
#             return 1;
#         elif qry[0:4].lower() == "show":
#             print("QUERY RAN SUCCESSFULLY, HOWEVER, THE RESULT CAN'T BE DISPLAYED\n")
#             return 1;
#         elif qry[0:6].lower() == "select":
#             print("ERROR :: SELECT QUERY IS NOT SUPPORTED\n")
#             return 1;
#         elif qry[0:4].lower() == "desc" or qry[0:8].lower == "describe":
#             cur.execute(qry)
#             fields = cur.fetchall()
#             print("\n")
#             for field in fields:
#                 print(f"{field[0]}  :  {field[1]}")
#             print("\n")
#             return 0;
#         # /////////////////////////////////////////

#         if qry[0:5].lower() != "alter":
#             cur.execute(qry)
#             cur.fetchall() # clearing data buffer
#             print("QUERY RAN SUCCESSFULLY\n")
#         # GETTING FIELD_NAMES WITHOUT CHANGING WORKING TABLE AGAIN
#         # IF QUERY IS RUN FOR ANOTHER TABLE, FIELD_NAMES ARE STORED IN table_select()
#         # ASKING IF ALTER COMMAND SHOULD BE RUN, IT CAN'T BE UNDONE...
#         elif qry[0:5].lower() == "alter": 
#             try:
#                 ch = str(input("ALTER COMMANDS ARE PERMANENT, CAN'T BE UNDONE\nCONTINUE ? [y,n] >>> "))
#                 if ch.lower() == 'y':
#                     cur.execute(qry)
#                     cur.fetchall() # clearing data buffer
#                     CONN.commit()
#                     print("QUERY RAN SUCCESSFULLY\n")
#                 elif ch.lower() =='n':
#                     print("QUERY WAS DISCARDED\n")
#                     return 1;
#                 else:
#                     print("ERROR :: QUERY WAS DISCARDED BY DEFAULT\n")
#                     return 1;
#             except:
#                 print("ERROR :: OPTIONS DIDN'T MATCH\n")
#                 return 1;
#         cur.execute(f"desc {working_table};")
#         fields = cur.fetchall()
#         field_names = []
#         for field in fields:
#             field_names.append(field[0])
#         return 0;
#     except : # QUERY_ERROR
#         print("QUERY_ERROR :: CONDTION / SYNTAX COULD NOT BE PROCESSED\n")
#         return 1;

# def changes(arg):
#     if arg == '0':
#         print("RECENT QUERIES HAVE BEEN UNDONE\n")
#         CONN.rollback()
#         return 0;
#     if arg == '9':
#         try:
#             ch = str(input("DO YOU WANT TO COMMIT CHANGES ? [y,n]\n>>> "))
#             if ch.lower() == 'y': 
#                 print("RECENT CHANGES WERE MADE PERMANENT\n")
#                 CONN.commit()
#                 return 0;
#             elif ch.lower() == 'n':
#                 print("NO CHANGES MADE...\n")
#                 return 0;
#         except:
#             print("ERROR :: INAPPROPRIATE INPUT, NO CHANGES WERE MADE\n")
#             return 1;

# #////////////////// CONNECTION SETUP //////////////////
# CONN = sql.connect(user = "root", password = "csproj25", database = "showroom")
# cur = CONN.cursor()

# # TABLE SELECT:
# system("cls")
# working_table = "NONE";
# while not table_select():
#     continue;
# system("cls")
# menu()

# # MAIN MENU:
# while True:
#     choice = str(input(">>> "))
#     match choice:
#         case choice if choice.lower() == 'x':
#             system("cls")
#             break; # CONNECTION CLOSES AT LAST
#         case choice if choice.lower() == 'c':
#             system("cls");
#             menu();
#         case choice if choice.lower() == 'm':
#             menu()
#         case choice if choice.lower() == 'q':
#             query()
#         case '1':
#             table_select()
#         case '2':
#             cur.execute(f"select * from {working_table}")
#             display_table(cur)
#         case '3':
#             add_record()
#         case '4':
#             update_column()
#         case '5':
#             delete_record()
#         case choice if choice == '0' or choice == '9':
#             changes(choice)
#         case _: # DEFAULT CASE TO AVOID UNWANTED OPTION INPUT
#             print("ERROR :: OPTIONS DID NOT MATCH")
#             continue;


# #\\\\\\\\\\\\\\\\ CONNECTION CLOSE \\\\\\\\\\\\\\\\
# try: # to avoid error with un-fetched data in the cursor object
#     cur.close()
#     CONN.close()
# except:
#     pass
# finally:
#     sys.exit()

# VERSION 1.1 USES TABULATE LIBRARY, FOR A CLEANER AND MORE ACCURATE TABLE DISPLAY, JUST LIKE SQL
# VERSION 1.0 CAN STILL BE USED, ONLY DIFFERENCE IS USING A DEDICATED LIBRARY FOR TABLES


from os import system
import sys

try:

    try:
        # simple library for tabular display
        from tabulate import tabulate
    except ImportError:
        system("pip install tabulate")
        from tabulate import tabulate

    try:
        import mysql.connector as sql
    except ImportError:
        system("pip install mysql-connector-python")
        import mysql.connector as sql

except: # EITHER IMPORT ERRORS OR INSTALL ERRORS
    print("ERROR :: DEPENDENCIES COULDN'T BE IMPORTED\n")
    sys.exit()


# CALLED EVERYTIME OPTION 'm' IS SELECTED
def menu():
    print(f""" \n\t{" "*(len(working_table)//2)}* CURRENT WORKING TABLE : \
{working_table.upper()} *
*----------------------------------------{"--"*len(working_table)}*
          
[1] : CHANGE WORKING TABLE
[2] : DISPLAY THE TABLE
[3] : ADD RECORD
[4] : UPDATE COLUMN
[5] : DELETE RECORD
          
[0] : ROLLBACK CHANGES
[9] : COMMIT CHANGES 

[Q] : RUN CUSTOM QUERY
[C] : CLEAR SCREEN
[X] : EXIT PROGRAM

""")

# THIS FUNCTION DISPLAYS THE 'TABLE' THAT IS THE WORKING TABLE
# THE FIELD_NAMES OF THE WORKING TABLE ARE FETCHED AT THE TIME OF
# SELECTING THE TABLE IN table_select()

def display_table(cursor):
    global working_table, field_names;
     
    try:
        data = cursor.fetchall() #data for displaying
        temp_mem = [] # CONTAINS ONLY FIELD NAME AND NOT ITS DATATYPE 
        for i in field_names:
            temp_mem.append(i[0])
        if data == []:
            print(f"\nEMPTY TABLE {working_table.upper()}")
            print(tabulate([temp_mem,[]],headers="firstrow",tablefmt="simple_grid"),end="\n")
            return;
    except:
        print("QUERY_ERROR :: DATA FOR THE GIVEN TABLE COULDN'T BE FETCHED\n")

    # USING TABULATE MODULE TO CREATE A TABLE WITH 'GRID' FORMATTING
    
    print(tabulate(data,headers=temp_mem,
                   tablefmt="simple_grid"))

    # CLEARING TEMPORARY MEMORY
    del temp_mem, data
    return;

# THIS CHANGES WORKING TABLE AS WELL AS STORES FIELD NAMES
# ITS THE FIRST FUNCTION THAT RUNS, RETURNS TRUE IF EVERYTHING GOES WELL, ELSE FALSE
# WHILE LOOP RUNS UNTIL A 'TRUE' VALUE IS RETURNED, WHICH SWITCHES TO FALSE (not True) TO EXIT THE LOOP
def table_select():
    global working_table, field_names, cur;

    cur.execute("show tables;")
    tables = cur.fetchall();

    # displaying tables
    print("\nSELECT WORKING TABLE :")
    for i in range(len(tables)):
        print(f"[{i+1}] : {tables[i][0].upper()}", end = "\n")
    try:
        option = int(input("\n>>> "))-1
    except:
        system('cls');
        print("ERROR :: OPTION DID NOT MATCH");
        return False;

    if option not in  range(len(tables)):
        system("cls")
        print("ERROR :: OPTION DID NOT MATCH");
        return False;

    working_table = tables[option][0];
    print(f"TABLE CHANGED TO {working_table.upper()}\n")
    
    # GETTING FIELD_NAMES USING DESCRIBE QUERY
    # EACH IS ENCLOSED IN A TUPLE WHICH IS STORED IN A LIST
    # GETTING 0th INDEX OF EACH TUPLE FOR NAME, 1st INDEX FOR DATATYPE
    cur.execute(f"desc {working_table};")
    fields = cur.fetchall()
    field_names = []
    for field in fields:
        field_names.append(field[0:2])
    return True;

# A BASIC FUNCTION FOR ADDING DATA PER FIELD FOR A RECORD
def add_record():
    global working_table, field_names, cur;
    tup = ()
    # ENTER VALUE FOR EACH FIELD
    while True:
        try:
            for field in field_names:
                tup += (input(f">>> {field[0]} ({field[1]}) : "),)
            cur.execute(f"insert into {working_table} values {tup};")
            system("cls")
            menu()
            q = input("\nRecord added, Continue ? [y,n]\n>>> ")
            if q.lower() == 'y':
                tup = ()
                continue;
            elif q.lower() == 'n':
                system("cls")
                menu()
                del tup
                return 0;
            else:
                system("cls")
                menu()
                print("\nERROR :: OPTIONS DIDN'T MATCH, ENTRIES DISCARDED, ABORTED BY DEFAULT\n")
                return 1;
                
        except:
            system("cls")
            menu()
            print("\nENTRY_ERROR :: THE GIVEN VALUES COULDN'T BE ENTERED INTO THE TABLE\n")
            return 1;

# ASKS FOR THE FIELD TO BE UPDATED
# TAKES 'todo' AS INPUT FOR WHAT HAS TO BE DONE TO THE FIELD
# CONDTION CAN BE LEFT EMPTY TO UPDATE EVERY RECORD
def update_column():
    global working_table, field_names, cur;

    print("\nUPDATE WHICH FIELD ? :")
    for i, field in enumerate(field_names):
        print(f"{i+1} : {field[0]} ({field[1]})")
    try:
        option = int(input("\n>>> ")) -1
        todo = str(input(f"SET {field_names[option][0]} = "))
        condition = str(input("(OPTIONAL) CONDITION WHERE >>> "))
        if condition == '':
            cur.execute(f"UPDATE {working_table} SET {field_names[option][0]} = {todo};")
        else:
            cur.execute(f"UPDATE {working_table} SET {field_names[option][0]} = {todo} WHERE\
                         {condition};")
        print("\nRECORDS UPDATED")
        return 0;
    except ValueError:
        system("cls")
        menu()
        print("\nERROR :: OPTIONS DID NOT MATCH\n")
        return 1;
    except IndexError:
        system("cls")
        menu()
        print("\nERROR :: OPTIONS DID NOT MATCH\n")
        return 1;
    except:
        # system("cls")
        # menu()
        print("\nQUERY_ERROR :: QUERY COULDN'T BE PROCESSED, PLEASE CHECK CONDITIONS\n")
        return 1;

# ASKS FOR THE FIELD USING WHICH THE CONDITIONAL DELETION OF A RECORD TAKES PLACE
def delete_record():
    global working_table, field_names, cur

    print("\nDELETE USING WHICH FIELD ? :")
    for i,field in enumerate(field_names):
        print(f"{i+1} : {field [0]} ({field[1]})")
    print("\n")

    try:
        option = int(input(">>> ")) -1
        condition = str(input(f"WHERE >>> {field_names[option][0]} = "))
        cur.execute(f"DELETE FROM {working_table} WHERE {field_names[option][0]} = {condition};")
        print("DELETED RECORD\n")
        return 0;
    except ValueError:
        system("cls")
        menu()
        print("ERROR :: THE VALUE ENTERED WAS INAPPROPRIATE")
        return 1;
    except: #QUERY_ERROR
        system("cls")
        menu()
        print("QUERY_ERROR :: THE QUERY COULDN'T BE PROCESSED, PLEASE CHECK THE CONDITION")
        return 1;

# RUN A QUERY YOURSELF, DISPLAY FUNTIONALITY IS UNAVAILABLE
# JOINS ARE ALSO NOT SUPPORTED
# CAN ALTER THE DEFINITION OF TABLE AND RECORDS IF NEEDED
# WORKS FOR TABLES OTHER THAN CURRENT WORKING TABLE AS WELL
def query():
    global cur, field_names, working_table;
    try:
        qry = str(input("\nQUERY :\n>>> "))

        # CHECK IF USER TRIES TO CHANGE DATABASE, PERFORMS SELECT QUERY OR SHOW QUERY
        if qry[0:3].lower() == "use":
            print("QUERY_ERROR :: CAN'T CHANGE DATABASE\n")
            return 1;
        elif qry[0:4].lower() == "show":
            print("QUERY RAN SUCCESSFULLY, HOWEVER, THE RESULT CAN'T BE DISPLAYED\n")
            return 1;
        elif qry[0:6].lower() == "select":
            print("ERROR :: SELECT QUERY IS NOT SUPPORTED\n")
            return 1;
        elif qry[0:4].lower() == "desc" or qry[0:8].lower == "describe":
            cur.execute(qry)
            fields = cur.fetchall()
            print("\n")
            for field in fields:
                print(f"{field[0]}  :  {field[1]}")
            print("\n")
            return 0;
        elif qry[0:10].lower() == "drop table":
            cur.execute(qry)
            system("cls")
            table_select()
            menu()
            return 0;
        # /////////////////////////////////////////

        if qry[0:5].lower() != "alter":
            cur.execute(qry)
            cur.fetchall() # clearing data buffer
            print("QUERY RAN SUCCESSFULLY\n")
        # GETTING FIELD_NAMES WITHOUT CHANGING WORKING TABLE AGAIN
        # IF QUERY IS RUN FOR ANOTHER TABLE, FIELD_NAMES ARE STORED IN table_select()
        # ASKING IF ALTER COMMAND SHOULD BE RUN, IT CAN'T BE UNDONE...
        elif qry[0:5].lower() == "alter": 
            try:
                ch = str(input("ALTER COMMANDS ARE PERMANENT, CAN'T BE UNDONE\nCONTINUE ? [y,n] >>> "))
                if ch.lower() == 'y':
                    try:
                        cur.execute(qry)
                        cur.fetchall() # clearing data buffer
                        CONN.commit()
                    except: # if alter query can't be processed
                        print("QUERY_ERROR :: CONDTION / SYNTAX COULD NOT BE PROCESSED\n")
                        return 1;
                    print("QUERY RAN SUCCESSFULLY\n")
                elif ch.lower() =='n':
                    print("QUERY WAS DISCARDED\n")
                    return 1;
                else:
                    print("ERROR :: QUERY WAS DISCARDED BY DEFAULT\n")
                    return 1;
            except:
                print("ERROR :: OPTIONS DIDN'T MATCH\n")
                return 1;
        cur.execute(f"desc {working_table};")
        cur.execute(f"desc {working_table};")
        fields = cur.fetchall()
        field_names = []
        for field in fields:
            field_names.append(field[0:2])
        return 0;
    except : # QUERY_ERROR
        print("QUERY_ERROR :: CONDTION / SYNTAX COULD NOT BE PROCESSED\n")
        return 1;

def changes(arg):
    if arg == '0':
        print("RECENT QUERIES HAVE BEEN UNDONE\n")
        CONN.rollback()
        return 0;
    if arg == '9':
        try:
            ch = str(input("DO YOU WANT TO COMMIT CHANGES ? [y,n]\n>>> "))
            if ch.lower() == 'y': 
                print("RECENT CHANGES WERE MADE PERMANENT\n")
                CONN.commit()
                return 0;
            elif ch.lower() == 'n':
                print("NO CHANGES WERE MADE PERMANENT...\n")
                return 0;
        except:
            print("ERROR :: INAPPROPRIATE INPUT, NO CHANGES WERE MADE\n")
            return 1;

#////////////////// CONNECTION SETUP //////////////////
CONN = sql.connect(user = "root", password = "csproj25", database = "showroom")
cur = CONN.cursor()

# TABLE SELECT:
system("cls")
working_table = "NONE";
while not table_select():
    continue;
system("cls")
menu()

# MAIN MENU:
while True:
    choice = str(input(">>> "))
    match choice:
        case choice if choice.lower() == 'x':
            system("cls")
            break; # CONNECTION CLOSES AT LAST
        case choice if choice.lower() == 'c':
            system("cls");
            menu();
        case choice if choice.lower() == 'q':
            query()
        case '1':
            table_select()
        case '2':
            cur.execute(f"select * from {working_table}")
            display_table(cur)
        case '3':
            add_record()
        case '4':
            update_column()
        case '5':
            delete_record()
        case choice if choice == '0' or choice == '9':
            changes(choice)
        case _: # DEFAULT CASE TO AVOID UNWANTED OPTION INPUT
            menu()
            print("ERROR :: OPTIONS DID NOT MATCH")
            continue;

#\\\\\\\\\\\\\\\\ CONNECTION CLOSE \\\\\\\\\\\\\\\\
try: # to avoid error with un-fetched data in the cursor object
    cur.close()
    CONN.close()
except:
    pass
finally:
    sys.exit()
