import requests
from json import JSONDecodeError


number = input("Enter a number: ")

try:
    print(int(number) * 2)
except LookupError:
    print('Lookup error? This should never happen.')
except ValueError:
    print('You did not enter a base 10 number! Try again.')

print('Hey!')

r = requests.post('http://text-processing.com/api/sentiment',
                  data={'text': 'Hello API'})

try:
    label = r.json()['label']
    print(label)
except JSONDecodeError:
    print('We could not decode the JSON response!')
except KeyError:
    print('We got JSON back, but it did not have a label.')
