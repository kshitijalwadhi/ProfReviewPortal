# Prof Review Portal

This project was done as a part of Recruitment Assignment of Dev Club IITD - 2020. 

This portal will allow students to post reviews/comments about any professor or course.
This may help juniors to get a better idea of courses at the time of registration.

The project was built using Django Framework.

## Note to judging team of Dev Club: 
* The answers to the questions are there in the repo itself in the pdf format. 
  
  Link to that: [Answers - Dev Club](./Dev_Club_Recruitment.pdf)
* Please have a look at my github page for other projects involving frontend projects as well.

## Database Model

The main model of this app contains the class Review which has the following parameters:
* code - Used as Foreign Key
* prof - Used as Foreign Key
* comment - Text Field
* difficulty - IntegerField (1-10)
* contentquality - IntegerField(1-10)
* anonymous - Boolean Field 
* author - Foreign Key linking to user model
* date - DateTime Field

## I am using two apps here:
* Accounts 
    * For storing the user model
    * Taking care of Logging users in and Sign Up
* Review
    * Has 4 classes in models(dot)py: 
      * Prof : Stores prof information
      * Course : Stores course information
      * Warning : Stores the warnings received by a user (should have added this in Accounts app)
      * Review : Stores the actual Review content
    * It has pages that account for:
      * Adding new course, prof.
      * Adding new review.
      * Searching for existing reviews.


## Existing Features:
* Registration system(local for now).
* Add Reviews with the Course and Prof fields using auto-complete. (Only for logged in users)
* Using django_filters library for sorting reviews
* Profile Page for users to view their reviews and also view the messages received from admin.
* Option to post Review Anonymously
* Admin can take down any offensive Review and also send a warning to the user from the admin portal.
* Admin can also ban any user from logging in again. (Can be toggled, user profile is not actually deleted)
* Admin Portal also has an excellent portal to view the recent activity of the users.
* Also revamped the Reviews page in Admin Portal to allow for easy viewing.
* Report button for reviews.
* Like/Dislike feature for author of a review to allow a reader to judge the authors credibility.

## Upcoming Features:
* ~~Report button for reviews~~ (Added)
* ~~Like/Dislike feature for author of a review.~~ (Added)
* Verification of email ID during registration.
* Option to ban a user for a particular number of days instead of permanently.

## Instructions for firing the server up:
First install the dependencies, by cloning the repo and going into the directory containing, then open a terminal there and execute:

pip3 install -r requirements.txt

Open the terminal and from the root directory of this repo(the one containing manage(dot)py), execute the following command: 

python manage.py runserver

## Default ID and passwords:

* For Admin:
  * username: admin
  * password: admin
* For other users:
  * username: useri
  * password: passi
  * where i =1,2,3,4,5
