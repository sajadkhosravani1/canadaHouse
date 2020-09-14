# Canada house

The purpose in this project is digging out raw data of selling houses from [this site](https://gopalsharma.ca/).
Then insert them into our local database and visualize them into our django-base website.
And finally we are going to implement a learner agent that 
estimates price of houses by their features.
By the way this project is going to be developed only for fun and learning purpose.
Thanks to dear [Jadi](https://github.com/jadijadi) for this idea.

## Digging out data

The purpose data are observable at here:https://gopalsharma.ca/1000000-1500000 .
You can also see the hyper texts in your browser in inspect mode.
But you would not be able to receive the relative hyper texts by code simply with a request to the url.
And you will see the container of our purpose data with no content. 
(The container's tag-id is 'carmen' which would be empty).
So it's obvious that there's some js that downloads the content in the browser, as it arrives to the client side.
So we have to find that js code to see where it fetches data from.
I have implemented a django command that finds all of imported js files' urls.
You can simply use it this way:
```bash
python manage.py get-js-links
```
After taking a look at the js files or monitoring the calling urls from your browser,
you will find the api that exempts us from parsing html tags.

## Fetching records
I have implemented a manage.py command that fetches data from API 
and stores them into tables.
```address
/gopal/management/commands/fetch.py
```
You can simply use it as following.
```bash
python manage.py fetch <limit>
```
Use an integer instead \<limit> so api can limit fetched objects count.
We can make some configurations in fetch.py file.
#### lazy mode 
In lazy mode we would assume that when we bump into a case that we have already saved that means
we have already saved the rest, so breaks the loops. because the cases are sorted by date.
But when lazy mode is off, every single objects will be checked.
You can simply turn on/off lazy mode by changing the lazy variable to True/False in fetch.py file.

#### price limit
You can also config the min and max price to fetch 
and store as simple as editing the priceRange list variable in fetch.py file.
First item is Min value adn Second item is Max value in dollars.
