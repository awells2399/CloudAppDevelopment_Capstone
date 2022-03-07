import sys
from ibmcloudant.cloudant_v1 import CloudantV1, Document
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator
def main(dict):
    authenticator = IAMAuthenticator('Place API key here')
    service = CloudantV1(authenticator=authenticator)
    service.set_service_url("URL here")
    
    try:
        review = Document(
        name=dict["name"],
        dealership=dict["dealership"],
        review=dict["review"],
        purchase=dict["purchase"],
        purchase_date=dict["purchase_date"],
        car_make=dict["car_make"],
        car_model=dict["car_model"],
        car_year=dict["car_year"],)

        response = service.post_document(db='reviews', document=review).get_result()


        result= {
        'headers': {'Content-Type':'application/json'},
        'body': {'data':response}
        }
        return response

    except:

          return {

                'statusCode': 404,

                'message':"SomethingWent Wrong Document was not added"

        }



