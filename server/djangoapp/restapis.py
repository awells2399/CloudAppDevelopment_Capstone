import requests
import json
from .nlu import get_sentiment
from requests.auth import HTTPBasicAuth
from .models import CarDealer, DealerReview


def get_request(url, **kwargs):
    print(kwargs)
    print("GET from {} ".format(url))
    try:
        # Call get method of requests library with URL and parameters
        response = requests.get(url, headers={'Content-Type': 'application/json'},
                    params=kwargs)
    except:
        # If any error occurs
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

# Create a `post_request` to make HTTP POST requests
def post_request(json_payload, **kwargs):
    print(json_payload)
    try:
        url = "https://d19f2121.us-south.apigw.appdomain.cloud/dealer-reviews/reviews"
        response = requests.post(url, params=kwargs, json=json_payload, headers={'Content-Type': 'application/json'})
    except:
        print("Network exception occurred")
    status_code = response.status_code
    print("With status {} ".format(status_code))
    json_data = json.loads(response.text)
    return json_data

def get_dealers_from_cf(url, **kwargs):
    results = []
    json_result = get_request(url)

    if json_result:
        dealers = json_result["body"]["rows"]

        for dealer in dealers:
            dealer_doc = dealer["doc"]
            dealer_obj = CarDealer(address=dealer_doc["address"], 
            city=dealer_doc["city"], 
            full_name=dealer_doc["full_name"],
            id=dealer_doc["id"], 
            lat=dealer_doc["lat"], 
            long=dealer_doc["long"],
            short_name=dealer_doc["short_name"],
            st=dealer_doc["st"], 
            zip=dealer_doc["zip"])

            results.append(dealer_obj)

    return results

def get_dealers_by_state(url, **kwargs):
    results = []
    json_result = get_request(url,kwargs)
    if json_result:
        dealers = json_result["body"]["rows"]
        for dealer in dealers:
            dealer_doc = dealer["doc"]
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"], full_name=dealer_doc["full_name"],
                                   id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"],
                                   short_name=dealer_doc["short_name"],
                                   st=dealer_doc["st"], zip=dealer_doc["zip"])
            results.append(dealer_obj)

    return results



# Create a get_dealer_reviews_from_cf method to get reviews by dealer id from a cloud function
def get_dealer_reviews(dealer_id):
    results = []
    # Call get_request with a URL parameter
    url= 'https://d19f2121.us-south.apigw.appdomain.cloud/dealer-reviews/reviews?id=' + str(dealer_id)
    json_result = get_request(url)
    if json_result:
        reviews = json_result['docs']
        for review in reviews:
            # print(review)
            review_obj = DealerReview(
                dealership=review["dealership"],
                name=review["name"],
                purchase=review["purchase"],
                review=review["review"],
                purchase_date=review["purchase_date"],
                car_make=review["car_make"],
                car_model=review["car_model"],
                car_year=review["car_year"],
                id=review["_id"] )
            review_obj.sentiment = analyze_review_sentiments(review_obj.review)
            results.append(review_obj)
    return results

def get_dealer(dealerId):
    url = "https://d19f2121.us-south.apigw.appdomain.cloud/dealer-reviews/dealership"

    json_result = get_request(url, id=dealerId)
    if json_result:
        dealer = json_result["body"]["docs"][0]['full_name']    

    return dealer


# Create an `analyze_review_sentiments` method to call Watson NLU and analyze text
def analyze_review_sentiments(text):
    return get_sentiment(text)
# - Call get_request() with specified arguments
# - Get the returned sentiment label such as Positive or Negative



