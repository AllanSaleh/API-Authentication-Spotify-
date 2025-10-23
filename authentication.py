# ============== Basic API Key authentication:

# - Keys that we attach to requests, as a form of auth
# -- Often time you'll need to make anm account with the api service to be granted a key (openweatherapi)
# -- You can simply grab the key from the documentation (reqres api)

# - With these keys you can add them into your API headers and gain access to all resources

#  ============== Token Authentication
# -- Typically a post request with some kind of account credentials
# -- They validate your credentials
# -- Mint/Sign a token to you (this token is your access pass)
# -- Send the token back to client
# -- The client must then store the token to be reused
# -- Apply the token upon each request, by adding it to the Headers