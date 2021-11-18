#coding=utf-8
#import pyapollos
#import subprocess
import requests
import json
import time

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
        #print("[GET]---url: %s,\t headers: %s" %(url, headers))
        res = requests.get(url, headers=headers)
        #if res.ok:
        if res.status_code == 200:
            #data = res.json()
            data = json.dumps(res.json(), indent=2, ensure_ascii=False)
            #re.match(r'(appId)'
            data_s = json.loads(data)
            res_j = res.json()
            #print("res: %s, data: %s, data_s: %s res_j: %s" % (type(res), type(data), type(data_s), type(res_j)))
            #print(data_s)
            return data_s
        else:
            print("data: nil")

def request_post(url, headers, body):
        #print("[POST]---url: %s,\t headers: %s,\t body: %s" %(url, headers, body))
        en_body = body.encode('utf-8')
        res = requests.post(url, headers=headers, data=en_body)
        if res.status_code == 200:
            print("POST Success")
        else:
            print("POST FAIL")
        #data = json.dumps(data)
        #print(res.json())

def request_put(url, headers, body):
        print("[PUT]---url: %s,\t headers: %s,\t body: %s" %(url, headers, body))
        en_body = body.encode('utf-8')
        res = requests.post(url, headers=headers, data=en_body)
        if res.status_code == 200:
            print("PUT Success")
        else:
            print("PUT FAIL")        

def env_c(env, cls):
    return env.lower() + cls[-1]

class ApolloOps(object):
    def __init__(self, config_server='localhost:30005', portal_server='localhost:30001', user='apollo', password='admin', cookie='',rep=True):
        self.config_server = config_server
        self.portal_server = portal_server
        self.user = user
        self.password = password
        self.cookie = cookie
        self.rep = rep
        self.headers = {"Cookie": cookie, 'Content-Type': "application/json;charset=UTF-8"}
	#get_cookie(portal_server)

    def login(self):
        url = '{}/signin'.format(self.portal_server)
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
        loginx = requests.post(url, data=json.dumps(payload), headers=headers)
        #loginx = requests.Session()
	    #loginx.headers.update(headers)
	    #loginx.post(url, data=payload)
        if loginx.status_code == 302:
            print('login success')
        else:
            print('login error')

    def get_xxx(self, xxx, *, appId='parent', envName='FAT', clusterName='default', namespaceName='option'):
        #headers = {'content-type': 'application/json', "Authorization":"Bearer {}".format(token)}
        headers = {"Cookie": self.cookie, 'Content-Type': "application/json;charset=UTF-8"}
        if xxx == 'apps':
            url = '{}/apps'.format(self.portal_server)
            ret = request_get(url, headers)
            #print(type(ret))
            #apps = []
            #for i in ret:
            #    apps.append(i["appId"])
            #return apps
            #print(apps)
            return ret
        elif xxx == 'nameSpaces':
            #url = '{}/openapi/v1/envs/{}/apps/{}/clusters/{}/namespaces'.format(self.portal_server, envName, appId, clusterName)
            url = '{}/apps/{}/envs/{}/clusters/{}/namespaces'.format(self.portal_server, appId, envName, clusterName)
            ret = request_get(url, headers)
            namespaces = []
            for i in (ret or []):
                namespaces.append(i["baseInfo"]["namespaceName"])
            return namespaces
        elif xxx == 'properties':
            url = '{}/apps/{}/envs/{}/clusters/{}/namespaces/{}/releases/active?page=0&size=1'.format(self.portal_server, appId, envName, clusterName, namespaceName)
            ret = request_get(url, headers)
            if ret:
                aws = eval(ret[0]['configurations'])
            else:
                aws = {}
            return  aws
            

        elif xxx == 'envclusters':
            url = '{}/openapi/v1/apps/{}/envclusters'.format(self.portal_server)
            params={'token': '{}'.format(self.token)}
        elif xxx == 'clusterName':
            url = '{}/openapi/v1/envs/{}/apps/{}/clusters/{}'.format(self.portal_server, env, appId, clusterName)
            print(namespaces)
        elif xxx == 'nameSpaceName':
            #url = '{}/openapi/v1/envs/{}/apps/{}/clusters/{}/namespaces/{}'.format(self.portal_server, envName, appId, clusterName, namespaceName)
            url = '{}/apps/{}/envs/{}/clusters/{}/namespaces/{}'.format(self.portal_server, appId, envName, clusterName, namespaceName)

        else:
            print("get error")

    def post_xxx(self, xxx, *, appId='parent', envName='FAT', clusterName='default', namespaceName='application', app={}):
        headers = {"Cookie": self.cookie, 'Content-Type': "application/json;charset=UTF-8"}
        if xxx == 'app':
            url = '{}/apps'.format(self.portal_server)
            body = "{{'appId': '{}', 'name': '{}', 'orgId': '{}', 'orgName': '{}', 'ownerName': '{}', 'admins': []}}".format(app["appId"], app["name"], app["orgId"], app["orgName"], app["ownerName"])
            #en_body = body.encode('utf-8')
            print(body)
            ret = request_post(url, headers, body)
        elif xxx == 'clusterName':
            #url = '{}/openapi/v1/envs/{}/apps/{}/clusters'.format(self.portal_server, env, appId)
            url = '{}/apps/{}/envs/{}/clusters'.format(self.portal_server, appId, envName)
            #body = "{'name': {}, 'appId': {}, 'dataChangeCreatedBy': {}}".format(clusterName, appId, self.user)
            body = "{{'appId': '{}', 'name': '{}'}}".format(appId, clusterName)
            print(type(body))
            ret = request_post(url, headers, body)
        elif xxx == 'nameSpace':
            #url = '{}/openapi/v1/apps/{}/appnamespaces'.format(self.portal_server, appId)
            url = '{}/apps/{}/namespaces'.format(self.portal_server, appId)
            #body = "{'name': {}, 'appId': {}, 'format': {}, 'isPublic': {}, 'comment':{}, 'dataChangeCreatedBy': {}}".format(clusterName, appId, format, isPubic, comment, self.user)
            body = "[{{'env': '{}', 'namespace': {{'appId': '{}', 'clusterName': '{}', 'namespaceName': '{}'}}}}]".format(envName, appId, clusterName, namespaceName)
            print(type(body))
            ret = request_post(url, headers, body)
        else:
            print("post error")

    def post_item(self, *, appId='parent', envName='FAT', clusterName='default', namespaceName='application', k="", v=""):
        url = '{}/apps/{}/envs/{}/clusters/{}/namespaces/{}/item'.format(self.portal_server, appId, envName, clusterName, namespaceName)
        body = "{{'tableViewOperType': 'create', 'key': '{}', 'value': '{}', 'addItemBtnDisabled': true}}".format(k, v)
        print(body)
        ret = request_post(url, self.headers, body)

    def post_release(self, *, appId='parent', envName='FAT', clusterName='default', namespaceName='application'):
        url = '{}/apps/{}/envs/{}/clusters/{}/namespaces/{}/releases'.format(self.portal_server, appId, envName, clusterName, namespaceName)
        body = "{'releaseTitle': '', 'releaseComment': '', 'isEmergencyPublish': false}"
        ret = request_post(url, self.headers, body)

    def put_xxx(self, xxx, *, appId, envName, clusterName, namespaceName):
        headers = {"Cookie": self.cookie, 'Content-Type': "application/json;charset=UTF-8"}
        if xxx == 'item':
            url = '{}/apps/{}/envs/{}/clusters/{}/namespaces/{}/items'.format(self.portal_server, appId, envName, clusterName, namespaceName)
            body = '{"configText": "fd = 13\nbs = 15\nwx = 8\nys = 3","namespaceId": 4278,"format": "properties"}'
            ret = request_put(url, headers, body)
            return ret

    def sync_app(self, *, remote=None):
        apps = remote.get_xxx('apps')
        for app in apps:
            print(app)
            self.post_xxx('app', app=app)

    def sync_cls(self, *, remote=None, srcEnv='', dstEnv='', srcCls='', dstCls=[] ):
        apps = remote.get_xxx('apps')
        for app in apps[:1]:
            for cls in dstCls:
                print('Create cls: %s' % cls)
                self.post_xxx('clusterName', appId=app["appId"], envName=dstEnv, clusterName=cls)
        
    def sync_ns(self, *, remote=None, srcEnv='', dstEnv='', srcCls='', dstCls=[] ):
        apps = remote.get_xxx('apps')
        for app in apps:
            nss = remote.get_xxx('nameSpaces', appId=app["appId"], envName=srcEnv, clusterName=srcCls)
            for cls in dstCls:
                print('Create cls: %s' % cls)
                self.post_xxx('clusterName', appId=app, envName=dstEnv, clusterName=cls)
                for ns in nss:
                    print('Create ns: %s' % ns)
                    self.post_xxx('nameSpace', appId=app["appId"], envName=dstEnv, clusterName=cls, namespaceName=ns)
                    #time.sleep(10)

    def sync_property(self, *, remote=None, srcEnv='', dstEnv='', srcCls='', dstCls=[] ):
        apps = remote.get_xxx('apps')
        sub = {}
        for app in apps:
            nss = remote.get_xxx('nameSpaces', appId=app["appId"], envName=srcEnv, clusterName=srcCls)
            for cls in dstCls:
                #senv_path = env_c(srcEnv, srcCls)
                #denv_path = env_c(dstEnv, cls)
                print('Create cls: %s' % cls)
                #self.post_xxx('clusterName', appId=app["appId"], envName=dstEnv, clusterName=cls)
                for ns in nss:
                    print('Create ns: %s' % ns)
                    #self.post_xxx('nameSpace', appId=app["appId"], envName=dstEnv, clusterName=cls, namespaceName=ns)
                    print(app, cls)
                    properties = self.get_xxx('properties', appId=app["appId"], envName=srcEnv, clusterName=srcCls, namespaceName=ns)
                    print(properties)
                    # for k,v in properties.items():
                    #     v = str(v)
                    #     if senv_path in v:
                    #         v = v.replace(senv_path, denv_path)
                    #     self.post_item(appId=app["appId"], envName=dstEnv, clusterName=cls, namespaceName=ns, k=k, v=v)
                    # self.post_release(appId=app["appId"], envName=dstEnv, clusterName=cls, namespaceName=ns)
                    #time.sleep(10)

    def get_all_propertys(self, *, env='', cls=''):
        apps = self.get_xxx('apps')
        for app in apps:
            nss = self.get_xxx('nameSpaces', appId=app["appId"], envName=env, clusterName=cls)
            for ns in nss:
                properties = self.get_xxx('properties', appId=app["appId"], envName=env, clusterName=cls, namespaceName=ns)
                print(properties)