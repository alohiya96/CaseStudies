#Python 3.9.10

#Assumptions: I assumed the current year is 2017 and the previous year is 2016. 


import sqlite3, csv
import pandas as pd


def InsertData():
        connection = sqlite3.connect("CaseStudy.db")   #sqlite3.cnnect() function returns objects that will be used to interact with database 
        cursor = connection.cursor()   #creates cursor object used to SQL statements to a SQLite database using cursor.execute()

        df = pd.read_csv('casestudy.csv')
        print(df)
        #print(df[net_income].sum())
        
        #print(df)
        #file = open("casestudy.csv","r")

        cursor.execute("CREATE TABLE IF NOT EXISTS CustomerInfo (customer_email TEXT , Net_Revenue INTEGER, Year TEXT)")
        connection.commit()

        for row in df.itertuples():
                #print(row)
                insert_sql = f"INSERT INTO CustomerInfo (customer_email, Net_Revenue, Year) VALUES ('{row[2]}', '{row[3]}', '{row[4]}')"
                cursor.execute(insert_sql)




        #while True:            
        #       line = file.readline()
        #       print("Hi")

        #       if not line:
        #               break
        
        #       cursor.execute("INSERT OR IGNORE INTO CustomerInfo VALUES ('?','?','?')".format(customer_email, Net_Revenue, Year))
        #       connection.commit()

        rows = cursor.execute("SELECT* FROM CustomerInfo").fetchall()  #fetchall() retrieves all the results from the select statement
        #print(rows)
        query_one = cursor.execute("SELECT SUM(Net_Revenue) AS TotalRevenueFor2017 FROM CustomerInfo WHERE Year = '2017'").fetchall()
        connection.commit()
        print("q1")
        print(query_one)

        query_two = cursor.execute("SELECT SUM(Net_Revenue) AS NewCustomerRevenue2017 FROM CustomerInfo WHERE customer_email NOT IN (Select customer_email  From CustomerInfo WHERE Year = '2016') AND Year = '2017' ").fetchall()
        connection.commit()
        print("q2")
        print(query_two)
        
        #cursor.execute("CREATE Table ExistingRev2017 AS (SELECT SUM(Net_Revenue) AS ExistingCustomerRevenueFor2017 FROM CustomerInfo WHERE customer_email IN (SELECT customer_email  From CustomerInfo WHERE Year = '2016') AND Year = '2017' GROUP BY Year") 
#       cursor.execute("CREATE Table ExistingRev2016 AS (SELECT SUM(Net_Revenue) AS ExistingCustomerRevenueFor2016 FROM CustomerInfo WHERE customer_email IN (SELECT customer_email From Table WHERE Year = '2015') AND Year = '2017' GROUP BY Year")
#       connection.commit()

#       query_three = cursor.execute("SELECT ExistingCustomerRevenueFor2017 - ExistingCustomerRevenueFor2016 FROM ExistingRev2016, ExistingRev2017  " ) 
#       connection.commit()
#       print(query_three)
        
        
        query_five = cursor.execute("SELECT SUM(Net_Revenue) AS ExistingCustomerRevenueFor2017 FROM CustomerInfo WHERE customer_email IN (SELECT customer_email  From CustomerInfo  WHERE Year = '2016') AND Year = '2017' GROUP BY Year").fetchall()
        connection.commit()
        print("q5")
        print(query_five)

        new_creation = cursor.execute("CREATE Table IF NOT EXISTS ExistingRev2016 AS SELECT SUM(Net_Revenue) AS ExistingCustomerRevenueFor2016 FROM CustomerInfo WHERE customer_email IN (SELECT customer_email FROM CustomerInfo WHERE Year = '2015') AND Year = '2016'")
        connection.commit()
        
        new_table = cursor.execute("CREATE Table IF NOT EXISTS ExistingRev2017 AS SELECT SUM(Net_Revenue) AS ExistingCustomerRevenueFor2017 FROM CustomerInfo WHERE customer_email IN (SELECT customer_email FROM CustomerInfo WHERE Year = '2016') AND Year = '2017'") 
        connection.commit()

        query_three = cursor.execute("SELECT ExistingCustomerRevenueFor2017 - ExistingCustomerRevenueFor2016 AS ExistingCustomerGrowth FROM ExistingRev2017, ExistingRev2016").fetchall()
        connection.commit()
        print("Q3")
        print(query_three)

        filter_one = (df['year'] == 2015)
        filter_two = (df['year'] == 2016)
        filter_three = (df['year'] == 2017)
        #print(df.loc[filter_one])
        #print(type(df.loc[filter_one]))

        total_2015 = df.loc[filter_one, 'net_revenue'].sum()
        total_2016 = df.loc[filter_two, 'net_revenue'].sum()
        total_2017 = df.loc[filter_three, 'net_revenue'].sum()

        Attrition_Loss = (total_2017 - total_2016) + (total_2016 - total_2015)
        print("Q4")

        print(Attrition_Loss)

        #print(total_2015)
        #print(total_2016)
        #print(total_2017)
        
        print("Q4")
        

        query_six = cursor.execute("SELECT SUM(Net_Revenue) AS ExistingCustomerRevenueFor2016 FROM CustomerInfo WHERE customer_email IN (SELECT customer_email  From CustomerInfo  WHERE Year = '2015') AND Year = '2016' GROUP BY Year").fetchall()
        connection.commit()
        print("Q6")
        print(query_six)


        query_seven = cursor.execute("SELECT COUNT(customer_email) AS TotalCustomersFor2017 FROM CustomerInfo WHERE Year = '2017'").fetchall()
        connection.commit()
        print("Q7")
        print(query_seven)

        query_eight = cursor.execute("SELECT COUNT(customer_email) AS TotalCustomersFor2016 FROM CustomerInfo WHERE Year = '2016'").fetchall()
        connection.commit()
        print("Q8")
        print(query_eight)

#       query_nine = cursor.execute("SELECT table1.customer_email AS NewCustomers FROM CustomerInfo table1, CustomerInfo table2 WHERE table1.Year = '2017' AND table2.Year != '2016'").fetchall()
#       connection.commit()
#       print(query_nine)

        query_nine_two = cursor.execute("SELECT COUNT(customer_email) AS NewCustomers  FROM CustomerInfo WHERE customer_email NOT IN (SELECT customer_email From CustomerInfo WHERE Year = '2016')").fetchall()
        connection.commit()
        print("Q9")
        print(query_nine_two)
        
        new_ten_table = cursor.execute("CREATE Table IF NOT EXISTS ExistingCustomer2016 AS SELECT Count(customer_email) AS LostCustomer2016 FROM CustomerInfo WHERE customer_email NOT IN (SELECT customer_email FROM CustomerInfo WHERE Year = '2016') AND Year = '2015'")
        
        new_creation = cursor.execute("CREATE Table IF NOT EXISTS ExistingCustomer2017 AS SELECT Count(customer_email) AS LostCustomer2017 FROM CustomerInfo WHERE customer_email IN (SELECT customer_email FROM CustomerInfo WHERE Year = '2017') AND Year = '2016'")
        
        connection.commit()

        query_ten = cursor.execute("SELECT (LostCustomer2016 + LostCustomer2017 ) AS LostCustomers FROM ExistingCustomer2016, ExistingCustomer2017").fetchall()
        print("Q10")
        print(query_ten)
    
        connection.close()

if __name__ == "__main__":
        InsertData()



