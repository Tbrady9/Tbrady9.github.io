# Project Three: Databases

## Inventory Tracker ##

The third project chosen for enhancement was a mobile app developed a year ago, in 2023, as part of my CS360 (Mobile Architect and Programming) course. The original task for this project was to develop a mobile android application for tracking inventory using the Java coding language, the Android Studio IDE, and an SQLite database. The requirements for the project were as follows:

    The app must have multiple screens
    The app must have a login and registration process
    The app must store and display inventory data
    The app must have a notification system

Both the original (TimBrady_InventoryTracker) as well as the enhanced (TimBrady_InventoryTracker_Enhanced) file folders are included above. At the time of developing the original, I had a very basic understanding of databases and ended up implementing two different databases to hold the different types of data (users and items). This works but is not best practice. My first enhancement was to correct that by merging the two into one database with two tables. I also enhanced interaction with the database by implementing full CRUD functionality for the users as it was only implemented for the items in the original. This also meant craeting a few more screens for users to view and edit the list of users. Below is a picture of the general table declaration for the newly merged database complete with autoincrementing ID numbers for each item and user entry to ensure unique entries.

![image](https://github.com/user-attachments/assets/e1ea4e5e-3cc8-4833-b1a4-404b7bdc366a)

Security was also enhanced from the original version. Slight input validation was already taking place in the original but it was taken a step further by implementing a authorization levels with employee roles. Each user must be assigned a role when their account is created. The Manager role allows a user to edit data related to the items and users while the Employee role has simple read-only access. Further security measures were taken by enhancing input validation on fields where it did not exist in the original. Future enhancements to security would also include password requirements but this was left off of the current enhanced version to allow for easier account registration and grading by my professor. Below is a portion of code showing example of increased security including the login confirmation process and one of the role-based authorization checks.

![image](https://github.com/user-attachments/assets/2c42668d-1467-4ba3-8304-b11d2b8385d6)

![image](https://github.com/user-attachments/assets/98dbd598-afb7-4539-9607-8d43b2996c9c)


Lastly, general cleanup was done in the form of improved comments and sectioning of the code as well as a more modern and interesting layout and design. Below you can see two of the screen transformations between the old and new versions.

Old version
![oldInventoryTracker](https://github.com/user-attachments/assets/f48a00f1-9338-4d03-a692-a7f227cde8a5)

New version
![newInventoryTracker](https://github.com/user-attachments/assets/90a403c1-8cce-4a73-a3d8-7c979e56e210)


## Instructions ##

### Objective and Requirements ###

This is an inventory tracking mobile application that allows users to create and maintain a list of items as well as a list of users for the app. Notifications can be setup to warn a user of low quantity for items.

This application was developed using the Java coding language in the Android Studio IDE. The emulator within Android Studio that was used for testing is a Pixel 5 phone with the 'R' Release Name (API Level 30). Though it will run on other devices and other API levels, this is the preferred setup. Below is a small video you can follow to set this up. You may need to click the down arrow beside API 30 to download it if it is not initially available to you.

![DeviceSetup](https://github.com/user-attachments/assets/4e177b68-f1be-434b-a1ea-148e7c546be7)

Upon running the app for the first time, no users will be stored in the database. Feel free to click on the button to create a new account and create a new account with the 'Manager' role. You can then go back to the login screen and login using your credentials. 

You will then be brought to a blank items screen where you can again go ahead and enter any amount of new items that you want by clicking on the button to add new items. When you click submit, the new item will be in your list. Each item is added as it's own card. Clicking on the button to go to the user screen will take you to a similar screen for a list of users where you can add or remove users as you please. Most of this functionality is only available to users with the Manager role as the Employees have read-only access. See the video below for an example of adding and removing an item.

![AddRemoveItem](https://github.com/user-attachments/assets/6b8e7a21-29de-46ce-82d6-72140bad7dd5)

Lastly is the notification feature. By clicking on the cog wheel in the top right corner of the item screen, you will be taken to the settings screen. There is a toggle to enable or disable notifications as well as a text field where you can set the minimum level of quantity for you to get a notification. For example, if you set this number to 10, you will receive a notification for any item that drops below 10 quantity. Feel free to go back to the item screen and edit an item's quantity to test it out!


Course Outcomes Displayed
---
### Develop a security mindset that anticipates adversarial exploits in software architecture and designs to expose potential vulnerabilities, mitigate design flaws, and ensure privacy and enhanced security of data and resources. ###

The implementation of authorization levels and enhanced input validation increase the security of this application. Replaceable parameters were also used to increase protection against SQL injection.


---
### Employ strategies for building collaborative environments that enable diverse audiences to support organizational decision-making in the field of computer science. ###

There were very large portions of code in the original that had no comments. This was improved in the enhanced version and greatly imrpoves the ability to collaborate and share with others.


