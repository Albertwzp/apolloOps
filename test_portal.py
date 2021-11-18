#! /bin/env python3
import sys
sys.path.append("./")
from apolloPortal import ApolloOps
if __name__ == '__main__':
    current = ApolloOps(portal_server="https://apollo-offline-xxxx.xx.cn", cookie="NG_TRANSLATE_LANG_KEY=zh-CN; JSESSIONID=95CD621B9CDFB1141D2E17F9BADBFB75")
#    ops = ApolloOps(portal_server="https://apollo-offline-xxxx.xx.cn", cookie="NG_TRANSLATE_LANG_KEY=zh-CN; JSESSIONID=C0D0B6F126BF3EEE2D0C99D3CDC5E055")
#    remote = ApolloOps(portal_server="https://apollo-offline-xxxx.xxx.cn", cookie="NG_TRANSLATE_LANG_KEY=zh-CN; JSESSIONID=41803E009F5F58EE49B8FEC5DF7E581E")
    #current.sync_app(remote=remote)
    #current.sync_cls(remote=remote, srcEnv='UAT', dstEnv='UAT', srcCls='Cluster-00', dstCls=['Cluster-01'])
    current.sync_property(remote=current, srcEnv='FAT', dstEnv='FAT', srcCls='Cluster-04', dstCls=['Cluster-05'])
#    current.get_all_propertys(env='FAT', cls='Cluster-05')
    #ops.login()

        
    #parent_ns = ops.get_xxx('nameSpaces', 'parent', envName='PRO', clusterName='Cluster-06')
    #parent_ns.remove('application')
    #for ns in parent_ns:
    #    print(ns)
    #    ops.post_xxx('nameSpace', appId='call', envName='PRO', clusterName='Cluster-06', namespaceName=ns)
    #abc = ops.get_xxx('nameSpaceName', appId='parent', envName='DEV', clusterName='Cluster-02')
#    a = ops.get_xxx('properties', appId='userCenterCtrlImpl', envName='FAT', clusterName='Cluster-04', namespaceName='application')
    #ops.put_xxx('item', appId='userCenterCtrlImpl', envName='FAT', clusterName='Cluster-05', namespaceName='application')
#    ops.post_item(appId='userCenterCtrlImpl', envName='FAT', clusterName='Cluster-05', namespaceName='application', dic=eval(a))
    #b = ops.get_xxx('nameSpaces', appId='parent', envName='DEV', clusterName='Cluster-02', namespaceName='businessMpl.mongo')
#    print(a)
    #ops.post_xxx('clusterName', appId='parent', envName='PRO', clusterName='Cluster-06')
    #ops.post_xxx('nameSpace', appId='parent', envName='PRO', clusterName='Cluster-06', namespaceName='nba')
