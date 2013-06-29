import anyjson
import base64
import httplib2
import logging
import sys
import urllib
import urlparse

logger = logging.getLogger('pypin')


class API(object):

    ENDPOINT = 'https://test-api.pin.net.au/1/'

    def __init__(self, api_key, debug=False, **kwargs):
        self.api_key = api_key
        self.headers = {'Authorization': 'Basic ' + base64.encodestring(api_key + ':')}
        self.client = httplib2.Http(**kwargs)
        self.debug = debug

    def _transform_content(self, content):
        return anyjson.deserialize(content)

    def _make_request(self, path, body=None, data={}, method='GET', headers={}, **kwargs):
        headers.update(self.headers)

        url = urlparse.urljoin(self.ENDPOINT, path)

        if body is None and data:
            body = urllib.urlencode(data)

        response, content = self.client.request(url, method=method, body=body, headers=headers, **kwargs)

        if self.debug:
            for h, v in response.items():
                logger.debug("{header}: {value}".format(header=h, value=v))

        return self._transform_content(content)

    def list_charges(self):
        return self._make_request('charges', method='GET')

    def create_charge(self, amount, description, email, ip_address, card_number,
            card_expiry_month, card_expiry_year, card_cvc, card_name,
            card_address_line1, card_address_city, card_address_postcode,
            card_address_state, card_address_country):

        data = {
            'amount': amount,
            'description': description,
            'email': email,
            'ip_address': ip_address,
            'card[number]': card_number,
            'card[expiry_month]': card_expiry_month,
            'card[expiry_year]': card_expiry_year,
            'card[cvc]': card_cvc,
            'card[name]': card_name,
            'card[address_line1]': card_address_line1,
            'card[address_city]': card_address_city,
            'card[address_postcode]': card_address_postcode,
            'card[address_state]': card_address_state,
            'card[address_country]': card_address_country,
        }

        return self._make_request('charges', data=data, method='POST')
