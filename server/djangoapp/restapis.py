import requests
import json
from .models import CarDealer, DealerReview
from requests.auth import HTTPBasicAuth


# Dealers Description
DEALERSHIP_BASE_URL = "https://gennosukekog-3000.theiadocker-3-labs-prod-theiak8s-4-tor01.proxy.cognitiveclass.ai/dealerships/get"

def get_request(url, **kwargs):
    
    # If argument contain API KEY
    api_key = kwargs.get("ICBSot9ei2EgiQqH4n-MJqZnGqDs88T-mKaYJ6x01Rn4")
    print("GET from {} ".format(url))
    try:
        if api_key:
            params = dict()
            params["text"] = kwargs["text"]
            params["version"] = kwargs["version"]
            params["features"] = kwargs["features"]
            params["return_analyzed_text"] = kwargs["return_analyzed_text"]
            response = requests.get(url, params=params, headers={'Content-Type': 'application/json'},
                                    auth=HTTPBasicAuth('apikey', api_key))
        else:
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

def get_dealers_from_cf(url, **kwargs):
    results = []
    state = kwargs.get("state")
    if state:
        json_result = get_request(url, state=state)
    else:
        json_result = get_request(url)

    print('json_result RESTAPIS', json_result)    

    if json_result:
        # Get the row list in JSON as dealers
        dealers = json_result

        # For each dealer object
        for dealer in dealers:
            # Get its content in `doc` object
            dealer_doc = dealer
            # print(dealer_doc)
            # Create a CarDealer object with values in `doc` object
            dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"],
                                   dealer_id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"], full_name=dealer_doc["full_name"],
                                
                                   st=dealer_doc["st"], zip=dealer_doc["zip"],  short_name=dealer_doc["short_name"])
            results.append(dealer_obj)

    return results

def get_dealer_by_id(url, dealer_id):
    json_result = get_request(url, dealer_id=dealer_id)
    print('json_result from line 54',json_result)

    if json_result:
        dealers = json_result
        
    
        dealer_doc = dealers[0]
        dealer_obj = CarDealer(address=dealer_doc["address"], city=dealer_doc["city"],
                                dealer_id=dealer_doc["id"], lat=dealer_doc["lat"], long=dealer_doc["long"], full_name=dealer_doc["full_name"],
                                
                                st=dealer_doc["st"], zip=dealer_doc["zip"], short_name=dealer_doc["short_name"])
    return dealer_obj
    
def get_dealers_by_state(state):
    # Call get_request with the base URL for dealerships and state parameter
    url = f"{DEALERSHIP_BASE_URL}?state={state}"
    json_result = get_request(url)

    results = []
    if json_result and "docs" in json_result:
        dealers = json_result["docs"]
        for dealer in dealers:
            # Create a CarDealer object with values in `dealer` dictionary
            dealer_obj = CarDealer(
                address=dealer.get("address", ""),
                city=dealer.get("city", ""),
                full_name=dealer.get("full_name", ""),
                dealer_id=dealer.get("id", ""),
                lat=dealer.get("lat", ""),
                long=dealer.get("long", ""),
                short_name=dealer.get("short_name", ""),
                st=dealer.get("st", ""),
                zip=dealer.get("zip", "")
            )
            results.append(dealer_obj)

    return results

def get_dealer_reviews_from_cf(dealer_id):
    # Call get_request with the base URL for reviews and dealerId parameter
    url = REVIEWS_BASE_URL.format(dealer_id=dealer_id)
    # Pass the API key to the get_request function
    api_key = "ICBSot9ei2EgiQqH4n-MJqZnGqDs88T-mKaYJ6x01Rn4"
    json_result = get_request(url, api_key=api_key)

    results = []
    if json_result:
        for review_data in json_result:
            # Check if all required fields exist in review_data
            if "id" in review_data and "dealership" in review_data and "review" in review_data \
                    and "purchase" in review_data and "purchase_date" in review_data \
                    and "car_make" in review_data and "car_model" in review_data and "car_year" in review_data:
                # If all fields are available, create the DealerReview object
                dealer_review = DealerReview(
                    review_id=review_data["id"],
                    dealer_id=review_data["dealership"],
                    review=review_data["review"],
                    purchase=review_data["purchase"],
                    purchase_date=review_data["purchase_date"],
                    car_make=review_data["car_make"],
                    car_model=review_data["car_model"],
                    car_year=review_data["car_year"],
                    sentiment=None
                )
                results.append(dealer_review)

    return results
