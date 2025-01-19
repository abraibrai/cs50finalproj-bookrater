# cs50finalproj-bookrater
#### Video Demo: https://youtu.be/b2v1IYqQ5os

#### Description
The Bookrater app is designed to allow users to create an account, submit books they've read, and rate them. It then crowdsources the rankings and provides a chart of top ranked books by all users.


This app incorporates JavaScript, Python, and SQL using SQLAlchemy (I wanted to learn an ORM!) I've structured it to use Python for the backend and Javascript on the frontend, using Flask as my framework of choice. I also used Tailwind CSS.

Some structures I was able to replicate from finance.py, but also wanted to extend my learning in a few ways:
1) I wanted to learn an ORM (as mentioned above)
2) I wanted to incorporate alert flashes rather than an error route, using Javascript. An error route felt frankly weird to me from finance.py -- that's not how most real-world applications work.
3) I wanted to call an external API. In this case, I call the Google Books API to use ISBN as my standard to prevent duplicate book entries. (Honestly, this was maybe my smartest decision. I will need to explore more APIs over time, but when collecting user-input data, being able to verify it against a factual list like Google for consistency is really nice.)
4) I wanted to incorporate a more modern CSS library -- Tailwind CSS.

My biggest learnings were:
1) I drew out the structure of the app I wanted to build first. Drawing things out has been critical for me all course long. I like to plan.
2) I really, really, really hate styling. I get why people pay for out-of-the-box components. Styling SUCKS.
3) I created a bunch of scripts to populate my database and unpopulate it -- I played a lot with database structure and testing different setups and relationships. I can imagine this is much harder in a prod setting -- in my case I just deleted the tables and rebuilt them a lot, but you can't do that in a production environment.
4) Honestly, AI is kind of unreliable for helping. For example, at one point I tried to use ChatGPT to debug a data mapping issue, but it kept referencing a table column in the User_Books table called user_id, which doesn't exist. Luckily, my self-debugging is pretty good, and I basically only used AI for syntax errors.

Thank you for all of the learning in this course!!