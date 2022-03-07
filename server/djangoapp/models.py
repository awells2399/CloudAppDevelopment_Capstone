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
      'Manufacturer: ' + self.manufacturer +'\n' +
      'Name: ' + self.name +'\n' +
      'Year: ' + self.Year +'\n' +
      'Type: ' + self.car_type +'\n' 
      )



# <HINT> Create a plain Python class `CarDealer` to hold dealer data
class CarDealer:
  
    def __init__(self, address, city, full_name, id, lat, long, short_name, st, zip):
        self.address = address
        self.city = city
        self.full_name = full_name
        self.id = id
        self.lat = lat
        self.long = long
        self.short_name = short_name
        self.st = st
        self.zip = zip

    def __str__(self):
        return "Dealer name: " + self.full_name


# <HINT> Create a plain Python class `DealerReview` to hold review data
class DealerReview:
  
    def __init__(self, dealership, name, purchase, review, purchase_date, car_make, car_model, car_year, id):
        
        self.dealership = dealership
        self.name = name 
        self.purchase = purchase       
        self.review = review
        self.purchase_date = purchase_date
        self.car_make = car_make
        self.car_model = car_model
        self.car_year = car_year        
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
        
        

