#Canada house

The purpose in this project is digging out raw data of selling houses from [this site](https://gopalsharma.ca/).
Then insert them into our local database and visualize them into our django-base website.
And at the end we are going to implement a learner agent that 
estimates price of houses by their features.
By the way this project is going to be developed only for fun and learning purpose.
Thanks to dear [Jadi](https://github.com/jadijadi) for this idea.

##Digging out data

The purpose data are observable at here:https://gopalsharma.ca/1000000-1500000 .
You can also see the hyper texts in your browser in inspect mode.
But you would not be able to receive the relative hyper texts by code simply with a request to the url.
And you will see the container of our purpose data with no content. 
(The container's html id is 'carmen' which would be empty).
So it's obvious that there's some js that downloads the content in the browser, as it arrives to the client side.
So we have to find that js code to see where it fetches data from.
I have implemented a django command that finds all of imported js files' urls.
You can simply use it this way:
```bash
python manage.py get-js-links
```
After taking a look at the js files or monitoring the calling urls from your browser,
you will find the api that exempts us from parsing html tags.

  
   