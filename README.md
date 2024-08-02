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

Additional enhancements made to the original file were improved comments and a more polished visual experience. The old slideshow looked stretched out and had a color scheme that often blended the text together with the background. It looked messy and uninviting. The new visuals look more sleek and refined but, most of all, allow the user to more easily read the text of each slide.

Old Slideshow Layout
----
![oldSlideShow](https://github.com/user-attachments/assets/aac973af-7fe2-44a2-a687-45a3ba825ae2)


New Slideshow Layout
----
![image](https://github.com/user-attachments/assets/d9cf1cde-50d8-4f85-b6c0-822de302eff3)

Course Outcomes Displayed
---
### Demonstrate an ability to use well-founded and innovative techniques, skills, and tools in computing practices for the purpose of implementing computer solutions that deliver value and accomplish industry-specific goals. ###

The implementation of an array of objects is a well-founded technique that accomplished the goal of organizing data for easier sorting and retrieval. It allows all data to be centralized and flexible.


---
### Design, develop, and deliver professional-quality oral, written, and visual communications that are coherent, technically sound, and appropriately adapted to specific audiences and contexts. ###

The improved code with better organization, more complete commenting, and better maintainability is developed in a professional manner. The enhanced visuals of the project leads to a more professional appearance to the user.


---
### Design and evaluate computing solutions that solve a given problem using algorithmic principles and computer science practices and standards appropriate to its solution while managing the trade-offs involved in design choices. ###

Having a sorting option available where the user can re-sort the data on the fly was done by implementing sorting algorithms within action listeners. The sorting functions used adhere to best practices and standards because they are proven functions that were implemented with simplicity in mind to enhance maintainability.
