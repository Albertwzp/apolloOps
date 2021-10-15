if __name__ == '__main__':
    #current = ApolloOps(portal_server="http://192.168.56.10:30001", cookie="NG_TRANSLATE_LANG_KEY=zh-CN; JSESSIONID=6FD8FF5D9B39CC57A916CF02C173845B")
    #remote = ApolloOps(portal_server="https://apollo-offline-wyc.xxx.cn", cookie="NG_TRANSLATE_LANG_KEY=zh-CN; JSESSIONID=590305E409F8B97DCB500CC0E17F5956")
    current = ApolloOps(portal_server="https://apollo-offline-bmpl.xxx.cn", cookie="NG_TRANSLATE_LANG_KEY=zh-CN; JSESSIONID=41804E009F5F58EE49B8FEC5DF7E581E")
    remote = ApolloOps(portal_server="https://apollo-offline-bmpl.xxx.cn", cookie="NG_TRANSLATE_LANG_KEY=zh-CN; JSESSIONID=41803E009F5F58EE49B8FEC5DF7E581E")
    #current.sync_app(remote=remote)
    #current.sync_cls(remote=remote, srcEnv='FAT', dstEnv='PRO', srcCls='Cluster-02', dstCls=['Cluster-01', 'Cluster-02'])
    #current.sync_ns(remote=remote, srcEnv='FAT', dstEnv='PRO', srcCls='Cluster-02', dstCls=['Cluster-01', 'Cluster-02'])
    #current.sync_cls(remote=remote, srcEnv='UAT', dstEnv='UAT', srcCls='Cluster-00', dstCls=['Cluster-01'])
    current.sync_ns(remote=remote, srcEnv='UAT', dstEnv='UAT', srcCls='Cluster-00', dstCls=['Cluster-01'])
    #ops.login()

        
    #parent_ns = ops.get_xxx('nameSpaces', 'parent', envName='PRO', clusterName='Cluster-06')
    #parent_ns.remove('application')
    #for ns in parent_ns:
    #    print(ns)
    #    ops.post_xxx('nameSpace', appId='call', envName='PRO', clusterName='Cluster-06', namespaceName=ns)
    #ops.get_xxx('nameSpaceName', 'parent', envName='PRO', clusterName='default', namespaceName='application')
    #ops.post_xxx('clusterName', appId='parent', envName='PRO', clusterName='Cluster-06')
    #ops.post_xxx('nameSpace', appId='parent', envName='PRO', clusterName='Cluster-06', namespaceName='nba')
