## Inspiration
We noticed that the UCI Campus Groups had an issue with a lack of tags in which to sort the clubs. Although there are tags, they do not break down the over 2500 clubs/organizations that are at the university. 
## What it does
Our program takes the data provided in UCI Campus Groups and reorganizes it in a way that allows for more variety of searches, according to the type of organization it is.
## How we built it
We utilized multiple programming languages and  python libraries to first, scrape through the html code of  Campus Groups, looking for the useful data to use in our sorting process.
## Challenges we ran into
We ran into many challenges when attempting to scrape Campus Groups for the needed data. We tried using RegEx, but once we later heard about BeautifulSoup, we quickly changed gears. Another issue came in when we encountered the dreaded zero-width space. Which is a space that has no length and is virtually invisible in python; it had been the source of many of our problems and once we figured it out, it made the rest of our journey a lot smoother.
## Accomplishments that we're proud of 
We were able to extract the extract data that we required from over 400,00 lines of html code as well as being able to create a functional website that can sort through our obtained data.
## What we learned
We learned a ton when it came to working with multiple languages (i.e. bridging the gap between them). Some of us also came in with little to no web design experience and were able to create and functioning published website. 
## What's next for The UCI Club Directory
One advantage that we have in our project is that it can be continually updated with our set up code as it uses the requests python library, also for daily updates to our sorter. So in the future, we will add more functionalities to our sorter, and more information on the clubs.

