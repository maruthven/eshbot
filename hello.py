import rauth

print 'hello world'

def get_search_parameters(city):
  #See the Yelp API for more details
  params = {}
  params["term"] = "restaurant"
  params["location"] = city
  params["radius_filter"] = "2000"
  params["limit"] = "10"
 
  return params

def get_results(params):
 
  #Obtain these from Yelp's manage access page
  consumer_key = "YOUR_KEY"
  consumer_secret = "YOUR_SECRET"
  token = "YOUR_TOKEN"
  token_secret = "YOUR_TOKEN_SECRET"
   
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