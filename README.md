# Prof Review Portal

This project was done as a part of Recruitment Assignment of Dev Club IITD - 2020. 

This portal will allow students to post reviews/comments about any professor or course.
This may help juniors to get a better idea of courses at the time of registration.

The project was built using Django Framework.


The main model of this app contains the class Review which has the following parameters:
* code - Used as Foreign Key
* prof - Used as Foreign Key
* comment - Text Field
* difficulty - IntegerField (1-10)
* contentquality - IntegerField(1-10)
* anonymous - Boolean Field 
* author - Foreign Key linking to user model
* date - DateTime Field
