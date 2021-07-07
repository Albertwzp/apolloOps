import pyapollos

a = pyapollos.ApolloClient("parent","default","http://192.168.56.10:30005")
a.start()

for key in ["apollo.portal.envs","apollo.portal.apps"]:
    v = a.get_value(key)
    print("%s : " % key)
    print(v)
