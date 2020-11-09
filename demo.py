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
        branches = [] #
        customerprojects = []#
        customers = []#
        developerprojects = []#
        developers = []#
        industry = []#
        issues = []#
        mergerequests = []#
        projectmanagers = []#
        projects = []#
        releases = []#

        #branches
        # b_issueID, b_branchID ,  b_desc
        for i in range(0,5):
            branches.append([i,i,'kgkhgkhg'])

        #customerprojects
        # cp_customerID , cp_projectID
        for i in range(0,5):
            customerprojects.append([i,i])

        #customers
        # c_customerID , c_industryID , c_name , c_phone , c_address
        customers.append([0,0, 'BOB', '619-584-0293','fghjk Street' ])
        customers.append([1,1, 'kiwi', '345-524-4593','qwer Street' ])
        customers.append([2,2, 'MY', '159-214-1433','ashjg Street' ])
        customers.append([3,3, 'LOL', '363-214-7532','lpokj Street' ])
        customers.append([4,4, 'John', '098-234-7993','ikmn Street' ])

        #developerprojects
        #dp_employeeID , dp_projectID
        for i in range(0,5):
            developerprojects.append([i,i])
        
        #developers
        #e_employeeID , e_username , e_password , e_email , e_createdDate
        developers.append([0,'THjD', 'AASDFGH', 'sdfghj@gmail.com', '01-01-2020' ])
        developers.append([1,'ljgd', 'mjhredc', 'sawerty@gmail.com', '01-02-2020' ])
        developers.append([2,'ertytgfv', 'asdfgcxa', 'plmnbv@gmail.com', '01-03-2020' ])
        developers.append([3,'Tploiuyd', 'poiuytrsd', 'rtyuij@gmail.com', '01-04-2020' ])
        developers.append([4,'asdfg', 'oiuytrsdfg', 'mjytrsx@gmail.com', '01-05-2020' ])

        #industry
        #ind_industryID , ind_industryName
        industry.append([0,'Food'])
        industry.append([1,'tech'])
        industry.append([2,'water'])
        industry.append([3,'alc'])
        industry.append([4,'toys'])

        #issues
        #i_projectID , i_issueID , i_desc
        issues.append([0, 0, 'asdfghjk'])
        issues.append([1, 1, 'loiuytf'])
        issues.append([2, 2, 'vfghjres'])
        issues.append([3, 3, 'avcxswer'])
        issues.append([4, 4, 'poiuytrd'])


        #mergerequests
        #mr_branchID , mr_mergeID , mr_desc
        mergerequests.append([0,0,'oiuytrdsd'])
        mergerequests.append([1,1,'plkjytrd'])
        mergerequests.append([2,2,'wertyuhfd tresdfg'])
        mergerequests.append([3,3,'poiuytdf ewasdv'])
        mergerequests.append([4,4,'vcxsweftresad'])

        #projectmanagers
        #pm_employeeID , pm_projectID
        projectmanagers.append([0,0])
        projectmanagers.append([1,1])
        projectmanagers.append([2,2])
        projectmanagers.append([3,3])
        projectmanagers.append([4,4])

        #projects
        #p_projectID , p_projectname , p_desc , p_managerID , p_createdDate , p_lastUpdate 

        projects.append([0,'a', 'sdfghj', 0, '01-02-2020', '01-03-2020'])
        projects.append([1,'b', 'ljhgfdxdfv', 1, '02-02-2020', '02-03-2020'])
        projects.append([2,'c', 'wertyhgfc', 2, '03-02-2020', '03-03-2020'])
        projects.append([3,'d', 'lkjhgfd', 3, '04-02-2020', '04-03-2020'])
        projects.append([4,'e', 'ougfd', 4, '05-02-2020', '05-03-2020'])

        #releases
        #r_projectID , r_releaseID , r_descS
        releases.append([0,0,'sdfghjkiuyt'])
        releases.append([1,1,'asdfghjkedc'])
        releases.append([2,2,'smjuytdsxc'])
        releases.append([3,3,'cvbnmiuysd'])
        releases.append([4,4,'fghjkltgvedc'])




        sql = "INSERT INTO branches VALUES(?, ?, ?)"
        _conn.executemany(sql, branches)

        sql = "INSERT INTO  customerprojects VALUES(?, ?)"
        _conn.executemany(sql, customerprojects)

        sql = "INSERT INTO customers VALUES(?, ?, ?, ?, ?, ?)"
        _conn.executemany(sql, customers)

        sql = "INSERT INTO developerprojects VALUES(?, ?)"
        _conn.executemany(sql, developerprojects)
        
        sql = "INSERT INTO developers VALUES(?, ?, ?, ?, ?)"
        _conn.executemany(sql, developers)

        sql = "INSERT INTO industry VALUES(?, ?)"
        _conn.executemany(sql, industry)

        sql = "INSERT INTO issues VALUES(?, ?, ?)"
        _conn.executemany(sql, issues)

        sql = "INSERT INTO mergerequests VALUES(?, ?, ?)"
        _conn.executemany(sql, mergerequests)
        
        sql = "INSERT INTO projectmanagers VALUES(?, ?)"
        _conn.executemany(sql, projectmanagers)  

        sql = "INSERT INTO projects VALUES(?, ?, ?, ?, ?, ?)"
        _conn.executemany(sql, projects)  

        sql = "INSERT INTO releases VALUES(?, ?, ?)"
        _conn.executemany(sql, releases)  





        _conn.commit()
    except Error as e:
        _conn.rollback()
        print(e)
        
    print("++++++++++++++++++++++++++++++++++")


def createIssue(_conn, i_projectID, i_desc = ""):
    print("++++++++++++++++++++++++++++++++++")
    print("Create Issue")
    try:
        sql = """
                SELECT MAX(i_issueID)
                FROM issues;
            """
        args = [i_projectID]
        cur = _conn.cursor()
        cur.execute(sql)
        
        print("-------------------------------")
        print("Fetching largest issueID...")
        rows = cur.fetchall()
        if(rows[0] == (None,)):
            row = [0]
        else: 
            row = rows[0]
        i_issueID = row[0]
        print("Largest issueID = " + str(row[0]))
        i_issueID = str(int(i_issueID) + 1)
        print("Inserting issue #" + i_issueID + " into table...")
        sql = """
                INSERT INTO issues(i_projectID, i_issueID, i_desc)
                VALUES(?, ?, ?)
        """
        args = [i_projectID, i_issueID, i_desc]
        cur = _conn.cursor()
        cur.execute(sql, args)
    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")

def createBranch(_conn, b_issueID, b_desc = ""):
    print("++++++++++++++++++++++++++++++++++")
    print("Create Branch")
    try:
        sql = """
                SELECT MAX(b_branchID)
                FROM branches;
            """
        args = [b_issueID]
        cur = _conn.cursor()
        cur.execute(sql)
        
        print("-------------------------------")
        print("Fetching largest branchID...")
        rows = cur.fetchall()
        if(rows[0] == (None,)):
            row = [0]
        else: 
            row = rows[0]
        b_branchID = row[0]
        print("Largest branchID = " + str(row[0]))
        b_branchID = str(int(b_branchID) + 1)
        print("Inserting branch #" + b_branchID + " into table...")
        sql = """
                INSERT INTO branches(b_issueID, b_branchID, b_desc)
                VALUES(?, ?, ?)
        """
        args = [b_issueID, b_branchID, b_desc]
        cur = _conn.cursor()
        cur.execute(sql, args)
    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")

def createReleases(_conn, r_projectID, r_desc = ""):
    print("++++++++++++++++++++++++++++++++++")
    print("Create Realese")
    try:
        sql = """
                SELECT MAX(r_releaseID)
                FROM releases;
            """
        cur = _conn.cursor()
        cur.execute(sql)
        
        print("-------------------------------")
        print("Fetching largest releaseID...")
        rows = cur.fetchall()
        if(rows[0] == (None,)):
            row = [0]
        else: 
            row = rows[0]
        r_releaseID = row[0]
        print("Largest releaseID = " + str(row[0]))
        r_releaseID= str(int(r_releaseID) + 1)
        print("Inserting releases #" + r_releaseID + " into table...")
        sql = """
                INSERT INTO releases(r_projectID, r_releaseID, r_desc)
                VALUES(?, ?, ?)
        """
        args = [r_projectID, r_releaseID, r_desc]
        cur = _conn.cursor()
        cur.execute(sql, args)
    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
    print("++++++++++++++++++++++++++++++++++")

def createMergeRequest(_conn, mr_branchID, mr_desc = ""):
    print("++++++++++++++++++++++++++++++++++")
    print("Create Merge Request")
    try:
        sql = """
                SELECT MAX(mr_mergeID)
                FROM mergerequests;
            """
        args = [mr_branchID]
        cur = _conn.cursor()
        cur.execute(sql)
        
        print("-------------------------------")
        print("Fetching largest mergeID...")
        rows = cur.fetchall()
        if(rows[0] == (None,)):
            row = [0]
        else: 
            row = rows[0]
        mr_mergeID = row[0]
        print("Largest mergeID = " + str(row[0]))
        mr_mergeID = str(int(mr_mergeID) + 1)
        print("Inserting merge request #" + mr_mergeID + " into table...")
        sql = """
                INSERT INTO mergerequests(mr_branchID, mr_mergeID, mr_desc)
                VALUES(?, ?, ?)
        """
        args = [mr_branchID, mr_mergeID, mr_desc]
        cur = _conn.cursor()
        cur.execute(sql, args)
    except Error as e:
        _conn.rollback()
        print(e)
    print("success")
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
        
        createIssue(conn, 1, "yo issue fat")
        print()
        createBranch(conn, 1, "yo branch fat")
        print()
        createMergeRequest(conn, 1, "yo merge request fat")
        print()
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
