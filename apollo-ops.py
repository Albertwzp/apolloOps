#!
import pyapollos
import subprocess
import requests
import json

class ApolloOps(object):
    def __init__(self, config_server_url='http://localhost:30005', user='apollo', password='admin'):
        self.config_server_url = config_server_url
        self.user = user
        self.password = password

    def login(self):
        url = '{}/signin'.format(self.config_server_url)
        #headers = {'content-type': 'application/json'}
        headers = {'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
                   'Accept-Encoding': 'gzip, deflate',
                   'Accept-Language': 'zh,zh-TW;q=0.9,en-US;q=0.8,en;q=0.7',
                   'Cache-Control': 'max-age=0',
                   'Connection': 'keep-alive',
                   'content-type': 'application/x-www-form-urlencoded',
                   'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'}
        payload = {'username': 'apollo', 'password': 'admin', 'login-submit': '登录'}
        print(url)
        #loginx = requests.post(url, data=json.dumps(payload), headers=headers)
        loginx = requests.post(url, data=payload, headers=headers)
        if loginx.status_code == 302:
            print('login success')
        else:
            print('login error')

    def get_clusters(self, appId, token):
        url = '{}/openapi/v1/apps/{}/envclusters'.format(self.config_server_url, appId,)
        print(url)
        #headers = {'content-type': 'application/json', "Authorization":"Bearer {}".format(token)}
        clusters = requests.get(url, params={'token': '{}'.format(token)})
        #if clusters.status_code == 200:
        if clusters.ok:
            data = clusters.json()
            print(data)
        else:
            print("clusters: no data")

#    def get_xxx(self, xxx, *, appId, clusterName='default', namespaceName='option'):
#        if xxx == 'envclusters':
#            url = 'http://{portal_address}/openapi/v1/apps/{}/envclusters'.format(self.config_server_url, appId)
#        elif xxx = 'apps':
#            url = 'http://{}/openapi/v1/apps'.format(self.config_server_url)
#        elif xxx = 'clusterName':
#            url = 'http://{}/openapi/v1/envs/{}/apps/{}/clusters/{}'.format(self.config_server_url, env, appId, clusterName)
#        elif xxx = 'nameSpaces':
#            url = 'http://{}/openapi/v1/envs/{}/apps/{}/clusters/{}/namespaces'.format(self.config_server_url, env, appId, clusterName)
#        elif xxx = 'nameSpaceName':
#            url = 'http://{}/openapi/v1/envs/{}/apps/{}/clusters/{}/namespaces/{}'.format(self.config_server_url, env, appId, clusterName, namespaceName)
#        elif xxx = '':
#        else
#
#    def post_xxx(self, xxx, *, appId, clusterName):
#        if xxx == 'clusterName':
#            url = 'http://{}/openapi/v1/envs/{}/apps/{}/clusters'.format(self.config_server_url, env, appId)
#            data = "{'name': {}, 'appId': {}, 'dataChangeCreatedBy': {}}".format(clusterName, appId, self.user)
#        elif xxx = 'nameSpace':
#            url = 'http://{}/openapi/v1/apps/{}/appnamespaces'.format(self.config_server_url, appId)
#            data = "{'name': {}, 'appId': {}, 'format': {}, 'isPublic': {}, 'comment':{}, 'dataChangeCreatedBy': {}}".format(clusterName, appId, format, isPubic, comment, self.user)
#        elif xxx = ''
#        else
#http://192.168.56.10:30001/apps/parent/envs/PRO/clusters

    def get_values(self, appId, cluster='default', ns='application', client='locahost'):
        url = '{}/configfiles/json/{}/{}/{}?ip={}'.format(self.config_server_url, appId, cluster, ns, client)
        print(url)
        values = requests.get(url)
        if values.ok:
            data = values.json()
            print(data)
        else:
            print("values: no data")

def main():
    #URL {config_server_url}/configfiles/json/{appId}/{clusterName}/{namespaceName}?ip={clientIp}
    #URL: {config_server_url}/configs/{appId}/{clusterName}/{namespaceName}?releaseKey={releaseKey}&ip={clientIp}
    #subprocess.run(['curl', '-X', 'GET', 'http://192.168.56.10:30005/configfiles/json/parent/default/application?ip=127.0.0.1'])
    #subprocess.Popen('curl -X GET http://192.168.56.10:30005/configs/parent/default/application?releaseKey=&ip=127.0.0.1', shell=True)
    config_server = "192.168.56.10:30005"
    ns=requests.get('http://192.168.56.10:30005/configfiles/json/parent/default/application?ip=127.0.0.1').json()
    while 1:
        a = pyapollos.ApolloClient(app_id="parent", cluster="default", config_server_url="192.168.56.10:30005")
        a.start()
        c = a.get_value('port', namespace="application")
        print(c)
        time.sleep(2)
 #token: 842386b0c21c94818f652b78d34e46601ee51ada

if __name__ == '__main__':
    ops = ApolloOps(config_server_url="http://192.168.56.10:30005")
    ops.login()
    ops.get_clusters(appId='parent', token='ce7088315ed143e0bb41514035ec50a9')
    ops.get_values(appId='parent')
    #main()
