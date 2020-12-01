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
    d_developerID INTEGER PRIMARY KEY, 
    d_username VARCHAR(20) NOT NULL, 
    d_password VARCHAR(45) NOT NULL, 
    d_email VARCHAR(45) NOT NULL, 
    d_createdDate DATETIME NOT NULL,
);



CREATE TABLE projectmanagers (
    pm_developerID DECIMAL(10, 0) NOT NULL,
    pm_projectID DECIMAL(10, 0) NOT NULL,
    FOREIGN KEY(pm_developerID) REFERENCES developers(d_developerID) ON DELETE CASCADE,
    FOREIGN KEY(pm_projectID) REFERENCES projects(p_projectID) ON DELETE CASCADE,
    PRIMARY KEY (pm_developerID, pm_projectID)
);


CREATE TABLE projects (
    p_projectID INTEGER PRIMARY KEY, 
    p_projectName VARCHAR(20) NOT NULL, 
    p_desc VARCHAR(512),
    p_createdDate DATETIME NOT NULL,
    p_lastUpdate DATETIME NOT NULL,
);





CREATE TABLE customers (
    c_customerID INTEGER PRIMARY KEY, 
    c_industryID DECIMAL(3, 0), 
    c_name VARCHAR(45),
    c_username VARCHAR(45),
    c_password VARCHAR(45), 
    c_phone VARCHAR(45),
    c_address VARCHAR(45),
    c_createdDate DATETIME NOT NULL,
    FOREIGN KEY(c_customerID) REFERENCES industy(ind_industryID) ON DELETE SET NULL,
    UNIQUE (c_customerID)
);
CREATE TABLE industry (
    ind_industryID INTEGER PRIMARY KEY,
    ind_industryName VARCHAR(45) NOT NULL,
    UNIQUE (ind_industryID)
);
CREATE TABLE developerprojects (
    dp_developerID DECIMAL(10, 0) NOT NULL,
    dp_projectID DECIMAL(10, 0) NOT NULL,
    FOREIGN KEY(dp_developerID) REFERENCES developers(d_developerID) ON DELETE CASCADE,
    FOREIGN KEY(dp_projectID) REFERENCES projects(p_projectID) ON DELETE CASCADE,
    UNIQUE (dp_developerID, dp_projectID)
);
CREATE TABLE customerprojects (
    cp_customerID DECIMAL(10, 0) NOT NULL,
    cp_projectID DECIMAL(10, 0) NOT NULL,
    FOREIGN KEY(cp_customerID) REFERENCES customers(c_customerID),
    FOREIGN KEY(cp_projectID) REFERENCES projects(p_projectID),
    UNIQUE (cp_customerID, cp_projectID)
);
CREATE TABLE releases(
    r_releaseID INTEGER PRIMARY KEY,
    r_projectID DECIMAL(10, 0) NOT NULL,
    r_desc VARCHAR(512),
    FOREIGN KEY(r_projectID) REFERENCES projects(p_projectID) ON DELETE CASCADE,
    UNIQUE (r_releaseID)
);
CREATE TABLE issues(
    i_issueID INTEGER PRIMARY KEY,
    i_projectID DECIMAL(10, 0) NOT NULL,
    i_desc VARCHAR(512),
    FOREIGN KEY(i_projectID) REFERENCES projects(p_projectID) ON DELETE CASCADE,
    UNIQUE (i_issueID)
);
CREATE TABLE branches(
    b_branchID INTEGER PRIMARY KEY,
    b_issueID DECIMAL(10, 0) NOT NULL,
    b_desc VARCHAR(512),
    FOREIGN KEY(b_issueID) REFERENCES issues(i_issueID) ON DELETE CASCADE
    UNIQUE (b_branchID)
);
CREATE TABLE mergerequests(
    mr_mergeID INTEGER PRIMARY KEY,
    mr_branchID DECIMAL(10, 0) NOT NULL,
    mr_desc VARCHAR(512),
    FOREIGN KEY(mr_branchID) REFERENCES branches(b_branchID) ON DELETE CASCADE,
    UNIQUE (mr_mergeID)
);
PRAGMA foreign_key_check;