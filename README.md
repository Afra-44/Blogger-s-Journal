# Blogger's Journal
#### Video Demo:  https://youtu.be/uDmlUr9ajkM

#### Description:
Blogger's Journal is a blogging site where you can explore interesting ideas and inspiring stories from all across the world. Here you can browse different categories of articles from people across the world and find what interests you the best. You can also create your own articles by signing in and share it with others. 
### Build With:
- HTML,CSS
- Bootstrap 5
- Python(Flask)
- JAvaScript
- SQLite3

###  Features
- User registration and signin
- Explore blog posts category wise 
- Create and post your own articles
- Sign up and manage your profile
- Edit your bio, cover photo, and profile photo
- Responsive design using Bootstrap 5

### Future plans
Plan on adding like, comment, follow functions and more features.


### how to run the code
- CLone the repository
- Navigate to the project folder `cd Blog`
- Make sure there is blog.db and it's .schema is
` CREATE TABLE users (
   username TEXT NOT NULL PRIMARY KEY  
   password NOT NULL   
   email NOT NULL
);
CREATE TABLE info (
    username TEXT PRIMARY KEY 
    profile_pic TEXT 
    bg_pic TEXT 
    about TEXT 
    description TEXT
    Contacts TEXT);
CREATE TABLE posts (
    number INTEGER PRIMARY KEY AUTOINCREMENT   
    username TEXT   
    title TEXT   
    desc TEXT   
    topic TEXT   
    pic TEXT   
    time CURRENT_TIMESTAMP   
    FOREIGN KEY (username) REFERENCES users(username)
); `
- install requirement.txt
- Run `flask --app blog.py run`
- visit the browser

### License
This project is licensed under the MIT License - see the LICENSE file for details.