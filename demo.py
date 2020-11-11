import sqlite3
from sqlite3 import Error


def openConnection(_dbFile):

    #print("Open database: ", _dbFile)

    conn = None
    try:
        conn = sqlite3.connect(_dbFile)
        print("established connection")
    except Error as e:
        print(e)



    return conn

def closeConnection(_conn, _dbFile):

    #print("Close database: ", _dbFile)

    try:
        _conn.close()
        print("closed connection")
    except Error as e:
        print(e)



def createTables(_conn):

    #print("Create Table")
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
                p_projectName VARCHAR(20) NOT NULL, 
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
        print("created tables")
    except Error as e:
        _conn.rollback()
        print(e)
    
def dropTables(_conn):

    #print("Drop Table")
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
        print("dropped all tables")
    except Error as e:
        _conn.rollback()
        print(e)

def populateTables(_conn):

    #print("Populate Table")
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
        # c_customerID , c_industryID , c_name , c_phone , c_address, c_createdDate
        customers.append([0,0, 'BOB', '619-584-0293','fghjk Street', '2020-04-15 03:55:18' ])
        customers.append([1,1, 'kiwi', '345-524-4593','qwer Street', '2020-05-15 03:55:18' ])
        customers.append([2,2, 'MY', '159-214-1433','ashjg Street', '2020-06-15 03:55:18' ])
        customers.append([3,3, 'LOL', '363-214-7532','lpokj Street', '2020-07-15 03:55:18' ])
        customers.append([4,4, 'John', '098-234-7993','ikmn Street' , '2020-10-15 03:55:18'])

        #developerprojects
        #dp_employeeID , dp_projectID
        for i in range(0,5):
            developerprojects.append([i,i])
        
        #developers
        #e_employeeID , e_username , e_password , e_email , e_createdDate
        developers.append([0,'Timmy', 'AASDFGH', 'sdfghj@gmail.com', '2020-01-11 03:55:18' ])
        developers.append([1,'Jimmy', 'mjhredc', 'sawerty@gmail.com', '2020-02-11 03:55:18' ])
        developers.append([2,'Kimmy', 'asdfgcxa', 'plmnbv@gmail.com', '2020-03-11 03:55:18' ])
        developers.append([3,'Paul', 'poiuytrsd', 'rtyuij@gmail.com', '2020-04-11 03:55:18' ])
        developers.append([4,'Ronny', 'oiuytrsdfg', 'mjytrsx@gmail.com', '2020-05-11 03:55:18' ])

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
        #p_projectID , p_projectName , p_desc , p_managerID , p_createdDate , p_lastUpdate 

        projects.append([0,'a', 'sdfghj', 0, '2020-02-01 03:55:18', '2020-02-01 03:55:18'])
        projects.append([1,'b', 'ljhgfdxdfv', 1, '2020-02-02 03:55:18', '2020-02-02 03:55:18'])
        projects.append([2,'c', 'wertyhgfc', 2, '2020-02-03 03:55:18', '2020-02-03 03:55:18'])
        projects.append([3,'d', 'lkjhgfd', 3, '2020-02-04 03:55:18', '2020-02-04 03:55:18'])
        projects.append([4,'e', 'ougfd', 4, '2020-02-05 03:55:18', '2020-02-05 03:55:18'])

        #releases
        #r_projectID , r_releaseID , r_descS
        releases.append([0,0,'sdfghjkiuyt'])
        releases.append([1,1,'asdfghjkedc'])
        releases.append([2,2,'smjuytdsxc'])
        releases.append([3,3,'cvbnmiuysd'])
        releases.append([4,4,'fghjkltgvedc'])




        sql = "INSERT INTO branches VALUES(?, ?, ?)"
        _conn.executemany(sql, branches)
        _conn.commit()

        sql = "INSERT INTO  customerprojects VALUES(?, ?)"
        _conn.executemany(sql, customerprojects)
        _conn.commit()

        sql = "INSERT INTO customers VALUES(?, ?, ?, ?, ?, ?)"
        _conn.executemany(sql, customers)
        _conn.commit()

        sql = "INSERT INTO developerprojects VALUES(?, ?)"
        _conn.executemany(sql, developerprojects)
        _conn.commit()
        
        sql = "INSERT INTO developers VALUES(?, ?, ?, ?, ?)"
        _conn.executemany(sql, developers)
        _conn.commit()

        sql = "INSERT INTO industry VALUES(?, ?)"
        _conn.executemany(sql, industry)
        _conn.commit()

        sql = "INSERT INTO issues VALUES(?, ?, ?)"
        _conn.executemany(sql, issues)
        _conn.commit()
        
        sql = "INSERT INTO mergerequests VALUES(?, ?, ?)"
        _conn.executemany(sql, mergerequests)
        _conn.commit()
        
        sql = "INSERT INTO projectmanagers VALUES(?, ?)"
        _conn.executemany(sql, projectmanagers)  
        _conn.commit()

        sql = "INSERT INTO projects VALUES(?, ?, ?, ?, ?, ?)"
        _conn.executemany(sql, projects)  
        _conn.commit()

        sql = "INSERT INTO releases VALUES(?, ?, ?)"
        _conn.executemany(sql, releases)  
        _conn.commit()

        print("populated tables")
    except Error as e:
        _conn.rollback()
        print(e)
   

   
def createProject(_conn, p_projectName, p_desc = "", p_managerID = ""):

    #print("Create Project")
    try:
        sql = """
                SELECT MAX(p_projectID)
                FROM projects;
            """
        cur = _conn.cursor()
        cur.execute(sql)
        _conn.commit()

        rows = cur.fetchall()
        if(rows[0] == (None,)):
            row = [0]
        else: 
            row = rows[0]
        p_projectID = row[0]

        p_projectID = str(int(p_projectID) + 1)
        
        sql = """
                SELECT datetime('now');
            """
        cur = _conn.cursor()
        cur.execute(sql)
        _conn.commit()

        rows = cur.fetchall()
        if(rows[0] == (None,)):
            row = [0]
        else: 
            row = rows[0]
        p_createdDate = p_lastUpdate = row[0]

        
        

        sql = """
                INSERT INTO projects(p_projectID, p_projectName, p_desc, p_createdDate, p_lastUpdate)
                VALUES(?, ?, ?, ?, ?)
        """
        args = [p_projectID, p_projectName, p_desc, p_createdDate, p_lastUpdate]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        
        if(len(p_managerID) != 0):
            setProjectManager(_conn, p_projectID, p_managerID)
        print("created project: " + str(p_projectID))
    except Error as e:
        _conn.rollback()
        print(e)
    
def setProjectName(_conn, p_projectID, p_projectName):
    #print("Setting project name")
    try:
        sql = """
            UPDATE projects
            SET p_projectName = ?
            WHERE p_projectID = ?;
        """
        args = [p_projectName, p_projectID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        
        updateProject(_conn, p_projectID)
        print("set project: " + str(p_projectID) + "'s name to: " + p_projectName)
    except Error as e:
        _conn.rollback()
        print(e)

def setProjectManager(_conn, p_projectID, p_managerID):
    #print("Setting project manager")
    try:
        sql = """
            UPDATE projects
            SET p_managerID = ?
            WHERE p_projectID = ?;
        """
        args = [p_managerID, p_projectID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        
        updateProject(_conn, p_projectID)
        print("set project: " + str(p_projectID) + "'s manager to: " + str(p_managerID))
    except Error as e:
        _conn.rollback()
        print(e)

def setProjectDescription(_conn, p_projectID, p_desc):
    #print("Setting project description")
    try:
        sql = """
            UPDATE projects
            SET p_desc = ?
            WHERE p_projectID = ?;
        """
        args = [p_desc, p_projectID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        
        updateProject(_conn, p_projectID)
        print("set project: " + str(p_projectID) + "'s description to: " + p_desc)
    except Error as e:
        _conn.rollback()
        print(e)

def updateProject(_conn, p_projectID):

    try:
        sql = """
                SELECT datetime('now');
            """
        cur = _conn.cursor()
        cur.execute(sql)

        rows = cur.fetchall()
        if(rows[0] == (None,)):
            row = [0]
        else: 
            row = rows[0]
        p_lastUpdate = row[0]

        
        sql = """
                UPDATE projects
                SET p_lastUpdate = ?
                WHERE p_projectID = ?;
        """
        
        args = [p_lastUpdate, p_projectID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        #print("updated project: " + str(p_projectID))
    except Error as e:
        _conn.rollback()
        print(e)

def getProjectID(_conn, p_projectName):
    try:
        sql = """
                    SELECT p_projectID
                    FROM projects
                    WHERE p_projectName = ?;
            """
        args = [p_projectName]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        rows = cur.fetchall()
        if(rows[0] == (None,)):
            return -1
        else: 
            row = rows[0]
        return row[0]
    except Error as e:
        _conn.rollback()
        print(e)



def createRelease(_conn, r_projectID, r_desc = ""):

    #print("Create Realese")
    try:
        sql = """
                SELECT MAX(r_releaseID)
                FROM releases;
            """
        cur = _conn.cursor()
        cur.execute(sql)
        _conn.commit()
        

        rows = cur.fetchall()
        if(rows[0] == (None,)):
            row = [0]
        else: 
            row = rows[0]
        r_releaseID = row[0]

        r_releaseID= str(int(r_releaseID) + 1)

        sql = """
                INSERT INTO releases(r_projectID, r_releaseID, r_desc)
                VALUES(?, ?, ?)
        """
        args = [r_projectID, r_releaseID, r_desc]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        print("created release: " + str(r_releaseID))
    except Error as e:
        _conn.rollback()
        print(e)
 


def createIssue(_conn, i_projectID, i_desc = ""):

    #print("Create Issue")
    try:
        sql = """
                SELECT MAX(i_issueID)
                FROM issues;
            """
        cur = _conn.cursor()
        cur.execute(sql)
        _conn.commit()
        

        rows = cur.fetchall()
        if(rows[0] == (None,)):
            row = [0]
        else: 
            row = rows[0]
        i_issueID = row[0]

        i_issueID = str(int(i_issueID) + 1)

        sql = """
                INSERT INTO issues(i_projectID, i_issueID, i_desc)
                VALUES(?, ?, ?)
        """
        args = [i_projectID, i_issueID, i_desc]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        print("created issue: " + str(i_issueID) + " for project: " + str(i_projectID))
    except Error as e:
        _conn.rollback()
        print(e)
  
def setIssueDescription(_conn, i_issueID, i_desc):
    #print("Setting issue description")
    try:
        sql = """
            UPDATE issues
            SET i_desc = ?
            WHERE i_issueID = ?;
        """
        args = [i_desc, i_issueID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        
        p_ID = getProjectIDFromIssue(_conn, i_issueID)
        if(p_ID != -1):
            updateProject(_conn, p_ID)
        print("set issue: " + str(i_issueID) + "'s description to: " + i_desc)
    except Error as e:
        _conn.rollback()
        print(e)

def mergeIssue(_conn, i_issueID):
    try:
        sql = """DELETE FROM issues WHERE i_issueID  = ?"""

        p_ID = getProjectIDFromIssue(_conn, i_issueID)
        if(p_ID != -1):
            updateProject(_conn, p_ID)
        
        rows = getAllBranchesFromIssue(_conn, i_issueID)
        for row in rows:
            mergeBranch(_conn, row[0])
        
        cur = _conn.cursor()
        cur.execute(sql, [i_issueID])
        _conn.commit()
        cur = _conn.cursor()


        
        print("merged issue: " + str(i_issueID))

    except Error as e:
        _conn.rollback()
        print(e)

def getProjectIDFromIssue(_conn, i_issueID):
    try:
        sql = """
                SELECT p_projectID
                FROM projects
                JOIN issues ON i_projectID = p_projectID
                WHERE i_issueID = ?;
            """
        args = [i_issueID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        rows = cur.fetchall()
        if(len(rows) == 0):
            return -1
        if(rows[0] == (None,)):
            return -1
        else: 
            row = rows[0]
        return row[0]
    except Error as e:
        _conn.rollback()
        print(e)

def getAllIssuesForProject(_conn, p_projectID):
    try:
        sql = """
                SELECT i_issueID
                FROM issues
                JOIN projects ON p_projectID = i_projectID
                WHERE p_projectID = ?;
        """
        cur = _conn.cursor()
        cur.execute(sql, [p_projectID])
        _conn.commit()
        
        rows = cur.fetchall()
        return rows
        
        
    except Error as e:
        _conn.rollback()
        print(e)



def createBranch(_conn, b_issueID, b_desc = ""):

    #print("Create Branch")
    try:
        sql = """
                SELECT MAX(b_branchID)
                FROM branches;
            """
        cur = _conn.cursor()
        cur.execute(sql)
        _conn.commit()
        

        rows = cur.fetchall()
        if(rows[0] == (None,)):
            row = [0]
        else: 
            row = rows[0]
        b_branchID = row[0]

        b_branchID = str(int(b_branchID) + 1)

        sql = """
                INSERT INTO branches(b_issueID, b_branchID, b_desc)
                VALUES(?, ?, ?)
        """
        args = [b_issueID, b_branchID, b_desc]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        print("created branch: " + str(b_branchID) + " for issue: " + str(b_issueID))
    except Error as e:
        _conn.rollback()
        print(e)

def setBranchDescription(_conn, b_branchID, b_desc):
    #print("Setting issue description")
    try:
        sql = """
            UPDATE branch
            SET b_desc = ?
            WHERE b_branchID = ?;
        """
        args = [b_desc, b_branchID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        
        p_ID = getProjectIDFromBranch(_conn, b_branchID)
        if(p_ID != -1):
            updateProject(_conn, p_ID)
        #updateProject(_conn, branchID)
        print("set branch: " + str(b_branchID) + "'s description to: " + b_desc)
    except Error as e:
        _conn.rollback()
        print(e)

def mergeBranch(_conn, b_branchID):
    try:
        sql = """DELETE FROM branches WHERE b_branchID  = ?"""

        p_ID = getProjectIDFromBranch(_conn, b_branchID)
        if(p_ID != -1):
            updateProject(_conn, p_ID)
            
        rows = getAllMergeRequestsFromBranch(_conn, b_branchID)
        for row in rows:
            mergeMergeRequest(_conn, row[0])
            
        cur = _conn.cursor()
        cur.execute(sql, [b_branchID])
        _conn.commit()
        cur = _conn.cursor()
        
        
        
        print("merged branch: " + str(b_branchID))

    except Error as e:
        _conn.rollback()
        print(e)

def getProjectIDFromBranch(_conn, b_branchID):
    try:
        sql = """
                SELECT p_projectID
                FROM projects
                JOIN issues ON i_projectID = p_projectID
                JOIN branches ON b_issueID = i_issueID
                WHERE b_branchID = ?;
            """
        args = [b_branchID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        rows = cur.fetchall()
        if(len(rows) == 0):
            return -1
        if(rows[0] == (None,)):
            return -1
        else: 
            row = rows[0]
        return row[0]
    except Error as e:
        _conn.rollback()
        print(e)

def getAllBranchesFromIssue(_conn, i_issueID):
    try:
        sql = """
                SELECT b_branchID
                FROM branches
                JOIN issues ON i_issueID = b_issueID
                WHERE i_issueID = ?;
        """
        cur = _conn.cursor()
        cur.execute(sql, [i_issueID])
        _conn.commit()
        
        rows = cur.fetchall()
        return rows
        
        
    except Error as e:
        _conn.rollback()
        print(e)



def createMergeRequest(_conn, mr_branchID, mr_desc = ""):

    #print("Create Merge Request")
    try:
        sql = """
                SELECT MAX(mr_mergeID)
                FROM mergerequests;
            """
        cur = _conn.cursor()
        cur.execute(sql)
        _conn.commit()
        

        rows = cur.fetchall()
        if(rows[0] == (None,)):
            row = [0]
        else: 
            row = rows[0]
        mr_mergeID = row[0]

        mr_mergeID = str(int(mr_mergeID) + 1)

        sql = """
                INSERT INTO mergerequests(mr_branchID, mr_mergeID, mr_desc)
                VALUES(?, ?, ?)
        """
        args = [mr_branchID, mr_mergeID, mr_desc]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        print("created merge request: " + str(mr_mergeID) + " for branch: " + str(mr_branchID))
    except Error as e:
        _conn.rollback()
        print(e)

def setMergeRequestDescription(_conn, mr_mergeID, mr_desc):
    #print("Setting merge request description")
    try:
        sql = """
            UPDATE mergerequests
            SET mr_desc = ?
            WHERE mr_mergeID = ?;
        """
        args = [mr_desc, mr_mergeID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        
        p_ID = getProjectIDFromMR(_conn, mr_mergeID)
        if(p_ID != -1):
            updateProject(_conn, p_ID)
        print("set merge request: " + str(mr_mergeID) + "'s description to: " + mr_desc)
    except Error as e:
        _conn.rollback()
        print(e)

def mergeMergeRequest(_conn, mr_mergeID):
    try:
        sql = """DELETE FROM mergerequests WHERE mr_mergeID  = ?"""
        p_ID = getProjectIDFromMR(_conn, mr_mergeID)
        if(p_ID != -1):
            updateProject(_conn, p_ID)
        cur = _conn.cursor()
        cur.execute(sql, [mr_mergeID])
        _conn.commit()
        
        print("merged merge request: " + str(mr_mergeID))

    except Error as e:
        _conn.rollback()
        print(e)

def getProjectIDFromMR(_conn, mr_mergeID):
    try:
        sql = """
                SELECT p_projectID
                FROM projects
                JOIN issues ON i_projectID = p_projectID
                JOIN branches ON b_issueID = i_issueID
                JOIN mergerequests ON mr_branchID = b_branchID
                WHERE mr_mergeID = ?;
            """
        args = [mr_mergeID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        rows = cur.fetchall()
        if(len(rows) == 0):
            return -1
        if(rows[0] == (None,)):
            return -1
        else: 
            row = rows[0]
        return row[0]
    except Error as e:
        _conn.rollback()
        print(e)

def getAllMergeRequestsFromBranch(_conn, b_branchID):
    try:
        sql = """
                SELECT mr_mergeID
                FROM mergerequests
                JOIN branches ON b_branchID = mr_branchID
                WHERE b_branchID = ?;
        """
        cur = _conn.cursor()
        cur.execute(sql, [b_branchID])
        _conn.commit()
        
        rows = cur.fetchall()
        return rows
        
        
    except Error as e:
        _conn.rollback()
        print(e)



def getEmployeeID(_conn, e_username):
    try:
        sql = """
                    SELECT e_employeeID
                    FROM developers
                    WHERE e_username LIKE ?;
            """
        args = [e_username]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        rows = cur.fetchall()
        if(rows[0] == (None,)):
            return -1
        else: 
            row = rows[0]
        return row[0]
    except Error as e:
        _conn.rollback()
        print(e)



def getCustomerID(_conn, c_name):
    try:
        sql = """
                    SELECT c_customerID
                    FROM customers
                    WHERE c_name LIKE ?;
            """
        args = [c_name]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        rows = cur.fetchall()
        if(rows[0] == (None,)):
            return -1
        else: 
            row = rows[0]
        return row[0]
    except Error as e:
        _conn.rollback()
        print(e)

def setCustomerIndustry(_conn, c_customerID, c_industry):
    try:
        sql = """
            UPDATE customers
            SET c_industry = ?
            WHERE c_customerID = ?;
        """
        args = [c_industry, c_customerID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        
        p_ID = getProjectIDFromMR(_conn, c_customerID)
        if(p_ID != -1):
            updateProject(_conn, p_ID)
        print("set merge request: " + str(c_customerID) + "'s description to: " + c_industry)
    except Error as e:
        _conn.rollback()
        print(e)

def setCustomerCustomerName(_conn, c_customerID, c_name):
    try:
        sql = """
            UPDATE customers
            SET c_name = ?
            WHERE c_customerID = ?;
        """
        args = [c_name, c_customerID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        
        p_ID = getProjectIDFromMR(_conn, c_customerID)
        if(p_ID != -1):
            updateProject(_conn, p_ID)
        print("set merge request: " + str(c_customerID) + "'s description to: " + c_name)
    except Error as e:
        _conn.rollback()
        print(e)

def setPhone(_conn, c_customerID, c_phone):
    try:
        sql = """
            UPDATE customers
            SET c_phone = ?
            WHERE c_customerID = ?;
        """
        args = [c_phone, c_customerID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        
        p_ID = getProjectIDFromMR(_conn, c_customerID)
        if(p_ID != -1):
            updateProject(_conn, p_ID)
        print("set merge request: " + str(c_customerID) + "'s description to: " + c_phone)
    except Error as e:
        _conn.rollback()
        print(e)

def setCustomerAddress(_conn, c_customerID, c_address):
    try:
        sql = """
            UPDATE customers
            SET c_address = ?
            WHERE c_customerID = ?;
        """
        args = [c_address, c_customerID]
        cur = _conn.cursor()
        cur.execute(sql, args)
        _conn.commit()
        
        p_ID = getProjectIDFromMR(_conn, c_customerID)
        if(p_ID != -1):
            updateProject(_conn, p_ID)
        print("set merge request: " + str(c_customerID) + "'s description to: " + c_address)
    except Error as e:
        _conn.rollback()
        print(e)



def main():
    database = r"data/tpch.sqlite"

    # create a database connection
    conn = openConnection(database)
    with conn:
        
        # SQL Connections
        dropTables(conn)
        print()
        createTables(conn)
        print()
        populateTables(conn)
        print()
        
        # Adding to table with all fields
        print("==================================")
        createIssue(conn, 1, "yo issue fat")
        print()
        
        
        createBranch(conn, 1, "yo branch fat")
        print()
        
        
        createMergeRequest(conn, 1, "yo merge request fat")
        print()
        
        
        createProject(conn, "devlogs")
        print()
        
        # Recursive merging and adding to table with minimum fields
        print("==================================")
        
        createIssue(conn, 3)
        print()
        
        createBranch(conn, 6)
        print()
        
        createBranch(conn, 6)
        print()
        
        createMergeRequest(conn, 6)
        print()
        
        createMergeRequest(conn, 6)
        print()
        
        createMergeRequest(conn, 6)
        print()
        
        mergeIssue(conn, 6)
        print()
        
        # Modifying properties
        print("==================================")
        
        
        projID = getProjectID(conn, "devlogs")
        setProjectDescription(conn, projID, "create logs for developers!")
        print()

        
        setProjectName(conn, projID, "Developer Logging")
        print()
        
        
        empID = getEmployeeID(conn, "Ronny")
        setProjectManager(conn, projID, empID)
        print()
        
        # Standalone merging
        print("==================================")
        
        
        mergeMergeRequest(conn, 2)
        print()
        
        
        mergeBranch(conn, 2)
        print()
        
        
        mergeIssue(conn, 2)
        print()
        
    closeConnection(conn, database)


if __name__ == '__main__':
    main()
