### Project Overview

 # 1. Features of Dataset for predicting the grades.


### Learnings from the project

 I learn the several features of the data sets for complete analysis i.e inculding read the data, display first 5 row of data sets,split the data into independent and target varaible and in the last how to split the data and to train and test the data sets.


### Approach taken to solve the problem

 Firstly i was not able to read the .csv file as provided it was showing file not found error then i tried to download the data file itself then its supposed to show the same after continuos trying i wondered it was due to api of the website then i copy the link address and pasted in the path then its simply works. 


### Challenges faced

 # 1.Read the data
data = pd.read_csv('https://storage.googleapis.com/ga-codeblock-live-prod-live-data/account/b21/2a7f53f8-19f6-45c7-9d74-560da9338b1a/b56/894b4c34-996b-4508-92cd-2407ac5bd182/file.csv')


# 2.Split the data into independent and target variable
X = data.drop('G3',1)
y = data.G3

#The above block of codes were the given challenges solution for this as mentioned below:-

#For the 1st #Read  the data 
The  provided filename was not in the directory first it was suppossed to be 'student_encoded.csv' , but it was not in the directory of the system then in thhe data section if found the data file i downloaded it and simply copied the link address and pasted the path section.

#This thing really turned the table and the FileNotFound error vanished.

#For the 2nd #Split the data into independent and target variable

X = data.drop(['G3'],1) - Initially it was same as now

but after changing the parameters to '( )' instead of '[ ]' it works .
 
 


### Additional pointers

 All this were the prework before the enrollment .  


