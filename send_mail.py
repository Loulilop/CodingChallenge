from __future__ import print_function
import time
import sib_api_v3_sdk
from sib_api_v3_sdk.rest import ApiException
from pprint import pprint
from mailin import Mailin

# Configure API key authorization: api-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['api-key'] = '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'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['api-key'] = 'Bearer'
# Configure API key authorization: partner-key
configuration = sib_api_v3_sdk.Configuration()
configuration.api_key['partner-key'] = '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'
# Uncomment below to setup prefix (e.g. Bearer) for API key, if needed
# configuration.api_key_prefix['partner-key'] = 'Bearer'

# create an instance of the API class
api_instance = sib_api_v3_sdk.AccountApi(sib_api_v3_sdk.ApiClient(configuration))

def get_account():
    try:
        # Get your account informations, plans and credits details
        api_response = api_instance.get_account()
        pprint(api_response)
    except ApiException as e:
        print("Exception when calling AccountApi->get_account: %s\n" % e)


def send_mail(first_name, email, content):
    print("This is an email for " + first_name + " with email address" + email)

    m = Mailin("https://api.sendinblue.com/v2.0","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")
    data = { "to" : {email:first_name},
		"from" : ["from@email.com", "from email!"],
		"subject" : "Happy Birthday",
		"html" : content
	}
 
    result = m.send_email(data)
    print(result)