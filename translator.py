'''Using Watson API - Language translator'''
from ibm_watson import LanguageTranslatorV3
from ibm_cloud_sdk_core.authenticators import IAMAuthenticator

URL_LT="https://api.eu-gb.language-translator.watson.cloud.ibm.com/instances/d36e442f-c147-4a28-9c38-f3f431e88c42"
APIKEY_LT = "diCRgNXN1K13BwDnvVcIyik9KIZilzl0mg_Mhls_J0fO"
VERSION = '2018-05-01'

AUTHENTICATOR = IAMAuthenticator(APIKEY_LT)
LANGUAGE_TRANSLATOR = LanguageTranslatorV3(version=VERSION, authenticator=AUTHENTICATOR)

LANGUAGE_TRANSLATOR.set_service_url(URL_LT)
def englishtofrench(input_text):
    '''This function translates the user_input(english) into french'''

    FRENCH_TRANSLATION = LANGUAGE_TRANSLATOR.translate(
        text= input_text , model_id='en-fr').get_result()

    return FRENCH_TRANSLATION['translations'][0]['translation']

def englishtogerman(input_text):
    '''this function translates the user_input(english) into german'''

    GERMAN_TRANSLATION = LANGUAGE_TRANSLATOR.translate(
        text= input_text , model_id='en-de').get_result()

    return GERMAN_TRANSLATION['translations'][0]['translation']
#input_text = input("Enter the english text to be translated to french and german : ")
#print(englishtofrench(input_text))
#print(englishtogerman(input_text))
