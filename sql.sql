DROP TABLE IF EXISTS developers;
DROP TABLE IF EXISTS projectmanagers;
DROP TABLE IF EXISTS customers;
DROP TABLE IF EXISTS industry;
DROP TABLE IF EXISTS developerprojects;
DROP TABLE IF EXISTS customerprojects;
DROP TABLE IF EXISTS projects;
DROP TABLE IF EXISTS releases;
DROP TABLE IF EXISTS issues;
DROP TABLE IF EXISTS branches;
DROP TABLE IF EXISTS mergerequests;

CREATE TABLE developers (
    e_employeeID DECIMAL(10, 0) NOT NULL, 
    e_username VARCHAR(20) NOT NULL, 
    e_password VARCHAR(45) NOT NULL, 
    e_email VARCHAR(45) NOT NULL, 
    e_createdDate DATETIME NOT NULL
);

CREATE TABLE projectmanagers (
    pm_employeeID DECIMAL(10, 0) NOT NULL,
    pm_projectID DECIMAL(10, 0) NOT NULL
);

CREATE TABLE customers (
    c_customerID DECIMAL(10, 0) NOT NULL, 
    c_industryID DECIMAL(3, 0), 
    c_name VARCHAR(45), 
    c_phone VARCHAR(45),
    c_address VARCHAR(45),
    c_createdDate DATETIME NOT NULL
);

CREATE TABLE industry (
    ind_industryID DECIMAL(3, 0) NOT NULL,
    ind_industryName VARCHAR(45) NOT NULL
);

CREATE TABLE developerprojects (
    dp_employeeID DECIMAL(10, 0) NOT NULL,
    dp_projectID DECIMAL(10, 0) NOT NULL
);

CREATE TABLE customerprojects (
    cp_customerID DECIMAL(10, 0) NOT NULL,
    cp_projectID DECIMAL(10, 0) NOT NULL
);

CREATE TABLE projects (
    p_projectID DECIMAL(10, 0) NOT NULL, 
    p_projectname VARCHAR(20) NOT NULL, 
    p_desc VARCHAR(512), 
    p_managerID DECIMAL(10, 0), 
    p_createdDate DATETIME NOT NULL,
    p_lastUpdate DATETIME NOT NULL
);

CREATE TABLE releases(
    r_projectID DECIMAL(10, 0) NOT NULL,
    r_releaseID DECIMAL(10, 0) NOT NULL,
    r_desc VARCHAR(512)
);

CREATE TABLE issues(
    i_projectID DECIMAL(10, 0) NOT NULL,
    i_issueID DECIMAL(10, 0) NOT NULL,
    i_desc VARCHAR(512)
);

CREATE TABLE branches(
    b_issueID DECIMAL(10, 0) NOT NULL,
    b_branchID DECIMAL(10, 0) NOT NULL,
    b_desc VARCHAR(512)
);

CREATE TABLE mergerequests(
    mr_branchID DECIMAL(10, 0) NOT NULL,
    mr_mergeID DECIMAL(10, 0) NOT NULL,
    mr_desc VARCHAR(512)
);

SELECT p_projectID
                    FROM projects
                    JOIN issues ON i_projectID = p_projectID
                    JOIN branches ON b_issueID = i_issueID
                    JOIN mergerequests ON b_branchID = mr_branchID
                    WHERE mr_mergeID = 2;