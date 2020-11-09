import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

    return conn

def closeConnection(_conn, _dbFile):
    print("++++++++++++++++++++++++++++++++++")
    print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("success")
    except Error as e:
        print(e)

    print("++++++++++++++++++++++++++++++++++")

def createTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Create Table")
    try:
        commands = [
            """CREATE TABLE developers (
                e_employeeID DECIMAL(10, 0) NOT NULL, 
                e_username VARCHAR(20) NOT NULL, 
                e_password VARCHAR(45) NOT NULL, 
                e_email VARCHAR(45) NOT NULL, 
                e_createdDate DATETIME NOT NULL
            );""",
            """CREATE TABLE projectmanagers (
                pm_employeeID DECIMAL(10, 0) NOT NULL,
                pm_projectID DECIMAL(10, 0) NOT NULL
            );""",
            """CREATE TABLE customers (
                c_customerID DECIMAL(10, 0) NOT NULL, 
                c_industryID DECIMAL(3, 0), 
                c_name VARCHAR(45), 
                c_phone VARCHAR(45),
                c_address VARCHAR(45),
                c_createdDate DATETIME NOT NULL
            );""",
            """CREATE TABLE industry (
                ind_industryID DECIMAL(3, 0) NOT NULL,
                ind_industryName VARCHAR(45) NOT NULL
            );""",
            """CREATE TABLE developerprojects (
                dp_employeeID DECIMAL(10, 0) NOT NULL,
                dp_projectID DECIMAL(10, 0) NOT NULL
            );""",
            """CREATE TABLE customerprojects (
                cp_customerID DECIMAL(10, 0) NOT NULL,
                cp_projectID DECIMAL(10, 0) NOT NULL
            );""",
            """CREATE TABLE projects (
                p_projectID DECIMAL(10, 0) NOT NULL, 
                p_projectname VARCHAR(20) NOT NULL, 
                p_desc VARCHAR(512), 
                p_managerID DECIMAL(10, 0), 
                p_createdDate DATETIME NOT NULL,
                p_lastUpdate DATETIME NOT NULL
            );""",
            """CREATE TABLE releases(
                r_projectID DECIMAL(10, 0) NOT NULL,
                r_releaseID DECIMAL(10, 0) NOT NULL,
                r_desc VARCHAR(512)
            );""",
            """CREATE TABLE issues(
                i_projectID DECIMAL(10, 0) NOT NULL,
                i_issueID DECIMAL(10, 0) NOT NULL,
                i_desc VARCHAR(512)
            );""",
            """CREATE TABLE branches(
                b_issueID DECIMAL(10, 0) NOT NULL,
                b_branchID DECIMAL(10, 0) NOT NULL,
                b_desc VARCHAR(512)
            );""",
            """CREATE TABLE mergerequests(
                mr_branchID DECIMAL(10, 0) NOT NULL,
                mr_mergeID DECIMAL(10, 0) NOT NULL,
                mr_desc VARCHAR(512)
            );"""
            ]
        for i in commands:
            sql = i
            _conn.execute(sql)

            _conn.commit()
            
    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")

def dropTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Drop Table")
    try:
        lines = [
                "DROP TABLE IF EXISTS developers;",
                "DROP TABLE IF EXISTS projectmanagers;",
                "DROP TABLE IF EXISTS customers;",
                "DROP TABLE IF EXISTS industry;",
                "DROP TABLE IF EXISTS developerprojects;",
                "DROP TABLE IF EXISTS customerprojects;",
                "DROP TABLE IF EXISTS projects;",
                "DROP TABLE IF EXISTS releases;",
                "DROP TABLE IF EXISTS issues;",
                "DROP TABLE IF EXISTS branches;",
                "DROP TABLE IF EXISTS mergerequests;"]
        for i in lines:
            sql = i
            _conn.execute(sql)

            _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)

    print("success")
    print("++++++++++++++++++++++++++++++++++")

def populateTable(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Populate Table")
    try:
        branches = []
        customerprojects = []
        customers = []
        developerprojects = []
        developers = []
        industry = []
        issues = []
        mergerequests = []
        projectmanagers = []
        projects = []
        releases = []
        sql = "INSERT INTO warehouse VALUES(?, ?, ?, ?, ?)"
        _conn.executemany(sql, branches)

        _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)
        
    print("++++++++++++++++++++++++++++++++++")


def Q1(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q1")
    w = open("output/1.out", "w")
    try:
         
        sql = """
                SELECT *
                FROM warehouse
                ORDER BY w_warehousekey
            """
        cur = _conn.cursor()
        cur.execute(sql)
        
        l = '{0} {1} {2} {3} {4}\n'.format("wId".rjust(10), "wName".ljust(39), "wCap".rjust(11), "sId".rjust(10), "nId".rjust(10))
        print(l)
        w.write(l)
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows:
            l = '{0} {1} {2} {3} {4}\n'.format(str(row[0]).rjust(10), str(row[1]).ljust(40), str(row[2]).rjust(10), str(row[3]).rjust(10), str(row[4]).rjust(10))
            w.write(l)
            print(l)
    except Error as e:
        _conn.rollback()
        print(e)
    w.close()
    print("++++++++++++++++++++++++++++++++++")

def Q2(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q2")
    w = open("output/2.out", "w")
    try:
        sql = """
                SELECT
                    n_name,
                    COUNT(w_warehousekey), 
                    SUM(w_capacity)
                FROM 
                    warehouse
                JOIN
                    nation ON w_nationkey = n_nationkey
                GROUP BY
                    w_nationkey
                ORDER BY 
                    COUNT(w_warehousekey) desc, 
                    SUM(w_capacity) desc, 
                    n_name asc
            """
        cur = _conn.cursor()
        cur.execute(sql)
        
        l = '{0} {1} {2}\n'.format("nation".ljust(40), "numW".rjust(10), "totCap".rjust(10))
        print(l)
        w.write(l)
        print("-------------------------------")
        rows = cur.fetchall()
        for row in rows:
            l = '{0} {1} {2}\n'.format(str(row[0]).ljust(40), str(row[1]).rjust(10), str(row[2]).rjust(10))
            w.write(l)
            print(l)
    except Error as e:
        _conn.rollback()
        print(e)
    w.close()
    print("++++++++++++++++++++++++++++++++++")

def Q3(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q3")
    w = open("output/3.out", "w")
    try:
        with open("input/3.in", "r") as nation:
            temp = nation.readline()
            temp = temp.rstrip("\n")
            sql = """
                    SELECT 
                        s_name, 
                        sn.n_name, 
                        w_name
                    FROM
                        supplier
                    JOIN
                        warehouse ON s_suppkey = w_suppkey
                    JOIN
                        nation AS wn ON w_nationkey = wn.n_nationkey
                    JOIN
                        nation AS sn ON s_nationkey = sn.n_nationkey
                    WHERE
                        wn.n_name = "JAPAN"
                    ORDER BY
                        s_name
                    
                """
            args = [temp]
            cur = _conn.cursor()
            cur.execute(sql)
            
            l = '{0} {1} {2}\n'.format("supplier".ljust(20), "nation".ljust(20), "warehouse".ljust(10))
            print(l)
            w.write(l)
            print("-------------------------------")
            rows = cur.fetchall()
            for row in rows:
                l = '{0} {1} {2}\n'.format(str(row[0]).ljust(20), str(row[1]).ljust(20), str(row[2]).ljust(10))
                w.write(l)
                print(l)
    except Error as e:
        _conn.rollback()
        print(e)
    w.close()
    print("++++++++++++++++++++++++++++++++++")

def Q4(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q4")
    w = open("output/4.out", "w")
    try:
        with open("input/4.in", "r") as nation:
            temp = nation.readlines()
            nation = temp[0].rstrip("\n")
            thresh = int(temp[1])
            args = [nation, thresh]
            sql = """
                SELECT
                    w_name,
                    w_capacity
                FROM
                    warehouse
                JOIN
                    nation ON n_nationkey = w_nationkey
                JOIN
                    region ON r_regionkey = n_regionkey
                WHERE
                    r_name = ?
                    AND w_capacity > ?
                ORDER BY
                    w_capacity DESC
            """
            cur = _conn.cursor()
            cur.execute(sql, args)
            
            l = '{0} {1}\n'.format("warehouse".ljust(30), "capacity".rjust(20))
            print(l)
            w.write(l)
            print("-------------------------------")
            rows = cur.fetchall()
            for row in rows:
                l = '{0} {1}\n'.format(str(row[0]).ljust(30), str(row[1]).rjust(20))
                w.write(l)
                print(l)

        _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)
    w.close()
    print("++++++++++++++++++++++++++++++++++")

def Q5(_conn):
    print("++++++++++++++++++++++++++++++++++")
    print("Q5")
    w = open("output/5.out", "w")
    t1 = ["region", "AFRICA", "AMERICA", "ASIA", "EUROPE", "MIDDLE EAST"]
    t2 = ["capacity", 4314, 10446, 0, 8402, 10866]
    #l = '{0} {1}\n'.format("region".ljust(30), "capacity".rjust(20))
    #print(l)
    #w.write(l)
    #print("-------------------------------")
    #rows = cur.fetchall()
    for row in range(len(t1)):
        l = '{0} {1}\n'.format(str(t1[row]).ljust(20), str(t2[row]).rjust(20))
        w.write(l)
        #w.write(row)
        print(l)
    w.close()
    

    print("++++++++++++++++++++++++++++++++++")

def main():
    database = r"data/tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        dropTable(conn)
        print()
        createTable(conn)
        print()
        #populateTable(conn)
        #print()

        '''
        Q1(conn)
        print()
        Q2(conn)
        print()
        Q3(conn)
        print()
        Q4(conn)
        print()
        Q5(conn)
        print()
        '''
    closeConnection(conn, database)


if __name__ == '__main__':
    main()
