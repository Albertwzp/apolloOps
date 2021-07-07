#coding=utf-8
#import pyapollos
#import subprocess
import requests
import json

from selenium import webdriver

def get_cookie(url, username, password):
    browser = webdriver.Chrome()
    browser.maximize_window()
    browser.delete_all_cookies()
    browser.get(url)
    browser.find_element_by_xpath('//input[@name="username"]').send_keys(username)
    browser.find_element_by_xpath('//input[@name="password"]').send_keys(password, Keys.ENTER)
    cookie = browser.get_cookies()
    return cookie

def request_get(url, headers):
        print("GET: url: %s,\t headers: %s" %(url, headers))
        res = requests.get(url, headers=headers)
        #if res.ok:
        if res.status_code == 200:
            #data = res.json()
            data = json.dumps(res.json(), indent=2, ensure_ascii=False)
            #re.match(r'(appId)'
            data_s = json.loads(data)
            res_j = res.json()
            print("res: %s, data: %s, data_s: %s res_j: %s" % (type(res), type(data), type(data_s), type(res_j)))
            #print(data)
            return data_s
        else:
            print("data: nil")

def request_post(url, headers, body):
        print("POST: url: %s,\t headers: %s,\t body: %s" %(url, headers, body))
        res = requests.post(url, headers=headers, data=body)
        if res.status_code == 200:
            print("POST Success")
        else:
            print("POST FAIL")
        #data = json.dumps(data)
        #print(res.json())
        
    
class ApolloOps(object):
    def __init__(self, config_server='localhost:30005', portal_server='localhost:30001', user='apollo', password='admin', cookie='default'):
        self.config_server = config_server
        self.portal_server = portal_server
        self.user = user
        self.password = password
        self.cookie = cookie
	#get_cookie(portal_server)

    def login(self):
        url = 'http://{}/signin'.format(self.portal_server)
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

    def get_xxx(self, xxx, appId, *, envName='FAT', clusterName='default', namespaceName='option'):
        #headers = {'content-type': 'application/json', "Authorization":"Bearer {}".format(token)}
        headers = {"Cookie": self.cookie}
        if xxx == 'envclusters':
            url = 'http://{}/openapi/v1/apps/{}/envclusters'.format(self.portal_server)
            params={'token': '{}'.format(self.token)}
        elif xxx == 'apps':
            url = 'http://{}/apps'.format(self.portal_server)
            ret = request_get(url, headers)
            #print(type(ret))
            apps = []
            for i in ret:
                apps.append(i["appId"])
            return apps
            print(apps)

        elif xxx == 'clusterName':
            url = 'http://{}/openapi/v1/envs/{}/apps/{}/clusters/{}'.format(self.portal_server, env, appId, clusterName)
        elif xxx == 'nameSpaces':
            #url = 'http://{}/openapi/v1/envs/{}/apps/{}/clusters/{}/namespaces'.format(self.portal_server, envName, appId, clusterName)
            url = 'http://{}/apps/{}/envs/{}/clusters/{}/namespaces'.format(self.portal_server, appId, envName, clusterName)
            ret = request_get(url, headers)
            namespaces = []
            for i in ret:
                namespaces.append(i["baseInfo"]["namespaceName"])
            return namespaces
            print(namespaces)

        elif xxx == 'nameSpaceName':
            #url = 'http://{}/openapi/v1/envs/{}/apps/{}/clusters/{}/namespaces/{}'.format(self.portal_server, envName, appId, clusterName, namespaceName)
            url = 'http://{}/apps/{}/envs/{}/clusters/{}/namespaces/{}'.format(self.portal_server, appId, envName, clusterName, namespaceName)
        else:
            print("get error")

    def post_xxx(self, xxx, *, appId='parent', envName='FAT', clusterName='default', namespaceName='application'):
        headers = {"Cookie": self.cookie, 'Content-Type': "application/json"}
        if xxx == 'clusterName':
            #url = 'http://{}/openapi/v1/envs/{}/apps/{}/clusters'.format(self.portal_server, env, appId)
            url = 'http://{}/apps/{}/envs/{}/clusters'.format(self.portal_server, appId, envName)
            #body = "{'name': {}, 'appId': {}, 'dataChangeCreatedBy': {}}".format(clusterName, appId, self.user)
            body = "{{'appId': '{}', 'name': '{}'}}".format(appId, clusterName)
            print(type(body))
            ret = request_post(url, headers, body)
        elif xxx == 'nameSpace':
            #url = 'http://{}/openapi/v1/apps/{}/appnamespaces'.format(self.portal_server, appId)
            url = 'http://{}/apps/{}/namespaces'.format(self.portal_server, appId)
            #body = "{'name': {}, 'appId': {}, 'format': {}, 'isPublic': {}, 'comment':{}, 'dataChangeCreatedBy': {}}".format(clusterName, appId, format, isPubic, comment, self.user)
            body = "[{{'env': '{}', 'namespace': {{'appId': '{}', 'clusterName': '{}', 'namespaceName': '{}'}}}}]".format(envName, appId, clusterName, namespaceName)
            print(type(body))
            ret = request_post(url, headers, body)
        elif xxx == 'release':
            url = 'http://{}/apps/{}/envs/{}/clusters/{}/namespaces/{}/release'.format(self.portal_server, appId, envName, clusterName, namespaceName)
        else:
            print("post error")

    def put_xxx(self, xxx, *, appId, envName, clusterName, namespaceName):
        if xxx == 'item':
            url = 'http://{}/apps/{}/envs/{}/clusters/{}/namespaces/{}/items'.format(self.portal_server, appId, envName, clusterName, namespaceName)
#http://192.168.56.10:30001/apps/parent/envs/PRO/clusters

    def get_values(self, *, appId, cluster='default', ns='application', client='locahost'):
        url = '{}/configfiles/json/{}/{}/{}?ip={}'.format(self.config_server, appId, cluster, ns, client)
        print(url)
        values = requests.get(url)
        if values.ok:
            data = values.json()
            print(data)
        else:
            print("values: no data")
        #print(res.json())

if __name__ == '__main__':
    #ops = ApolloOps(portal_server="192.168.56.10:30001", cookie="NG_TRANSLATE_LANG_KEY=zh-CN; JSESSIONID=A399F6153F85C82719B50438EAB669DE")
    ops = ApolloOps(portal_server="apollo-offline-wyc.wsecar.cn", cookie="NG_TRANSLATE_LANG_KEY=zh-CN; JSESSIONID=E4D1ED0023DFFF453D830A92F7CA6BB2")
    ops.login()
    #ops.get_values(appId='parent')
    apps = ops.get_xxx('apps', 'parent')
    clusters=['Cluster-03', 'Cluster-04']
    for app in apps:
        for cls in clusters:
            print('Create cls: %s' % cls)
            #ops.post_xxx('clusterName', appId=app, envName='PRO', clusterName=cls)
            #for ns in ops.get_xxx('nameSpaces', app, envName='PRO', clusterName='Cluster-02'):
                #print(ns)
                #ops.post_xxx('nameSpace', appId=app, envName='PRO', clusterName=cls, namespaceName=ns)
        
    #parent_ns = ops.get_xxx('nameSpaces', 'parent', envName='PRO', clusterName='Cluster-06')
    #parent_ns.remove('application')
    #for ns in parent_ns:
    #    print(ns)
    #    ops.post_xxx('nameSpace', appId='call', envName='PRO', clusterName='Cluster-06', namespaceName=ns)
    #ops.get_xxx('nameSpaceName', 'parent', envName='PRO', clusterName='default', namespaceName='application')
    #ops.post_xxx('clusterName', appId='parent', envName='PRO', clusterName='Cluster-06')
    #ops.post_xxx('nameSpace', appId='parent', envName='PRO', clusterName='Cluster-06', namespaceName='nba')
