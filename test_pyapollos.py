#import pyapollos
#
#a = pyapollos.ApolloClient("parent","default","http://192.168.56.10:30005")
#a.start()
#
#for key in ["apollo.portal.envs","apollo.portal.apps"]:
#    v = a.get_value(key)
#    print("%s : " % key)
#    print(v)

from typing import Optional
from pyapollo.apollo_client import ApolloClient
from unittest import TestCase

class TestClient(TestCase):
    def test_client(self):
        obj = ApolloClient(app_id='passenger', config_server_url='http://192.168.56.10:30005')
        self.assertEqual(obj.get_value('a'), 'gogogogo123456')
        self.assertEqual(obj.get_value('c', '123'), '123')
        self.assertEqual(obj.get_value('c1', '123', 'development.py-client'), '123')
