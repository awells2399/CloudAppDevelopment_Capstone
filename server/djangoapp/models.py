from django.db import models
from django.utils.timezone import now


# Create your models here.

class CarMake(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=200)
    
    def __str__(self):
       return self.name


class CarModel(models.Model):
  SEDAN = 'sedan'
  SUV = 'Suv'
  WAGON = 'Wagon'
  SPORT = 'Sport'
  VAN = 'Van'
  CROSSOVER = 'Crossover' 
  CAR_TYPE_CHOICES = [
        (SEDAN, 'Sedan'),
        (SUV, 'Suv'),
        (WAGON, 'Wagon'),
        (SPORT, 'Sport'),
        (VAN, 'Van'),
        (CROSSOVER, 'Crossover')
    ]

  dealer_id = models.IntegerField()
  manufacturer = models.ForeignKey(CarMake, on_delete=models.CASCADE)
  name = models.CharField(max_length=30)
  year = models.DateField()
  car_type = models.CharField(max_length=30, choices=CAR_TYPE_CHOICES)

  def __st__(self):
    return (
      'Dealer: ' + self.dealer_id +'\n' +
      'Name: ' + self.name +'\n' +
      'Year: ' + self.Year +'\n' +
      'Type: ' + self.car_type +'\n' 
      )



# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
  
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        # Dealer address
        self.address = address
        # Dealer city
        self.city = city
        # Dealer Full Name
        self.full_name = full_name
        # Dealer id
        self.id = id
        # Location lat
        self.lat = lat
        # Location long
        self.long = long
        # Dealer short name
        self.short_name = short_name
        # Dealer state
        self.st = st
        # Dealer zip
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
  
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, id):
        # Dealer address
        self.dealership = dealership
        # Dealer city
        self.name = name
        # Dealer Full Name
        self.purchase = purchase
        # Dealer id
        self.review = review
        # Location lat
        self.purchase_date = purchase_date
        # Location long
        self.car_make = car_make
        # Dealer short name
        self.car_model = car_model
        # Dealer state
        self.car_year = car_year
        # Dealer zip
        self.sentiment = ''
        self.id = id

    def __str__(self):
        return (
        'Dealer name: ' + self.dealership +'\n'  +
        'Reviewer name: ' + self.name +'\n' +
        'Comment: ' + self.review +'\n' +
        'Make and Model: ' + self.make + ' ' + self.car_model + '\n' + 
        'Dealer name: ' + self.dealership +'\n'
        )
        
        

