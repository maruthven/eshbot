import rauth
import pandas as pd
from config import shush
print 'hello world'

def get_search_parameters(term, city):
  #See the Yelp API for more details
  params = {}
  params["term"] = term
  params["location"] = city
  params["radius_filter"] = "4000"
  params["limit"] = "20"
  params["sort"] = "2"
 
  return params

def get_results(params):
 
  #Obtain these from Yelp's manage access page
  consumer_key = shush["key"]
  consumer_secret = shush["secret"]
  token = shush["token"]
  token_secret = shush["token_secret"]
   
  session = rauth.OAuth1Session(
    consumer_key = consumer_key
    ,consumer_secret = consumer_secret
    ,access_token = token
    ,access_token_secret = token_secret)
     
  request = session.get("http://api.yelp.com/v2/search",params=params)
   
  #Transforms the JSON API response into a Python dictionary
  data = request.json()
  session.close()
   
  return data

locations = ['San Fransisco, CA', 'New York, NY']
search = 'ice cream sandwiches'
api_calls = []
print 'hello, searching for ' + search
for loc in locations:
	print loc
	params = get_search_parameters(search, loc)
	out = get_results(params)
	print out
	api_calls = api_calls + out
	#Be a good internet citizen and rate-limit yourself
	time.sleep(1.0)


print api_calls
     
  ##Do other processing