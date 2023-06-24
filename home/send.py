import requests
from kavenegar import *

def send(phone):
	return requests.post("https://app.snapp.taxi/api/api-passenger-oauth/v2/otp", data={"cellphone": phone})



