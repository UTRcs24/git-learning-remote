# CS-2450 SOFTWARE ENGINEERING JOURNAL
---
## 14, January, 2025
### INIT()
I would center the title, but I won't bother with doing that in Markdown yet. I have a few ideas for our project throughout the semester. My main idea that I have currently is a social media platform
for world leaders. The platform will be advertised a method of ensuring world peace, but really it's to make world leaders mad at each other and ensure conflicts which will bring our company, Lockheed 
Marvin (Sidenote, I should have suggested Seaweed Marlin. Why didn't I come up with that earlier? It would have been much more humorous.), more profits. My other idea is to create a website called 
MageBook. It will be a social media service that anyone connected to the Planes-Wide-Orb can use. Any magic user from any universe who's connected to the orb could use it. Other than these two ideas, I 
don't have much at the moment, and thus ends my first entry.

## 16, January, 2025, 2:56
### Small Update
I just got this repo on my desktop at home, which is currently running Ubuntu. This entry is mostly to make sure I set up my repo, keys, and everything correctly before I clone the team repo. I just
want to document another idea I have as well, though. I'm thinking that it could be a fun project, in the future, to create a new programming language. Nothing too complex because I can't think of
a reason to do something to complex. What I'm thinking of is pseudo-assembly. A language that works like any other assembly language, but all of it's functions are named appropriately as to be less
intimidating to someone learning assembly for the first time. I'm thinking that I could write it in Python, and of course all of the functions would just translate to something in Python. It wouldn't
allow the user to write assembly code that gets compiled straight to the processor; it would be more like an emulator. Everything that looks like it's in assembly would simply be fake: imitations of
assembly rules. The stack would simply be a python list that the user has to reserve. There will be 31 'registers', all mapped to variables. Why make this limited language? It could be a way to
introduce elementary schoolers and middle schoolers to assembly. They wouldn't need to set up any complex tools or worry configuring things on the command-line, nor would they need to worry about
unintuitive names for things. Just a thought.

## 06, February, 2025, 16:54
### First Update in Awhile
This is the first update I've had in awhile. There really hasn't been anything of note to jot down, and as a result, I haven't updated this journal in a minute. We've started going over diagrams in
class. This coupled with the requirements document has given some form to our amorphous blob of a software project. With diagrams, I can now more easily piece together what exactly we will need to
create, and in what order. I also have a better idea of how to code the back-end of things. I'm thinking that each user will have a number of fields associated with them in the data base. The main 
Python code will pull this info and use it as needed. We are going to call the social media platform MyState. As for my other project, I have yet to have much will to work on it considering everything
else I'm already doing. I plan on working on it a bit more as summer approaches. I at least want all of the design finished by April so that I can know exactly what technologies I need to learn how to 
use.

## 19, February, 2025, 13:06
### Beginning of Work
We recently pitched our project. To do that, we heavily discussed the project architecture last week. After discussing things, I think I know exactly how I'm going to do the database. I'm going with
TinyDB. The overarching datatype is going to be a user. Each user will contain a list of posts. Each post contains an author, associated image URLs, associated video URLs, text content, reactions, 
and a list of replies. Each reply will contain an author and associated picture URLs. Each user will also have a background color, foreground color, and text color on their page. They will have an image 
URL for their flag. They will also have a list of strings which are their favorite things. They will have an allies list which is just a list of users. In addition, they'll have a messages list. Each 
message will have an author, a recipient, any associated image or video URLs, and content.

## 25, February, 2025, 13:49
### Git Issues
When you hear "issue" and "Github", you probably don't think of going things going wrong. But in this instance, an issue denotes something going wrong, way wrong. While working on the database, I tried to merge my branch onto our main branch. However, there was an issue. To try and resolve the issue, I did a git pull, which put a bunch of junk from other projects within my directory. In trying to fix it, I somehow got the junk on our team's main branch on Github. So, I deleted the stuff locally and tried to merge the changes back in, but that was no help, for the changes were too complex to edit on the web. Thus, I had to go to Jeff's office and try to resolve the issue in the command line. Eventually, the issue was resolved and the directory is now back to normal. I deleted my local instance of the repo, recloned the remote instance, and now hopefully, it should be happy trails from here on out. Right? Right?

## 20, March, 2025, 18:37
###User Initialization
For the longest time, I had a huge issue when trying to have two different types of users on MyState. The login page struggled greatly with having two different types of users in the database. I had
a table for regular users, and I had a table for secondary users. However, I've figured out how to fix this! Instead of having two tables, I simply added a new field to users: 'associated_user'. If
the associated user is None, then that means that they are a primary user. If they're a primary user, when they login, they will see their home page, along with the button to edit it, the friends list,
etc. However, if they are a secondary user, then when logging in, they'll see an altered version of their associated users homepage. They'll see posts and be able to react and comment, but they'll be
unable to edit the webpage or see a friends list.

## 26, March, 2025, 17:23
###Refactoring
When refactoring the tic-tac-toe game, I've decided that I'm going to do three for loops for the winner function. It will be three nested for loops for a total of six for loops. The for loop for
diagonal wins was a pain, but I think I've got it. As for everything else, I've added some comments and changed function names. The most troublesome thing regarding naming was the name of the
board. The board was simply called 'b'. Not only is this non-descriptive, but when changing it to board, I had to just keep rerunning the program until I ran to the 'b not initialized' error. This is
because since b is a single letter, it shows far too often in any search. Note to self, avoid naming a variable as a single letter as much as possible.
