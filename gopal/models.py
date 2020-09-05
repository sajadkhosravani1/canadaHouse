from django.db import models

# data type hierarchy sample:
# to check a sample with if of : <id> --> https://gopalsharma.ca/listing/R<id>/
objectSample = {'mlsListingID': 'R2396512',
       'address': '# 4301 1289 Hornby Street, Vancouver, BC',
       'city': 'Vancouver',
       'community': 'Downtown VW',
       'state': 'BC',
       'ownership': 'Freehold Strata',
       'publicRemarks': "Great opportunity to own a dream home in a timeless architectural gem - ONE BURRARD PLACE. Located in the heart of downtown Vancouver. This functional two bedrooms with flex space above 43 floor features with finest fixtures & finishes including lofty 9' ceilings, floor to ceiling glazed windows, wide plank hardwood flooring throughout, motion sensor lighting in closets, central A/C, automated smart home controls & list go on. Building with five star amenities including full length lap pool, sauna, steam rooms, fitness center, 30,000 sq.ft of private clubhouse, secured floor-by-floor fob controlled, 24/7 butler concierge services. Mins walk to skytrain, Yaletown, shopping, restaurants. Enjoy City skyline and English Bay day & night. Truly a glamorous & luxurious living!",
       'price': 1380000,
       'bedrooms': 2,
       'baths': 2,
       'dateListed': '2019-08-13 07:00:00',
        'media': ['abe42153f7e2ca693da4d6388d640cde427cbb47.jpg', 'f53cb3ec6e4fa4cbda81c159d5747f510895bf98.jpg', 'aad98da13c7c90d1f9da0d5a8de029c5185657c5.jpg', 'bf5136f25f8e8a770fdaccff957e6c6c89d1325c.jpg', '371ddc31cb580877e2ff495f1a398c9ef9f11a72.jpg', 'd2f8109e5cd58c8d9b3d2d3c56fa1ae36e252488.jpg', 'bd4da0d19e4a42d8bf6beb069e36c6d0e574cef2.jpg', '945b3660227453b29ae42b75a3cc92b7950d1c4f.jpg', '807f454d98bd4a322b76732241b1f056b78bf530.jpg', 'ea18e06c6a87254fcedaf2d3cba59cef9be7b00d.jpg', '11fa844267b9576304b037df64d91a6ccbaac0aa.jpg', '256eedc26be5feda94dc6433951594d112216603.jpg', '7967d5dce48a58788f27821133fa70789bb10e8b.jpg', '6233ff6f9b52cd4eb67f364ac44d8cb36555c0f7.jpg'],
        'mediaURL': 'https://s3-us-west-2.amazonaws.com/avenuehq-listings/fvrebgv/000/262/418/',
        'size': {'low': 763, 'high': 763},
        'squareFootage': 0,
        'acres': 0,
        'title': '#4301 - 1289 Hornby Street',
        'position': {'lat': 49.2774773, 'lng': -123.1295852},
        'agent': 'Andy Hsu PREC*',
        'office': 'RE/MAX Crest Realty',
        'openHouses': 0,
        'openHouseBanners': None,
        'lolType': 'condo'}


class City(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField(null=True)


class State(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True)
    desc = models.TextField(null=True)


class Ownership(models.Model):
    id = models.AutoField(primary_key=True)
    value = models.CharField(max_length=100, unique=True)
    desc = models.TextField(null=True)


class Media(models.Model):
    house = models.ForeignKey('House',on_delete=models.CASCADE,default=None)
    src = models.CharField(max_length=200)
    desc = models.TextField(null=True)


class Type(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100,unique=True)
    desc = models.TextField(null=True)


class House(models.Model):
    id = models.IntegerField(primary_key=True)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)
    ownership = models.ForeignKey(Ownership, on_delete=models.CASCADE)
    public_remarks = models.TextField()
    price = models.IntegerField()
    bedrooms = models.IntegerField()
    baths = models.IntegerField()
    dateListed = models.DateTimeField()
    mediaURL = models.TextField()
    sizel = models.IntegerField()
    sizeh = models.IntegerField()
    square_footage = models.IntegerField()
    acres = models.FloatField()
    title = models.CharField(max_length=200)
    position_lat = models.IntegerField()
    position_lng = models.IntegerField()
    office = models.CharField(max_length=200)
    lol_type = models.ForeignKey(Type, on_delete=models.CASCADE)

