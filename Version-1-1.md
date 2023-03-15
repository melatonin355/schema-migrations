# Database Schema 1.1
This schema is still backwards compatible with 1.0 we are just adding  new table called Pets. 

Changelog:
- added table pets

## Table Structure

### User Table
The users table has the following columns:

|Column	|Type|	Description|
|-----------|-----------|-----------|
id|	INT|	Unique ID for each user|
name|	VARCHAR(255)|User's full name|
email|	VARCHAR(255)|	User's email address|


### Pets Table
|Column	|Type|	Description|
|-----------|-----------|-----------|
id|	INT|	Unique ID for each pet|
name|	VARCHAR(255)| pets full name|
type|	VARCHAR(255)|	type of pet dog, cat, bird|



