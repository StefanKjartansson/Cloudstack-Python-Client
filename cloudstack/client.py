from baseclient import *
from data_types import *


class Client(BaseClient):
    """Cloud.com API client"""

    def addHost(self, username, password, zoneId, url, podId=None,
        clusterId=None, clusterName=None, _class=DataObject):
        return self.process('addhostsresponse',
            self.__execute__('addHost',
            {
                'username': username, 'password': password, 'zoneId': zoneId,
                'url': url, 'podId': podId, 'clusterId': clusterId,
               'clusterName': clusterName}),
            _class)

    def addSecondaryStorage(self, zoneId, url, _class=DataObject):
        return self.process('addsecondarystorageresponse',
            self.__execute__('addSecondaryStorage',
            {'zoneId': zoneId, 'url': url}),
            _class)

    def assignPortForwardingService(self, publicIp, virtualMachineId,
        id=None, ids=None, _class=DataObject):
        return self.process_async('assignPortForwardingService',
            {
                'publicIp': publicIp, 'virtualMachineId': virtualMachineId,
                'id': id, 'ids': ids},
            _class)

    def assignToLoadBalancerRule(self, id, virtualMachineId=None,
        virtualMachineIds=None, _class=DataObject):
        return self.process_async('assignToLoadBalancerRule',
            {
                'id': id, 'virtualMachineId': virtualMachineId,
                'virtualMachineIds': virtualMachineIds},
            _class)

    def associateIpAddress(self, zoneId, _class=DataObject):
        return self.process('associateipaddressresponse',
            self.__execute__('associateIpAddress',
            {'zoneId': zoneId}),
            _class)

    def attachIso(self, id, virtualMachineId, _class=DataObject):
        return self.process_async('attachIso',
            {'id': id, 'virtualMachineId': virtualMachineId},
            _class)

    def attachVolume(self, id, virtualMachineId, deviceId=None,
        _class=DataObject):
        return self.process_async('attachVolume',
            {
                'id': id, 'virtualMachineId': virtualMachineId,
                'deviceId': deviceId},
            _class)

    def cancelHostMaintenance(self, id, _class=DataObject):
        return self.process_async('cancelHostMaintenance',
            {'id': id},
            _class)

    def changeServiceForVirtualMachine(self, id, serviceOfferingId,
        _class=DataObject):
        return self.process_async('changeServiceForVirtualMachine',
            {'id': id, 'serviceOfferingId': serviceOfferingId},
            _class)

    def copyIso(self, id, sourceZoneId, destZoneId, _class=DataObject):
        return self.process_async('copyIso',
            {'id': id, 'sourceZoneId': sourceZoneId,
            'destZoneId': destZoneId},
            _class)

    def copyTemplate(self, id, sourceZoneId, destZoneId, _class=DataObject):
        return self.process_async('copyTemplate',
            {'id': id, 'sourceZoneId': sourceZoneId, 'destZoneId': destZoneId},
            _class)

    def createDiskOffering(self, name, displayText, diskSize,
        _class=DataObject):
        return self.process('creatediskofferingresponse',
            self.__execute__('createDiskOffering',
            {'name': name, 'displayText': displayText, 'diskSize': diskSize}),
            _class)

    def createDomain(self, name, parentDomainId=None, _class=DataObject):
        return self.process('createdomainresponse',
            self.__execute__('createDomain',
            {'name': name, 'parentDomainId': parentDomainId}),
            _class)

    def createLoadBalancerRule(self, name, publicIp, publicPort, privatePort,
        algorithm, description=None, _class=DataObject):
        return self.process('createloadbalancerruleresponse',
            self.__execute__('createLoadBalancerRule',
            {'name': name, 'publicIp': publicIp, 'publicPort': publicPort,
            'privatePort': privatePort, 'algorithm': algorithm,
            'description': description}),
            _class)

    def createPod(self, name, zoneId, cidr, startIp, gateway,
        endIp=None, _class=DataObject):
        return self.process('createpodresponse',
            self.__execute__('createPod',
            {'name': name, 'zoneId': zoneId, 'cidr': cidr, 'startIp': startIp,
            'gateway': gateway, 'endIp': endIp}),
            _class)

    def createPortForwardingRule(self, ipAddress, publicPort, privatePort,
        protocol, virtualMachineId, _class=DataObject):
        return self.process('createportforwardingruleresponse',
            self.__execute__('createPortForwardingRule',
            {'ipAddress': ipAddress, 'publicPort': publicPort,
            'privatePort': privatePort, 'protocol': protocol,
            'virtualMachineId': virtualMachineId}),
            _class)

    def createPortForwardingService(self, name, description=None,
        _class=DataObject):
        return self.process('createportforwardingserviceresponse',
            self.__execute__('createPortForwardingService',
            {'name': name, 'description': description}),
            _class)

    def createPortForwardingServiceRule(self, publicPort, privatePort,
        portForwardingServiceId, protocol=None, _class=DataObject):
        return self.process_async('createPortForwardingServiceRule',
            {'publicPort': publicPort, 'privatePort': privatePort,
            'portForwardingServiceId': portForwardingServiceId,
            'protocol': protocol},
            _class)

    def createServiceOffering(self, name, displayText, cpuNumber, cpuSpeed,
        memory, storageType=None, offerHa=None, useVirtualNetwork=None,
        tags=None, _class=DataObject):
        return self.process('createserviceofferingresponse',
            self.__execute__('createServiceOffering',
            {'name': name, 'displayText': displayText, 'cpuNumber': cpuNumber,
            'cpuSpeed': cpuSpeed, 'memory': memory,
            'storageType': storageType, 'offerHa': offerHa,
            'useVirtualNetwork': useVirtualNetwork, 'tags': tags}),
            _class)

    def createSnapshot(self, volumeId, _class=DataObject):
        return self.process_async('createSnapshot',
            {'volumeId': volumeId},
            _class)

    def createSnapshotPolicy(self, volumeId, schedule, intervalType, maxSnaps,
        timezone, _class=DataObject):
        return self.process('createsnapshotpolicysresponse',
            self.__execute__('createSnapshotPolicy',
            {'volumeId': volumeId, 'schedule': schedule,
            'intervalType': intervalType, 'maxSnaps': maxSnaps,
            'timezone': timezone}),
            _class)

    def createStoragePool(self, name, zoneId, url, podId=None, clusterId=None,
        tags=None, details=None, _class=DataObject):
        return self.process('createstoragepoolresponse',
            self.__execute__('createStoragePool',
            {'name': name, 'zoneId': zoneId, 'url': url, 'podId': podId,
            'clusterId': clusterId, 'tags': tags, 'details': details}),
            _class)

    def createTemplate(self, name, displayText, osTypeId, volumeId=None,
        passwordEnabled=None, isPublic=None, isFeatured=None, snapshotId=None,
        _class=DataObject):
        return self.process_async('createTemplate',
            {'name': name, 'displayText': displayText, 'osTypeId': osTypeId,
            'volumeId': volumeId, 'passwordEnabled': passwordEnabled,
            'isPublic': isPublic, 'isFeatured': isFeatured,
            'snapshotId': snapshotId},
            _class)

    def createUser(self, username, password, email, firstName, lastName,
        accountType, domainId=None, account=None, timezone=None,
        _class=User):
        return self.process_list('createuserresponse>user',
            self.__execute__('createUser',
            {'username': username, 'password': password, 'email': email,
            'firstName': firstName, 'lastName': lastName,
            'accountType': accountType, 'domainId': domainId,
            'account': account, 'timezone': timezone}),
            _class)[0]

    def createVlanIpRange(self, gateway, netmask, zoneId, startIp, endIp=None,
        vlan=None, _class=DataObject):
        return self.process('createvlaniprangeresponse',
            self.__execute__('createVlanIpRange',
            {'gateway': gateway, 'netmask': netmask, 'zoneId': zoneId,
            'startIp': startIp, 'endIp': endIp, 'vlan': vlan}),
            _class)

    def createVolume(self, name, zoneId=None, diskOfferingId=None,
        snapshotId=None, _class=DataObject):
        return self.process_async('createVolume',
            {'name': name, 'zoneId': zoneId, 'diskOfferingId': diskOfferingId,
            'snapshotId': snapshotId},
            _class)

    def createZone(self, name, dns1, internaldns1, guestCidrAddress, dns2=None,
        internaldns2=None, vnet=None, _class=DataObject):
        return self.process('createzoneresponse',
            self.__execute__('createZone',
            {'name': name, 'dns1': dns1, 'internaldns1': internaldns1,
            'guestCidrAddress': guestCidrAddress, 'dns2': dns2,
            'internaldns2': internaldns2, 'vnet': vnet}),
            _class)

    def deleteDiskOffering(self, id, _class=DataObject):
        return self.process('deletediskofferingresponse',
            self.__execute__('deleteDiskOffering',
            {'id': id}),
            _class)

    def deleteDomain(self, id, _class=DataObject):
        return self.process_async('deleteDomain',
            {'id': id},
            _class)

    def deleteHost(self, id, _class=DataObject):
        return self.process('deletehostresponse',
            self.__execute__('deleteHost',
            {'id': id}),
            _class)

    def deleteIso(self, id, zoneId=None, _class=DataObject):
        return self.process('deleteisoresponse',
            self.__execute__('deleteIso',
            {'id': id, 'zoneId': zoneId}),
            _class)

    def deleteLoadBalancerRule(self, id, _class=DataObject):
        return self.process('deleteloadbalancerruleresponse',
            self.__execute__('deleteLoadBalancerRule',
            {'id': id}),
            _class)

    def deletePod(self, id, _class=DataObject):
        return self.process('deletepodresponse',
            self.__execute__('deletePod',
            {'id': id}),
            _class)

    def deletePortForwardingRule(self, id, _class=DataObject):
        return self.process('deleteportforwardingruleresponse',
            self.__execute__('deletePortForwardingRule',
            {'id': id}),
            _class)

    def deletePortForwardingService(self, id, _class=DataObject):
        return self.process_async('deletePortForwardingService',
            {'id': id},
            _class)

    def deletePortForwardingServiceRule(self, id, _class=DataObject):
        return self.process_async('deletePortForwardingServiceRule',
            {'id': id},
            _class)

    def deleteServiceOffering(self, id, _class=DataObject):
        return self.process('deleteserviceofferingresponse',
            self.__execute__('deleteServiceOffering',
            {'id': id}),
            _class)

    def deleteSnapshot(self, id, _class=DataObject):
        return self.process_async('deleteSnapshot',
            {'id': id},
            _class)

    def deleteSnapshotPolicies(self, volumeId, intervalType=None,
        _class=DataObject):
        return self.process('deletesnapshotpoliciesresponse',
            self.__execute__('deleteSnapshotPolicies',
            {'volumeId': volumeId, 'intervalType': intervalType}),
            _class)

    def deleteStoragePool(self, name, _class=DataObject):
        return self.process('deletestoragepoolresponse',
            self.__execute__('deleteStoragePool',
            {'name': name}),
            _class)

    def deleteTemplate(self, id, _class=DataObject):
        return self.process_async('deleteTemplate',
            {'id': id},
            _class)

    def deleteUser(self, id, _class=DataObject):
        return self.process('deleteuserresponse',
            self.__execute__('deleteUser',
            {'id': id}),
            _class)

    def deleteVlanIpRange(self, id, _class=DataObject):
        return self.process('deletevlaniprangeresponse',
            self.__execute__('deleteVlanIpRange',
            {'id': id}),
            _class)

    def deleteVolume(self, id, _class=DataObject):
        return self.process('deletevolumeresponse',
            self.__execute__('deleteVolume',
            {'id': id}),
            _class)

    def deleteZone(self, id, _class=DataObject):
        return self.process('deletezoneresponse',
            self.__execute__('deleteZone',
            {'id': id}),
            _class)

    def deployVirtualMachine(self, zoneId, serviceOfferingId, templateId,
        diskOfferingId=None, displayName=None, group=None, userData=None,
        _class=VirtualMachine):
        return self.process_async('deployVirtualMachine',
            {'zoneId': zoneId, 'serviceOfferingId': serviceOfferingId,
            'templateId': templateId, 'diskOfferingId': diskOfferingId,
            'displayName': displayName, 'group': group,
            'userData': userData},
            _class)

    def destroyVirtualMachine(self, id, _class=DataObject):
        return self.process_async('destroyVirtualMachine',
            {'id': id},
            _class)

    def detachIso(self, virtualMachineId, _class=DataObject):
        return self.process_async('detachIso',
            {'virtualMachineId': virtualMachineId},
            _class)

    def detachVolume(self, id, _class=DataObject):
        return self.process_async('detachVolume',
            {'id': id},
            _class)

    def disableAccount(self, account, domainId, _class=DataObject):
        return self.process_async('disableAccount',
            {'account': account, 'domainId': domainId},
            _class)

    def disableUser(self, id, _class=DataObject):
        return self.process_async('disableUser',
            {'id': id},
            _class)

    def disassociateIpAddress(self, ipaddress, _class=DataObject):
        return self.process('disassociateipaddressresponse',
            self.__execute__('disassociateIpAddress',
            {'ipaddress': ipaddress}),
            _class)

    def enableAccount(self, account, domainId, _class=DataObject):
        return self.process('enableaccountresponse',
            self.__execute__('enableAccount',
            {'account': account, 'domainId': domainId}),
            _class)

    def enableUser(self, id, _class=DataObject):
        return self.process('enableuserresponse',
            self.__execute__('enableUser',
            {'id': id}),
            _class)

    def getCloudIdentifier(self, userId, _class=DataObject):
        return self.process('getcloudidentifierresponse',
            self.__execute__('getCloudIdentifier',
            {'userId': userId}),
            _class)

    def listAccounts(self, keyword=None, _class=Account):
        return self.process_list('listaccountsresponse>account',
            self.__execute__('listAccounts',
            {'keyword': keyword}),
            _class)

    def listAlerts(self, type=None, keyword=None, _class=DataObject):
        return self.process_list('listalertsresponse>alert',
            self.__execute__('listAlerts',
            {'type': type, 'keyword': keyword}),
            _class)

    def listAsyncJobs(self, startDate=None, _class=DataObject):
        return self.process_list('listasyncjobsresponse>asyncjobs',
            self.__execute__('listAsyncJobs',
            {'startDate': startDate}),
            _class)

    def listCapacity(self, zoneId=None, podId=None, hostId=None, type=None,
        _class=DataObject):
        return self.process_list('listcapacityresponse>capacity',
            self.__execute__('listCapacity',
            {'zoneId': zoneId, 'podId': podId, 'hostId': hostId,
            'type': type}),
            _class)

    def listClusters(self, id=None, name=None, podId=None, zoneId=None,
        _class=DataObject):
        return self.process_list('listclusterresponse>cluster',
            self.__execute__('listClusters',
            {'id': id, 'name': name, 'podId': podId, 'zoneId': zoneId}),
            _class)

    def listConfigurations(self, name=None, category=None, keyword=None,
        _class=DataObject):
        return self.process_list('listconfigurationsresponse>configuration',
            self.__execute__('listConfigurations',
            {'name': name, 'category': category, 'keyword': keyword}),
            _class)

    def listDiskOfferings(self, id=None, name=None, keyword=None,
        _class=DataObject):
        return self.process_list('listdiskofferingsresponse>diskoffering',
            self.__execute__('listDiskOfferings',
            {'id': id, 'name': name, 'keyword': keyword}),
            _class)

    def listDomainChildren(self, id, name=None, keyword=None, isRecursive=None,
        _class=DataObject):
        return self.process_list('listdomainchildrenresponse>domain',
            self.__execute__('listDomainChildren',
            {'id': id, 'name': name, 'keyword': keyword,
            'isRecursive': isRecursive}),
            _class)

    def listDomains(self, id=None, name=None, domainLevel=None, keyword=None,
        _class=DataObject):
        return self.process_list('listdomainsresponse>domain',
            self.__execute__('listDomains',
            {'id': id, 'name': name, 'domainLevel': domainLevel,
            'keyword': keyword}),
            _class)

    def listEvents(self, type=None, level=None, startDate=None, endDate=None,
        keyword=None, entryTime=None, duration=None, _class=DataObject):
        return self.process_list('listeventsresponse>event',
            self.__execute__('listEvents',
            {
                'type': type, 'level': level, 'startDate': startDate,
                'endDate': endDate, 'keyword': keyword,
                'entryTime': entryTime, 'duration': duration}),
            _class)

    def listHosts(self, id=None, name=None, zoneId=None, podId=None, type=None,
        state=None, _class=DataObject):
        return self.process_list('listhostsresponse>host',
            self.__execute__('listHosts',
            {
                'id': id, 'name': name, 'zoneId': zoneId, 'podId': podId,
                'type': type, 'state': state}),
            _class)

    def listIsos(self, id=None, name=None, isoFilter=None, bootable=None,
        keyword=None, _class=DataObject):
        return self.process_list('listisosresponse>iso',
            self.__execute__('listIsos',
            {
                'id': id, 'name': name, 'isoFilter': isoFilter,
                'bootable': bootable, 'keyword': keyword}),
            _class)

    def listLoadBalancerRuleInstances(self, id=None, applied=None,
        _class=DataObject):
        return self.process_list(
            'listloadbalancerruleinstancesresponse>loadbalancerruleinstance',
            self.__execute__('listLoadBalancerRuleInstances',
            {'id': id, 'applied': applied}),
            _class)

    def listLoadBalancerRules(self, id=None, name=None, keyword=None,
        virtualMachineId=None, publicIp=None, _class=DataObject):
        return self.process_list(
            'listloadbalancerrulesresponse>loadbalancerrule',
            self.__execute__('listLoadBalancerRules',
            {'id': id, 'name': name, 'keyword': keyword,
            'virtualMachineId': virtualMachineId, 'publicIp': publicIp}),
            _class)

    def listOsCategories(self, _class=DataObject):
        return self.process_list('listoscategoriesresponse>oscategory',
            self.__execute__('listOsCategories',
            {}),
            _class)

    def listOsTypes(self, _class=DataObject):
        return self.process_list('listostypesresponse>ostype',
            self.__execute__('listOsTypes',
            {}),
            _class)

    def listPods(self, id=None, name=None, keyword=None, zoneId=None,
        _class=DataObject):
        return self.process_list('listpodsresponse>pod',
            self.__execute__('listPods',
            {'id': id, 'name': name, 'keyword': keyword, 'zoneId': zoneId}),
            _class)

    def listPortForwardingRules(self, ipAddress=None, _class=DataObject):
        return self.process_list(
            'listportforwardingrulesresponse>portforwardingrule',
            self.__execute__('listPortForwardingRules',
            {'ipAddress': ipAddress}),
            _class)

    def listPortForwardingServiceRules(self, id=None,
        portForwardingServiceId=None, _class=DataObject):
        return self.process_list(
            'listportforwardingservicerulesresponse>portforwardingservicerule',
            self.__execute__('listPortForwardingServiceRules',
            {'id': id, 'portForwardingServiceId': portForwardingServiceId}),
            _class)

    def listPortForwardingServices(self, id=None, name=None, keyword=None,
        _class=DataObject):
        return self.process_list(
            'listportforwardingservicesresponse>portforwardingservice',
            self.__execute__('listPortForwardingServices',
            {'id': id, 'name': name, 'keyword': keyword}),
            _class)

    def listPortForwardingServicesByVm(self, virtualMachineId, ipAddress=None,
        keyword=None, _class=DataObject):
        return self.process_list(
            'listportforwardingservicesbyvmresponse>portforwardingservice',
            self.__execute__('listPortForwardingServicesByVm',
            {'virtualMachineId': virtualMachineId, 'ipAddress': ipAddress,
            'keyword': keyword}),
            _class)

    def listPublicIpAddresses(self, keyword=None, zoneId=None, ipAddress=None,
        forVirtualNetwork=None, _class=DataObject):
        return self.process_list(
            'listpublicipaddressesresponse>publicipaddress',
            self.__execute__('listPublicIpAddresses',
            {
                'keyword': keyword, 'zoneId': zoneId, 'ipAddress': ipAddress,
                'forVirtualNetwork': forVirtualNetwork}),
            _class)

    def listResourceLimits(self, resourceType=None, _class=DataObject):
        return self.process_list('listresourcelimitsresponse>resourcelimit',
            self.__execute__('listResourceLimits',
            {'resourceType': resourceType}),
            _class)

    def listRouters(self, zoneId=None, podId=None, hostId=None, state=None,
        name=None, account=None, domainId=None, keyword=None,
        _class=DataObject):
        return self.process_list('listroutersresponse>router',
            self.__execute__('listRouters',
            {
                'zoneId': zoneId, 'podId': podId, 'hostId': hostId,
                'state': state, 'name': name, 'account': account,
                'domainId': domainId, 'keyword': keyword}),
            _class)

    def listServiceOfferings(self, id=None, name=None, virtualMachineId=None,
        keyword=None, _class=DataObject):
        return self.process_list(
            'listserviceofferingsresponse>serviceoffering',
            self.__execute__('listServiceOfferings',
            {'id': id, 'name': name, 'virtualMachineId': virtualMachineId,
            'keyword': keyword}),
            _class)

    def listSnapshotPolicies(self, volumeId=None, _class=DataObject):
        return self.process_list('listsnapshotpoliciesresponse>snapshotpolicy',
            self.__execute__('listSnapshotPolicies',
            {'volumeId': volumeId}),
            _class)

    def listSnapshots(self, volumeId=None, intervalType=None,
        snapshotType=None, keyword=None, _class=DataObject):
        return self.process_list('listsnapshotresponse>snapshot',
            self.__execute__('listSnapshots',
            {
                'volumeId': volumeId, 'intervalType': intervalType,
                'snapshotType': snapshotType, 'keyword': keyword}),
            _class)

    def listStoragePools(self, name=None, zoneId=None, ipAddress=None,
        path=None, keyword=None, podId=None, _class=DataObject):
        return self.process_list('liststoragepoolresponse>storagepool',
            self.__execute__('listStoragePools',
            {'name': name, 'zoneId': zoneId, 'ipAddress': ipAddress,
            'path': path, 'keyword': keyword, 'podId': podId}),
            _class)

    def listSystemVms(self, id=None, zoneId=None, podId=None, hostId=None,
        state=None, name=None, account=None, domainId=None, keyword=None,
        systemVmType=None, _class=DataObject):
        return self.process_list('listsystemvmsresponse>systemvm',
            self.__execute__('listSystemVms',
            {
                'id': id, 'zoneId': zoneId, 'podId': podId, 'hostId': hostId,
                'state': state, 'name': name, 'account': account,
                'domainId': domainId, 'keyword': keyword,
                'systemVmType': systemVmType}),
            _class)

    def listTemplatePermissions(self, id, _class=DataObject):
        return self.process_list(
            'listtemplatepermissionsresponse>templatepermission',
            self.__execute__('listTemplatePermissions',
            {'id': id}),
            _class)

    def listCommunityTemplates(self, id=None, name=None, keyword=None,
        _class=DataObject):
        return self.listTemplates('community', id, name, keyword, _class)

    def listFeaturedTemplates(self, id=None, name=None, keyword=None,
        _class=DataObject):
        return self.listTemplates('featured', id, name, keyword, _class)

    def listTemplates(self, templateFilter, id=None, name=None, keyword=None,
        _class=DataObject):
        return self.process_list('listtemplatesresponse>template',
            self.__execute__('listTemplates',
            {'templateFilter': templateFilter, 'id': id,
            'name': name, 'keyword': keyword}),
            _class)

    def listUsageRecords(self, startDate, endDate, account=None, domainId=None,
        _class=DataObject):
        return self.process_list('listusagerecordsresponse>usagerecord',
            self.__execute__('listUsageRecords',
            {
                'startDate': startDate, 'endDate': endDate, 'account': account,
                'domainId': domainId}),
            _class)

    def listUsers(self, id=None, username=None, account=None, domainId=None,
        accountType=None, state=None, keyword=None, _class=User):
        return self.process_list('listusersresponse>user',
            self.__execute__('listUsers',
            {'id': id, 'username': username, 'account': account,
            'domainId': domainId, 'accountType': accountType,
            'state': state, 'keyword': keyword}),
            _class)

    def listVirtualMachines(self, name=None, state=None, zoneId=None,
        keyword=None, _class=VirtualMachine):
        return self.process_list('listvirtualmachinesresponse>virtualmachine',
            self.__execute__('listVirtualMachines',
            {'name': name, 'state': state, 'zoneId': zoneId,
            'keyword': keyword}),
            _class)

    def getVirtualMachineById(self, id):
        return [i for i in self.listVirtualMachines()
            if i.id == id][0]

    def listVlanIpRanges(self, id=None, name=None, zoneId=None, keyword=None,
        vlan=None, podId=None, account=None, domainId=None, _class=DataObject):
        return self.process_list('listvlaniprangesresponse>vlaniprange',
            self.__execute__('listVlanIpRanges',
            {'id': id, 'name': name, 'zoneId': zoneId, 'keyword': keyword,
            'vlan': vlan, 'podId': podId, 'account': account,
            'domainId': domainId}),
            _class)

    def listVolumes(self, id=None, name=None, zoneId=None,
        virtualMachineId=None, keyword=None, _class=DataObject):
        return self.process_list('listvolumesresponse>volume',
            self.__execute__('listVolumes',
            {'id': id, 'name': name, 'zoneId': zoneId,
            'virtualMachineId': virtualMachineId, 'keyword': keyword}),
            _class)

    def listZones(self, available=True, _class=DataObject):
        return self.process_list('listzonesresponse>zone',
            self.__execute__('listZones',
            {'available': available}),
            _class)

    def lockAccount(self, account, domainId, _class=DataObject):
        return self.process('lockaccountresponse',
            self.__execute__('lockAccount',
            {'account': account, 'domainId': domainId}),
            _class)

    def lockUser(self, id=None, _class=DataObject):
        return self.process('lockuserresponse',
            self.__execute__('lockUser',
            {'id': id}),
            _class)

    def login(self, username, password, domainId=None, _class=DataObject):
        return self.process('loginresponse',
            self.__execute__('login',
            {'username': username, 'password': password,
            'domainId': domainId}),
            _class)

    def logout(self, _class=DataObject):
        return self.process('logoutresponse',
            self.__execute__('logout',
            {}),
            _class)

    def prepareHostForMaintenance(self, id, _class=DataObject):
        return self.process_async('prepareHostForMaintenance',
            {'id': id},
            _class)

    def queryAsyncJobResult(self, jobId, _class=DataObject):
        return self.process('queryasyncjobresultresponse',
            self.__execute__('queryAsyncJobResult',
            {'jobId': jobId}),
            _class)

    def rebootRouter(self, id, _class=DataObject):
        return self.process_async('rebootRouter',
            {'id': id},
            _class)

    def rebootSystemVm(self, id, _class=DataObject):
        return self.process_async('rebootSystemVm',
            {'id': id},
            _class)

    def rebootVirtualMachine(self, id, _class=DataObject):
        return self.process_async('rebootVirtualMachine',
            {'id': id},
            _class)

    def reconnectHost(self, id, _class=DataObject):
        return self.process_async('reconnectHost',
            {'id': id},
            _class)

    def recoverVirtualMachine(self, id, _class=DataObject):
        return self.process('recovervirtualmachineresponse',
            self.__execute__('recoverVirtualMachine',
            {'id': id}),
            _class)

    def registerIso(self, name, displayText, url, osTypeId, zoneId,
        isPublic=None, isFeatured=None, bootable=None, _class=DataObject):
        return self.process('registerisoresponse',
            self.__execute__('registerIso',
            {'name': name, 'displayText': displayText, 'url': url,
            'osTypeId': osTypeId, 'zoneId': zoneId, 'isPublic': isPublic,
            'isFeatured': isFeatured, 'bootable': bootable}),
            _class)

    def registerTemplate(self, name, displayText, url, format, osTypeId,
        zoneId, passwordEnabled=None, isPublic=None, isFeatured=None,
        _class=DataObject):
        return self.process('registertemplateresponse',
            self.__execute__('registerTemplate',
            {'name': name, 'displayText': displayText, 'url': url,
            'format': format, 'osTypeId': osTypeId, 'zoneId': zoneId,
            'passwordEnabled': passwordEnabled, 'isPublic': isPublic,
            'isFeatured': isFeatured}),
            _class)

    def registerUserKeys(self, id, _class=DataObject):
        return self.process('registeruserkeysresponse',
            self.__execute__('registerUserKeys',
            {'id': id}),
            _class)

    def removeFromLoadBalancerRule(self, id, virtualMachineId=None,
        virtualMachineIds=None, _class=DataObject):
        return self.process_async('removeFromLoadBalancerRule',
            {'id': id, 'virtualMachineId': virtualMachineId,
            'virtualMachineIds': virtualMachineIds},
            _class)

    def removePortForwardingService(self, id, publicIp, virtualMachineId,
        _class=DataObject):
        return self.process_async('removePortForwardingService',
            {'id': id, 'publicIp': publicIp,
            'virtualMachineId': virtualMachineId},
            _class)

    def resetPasswordForVirtualMachine(self, id, _class=DataObject):
        return self.process_async('resetPasswordForVirtualMachine',
            {'id': id},
            _class)

    def startRouter(self, id, _class=DataObject):
        return self.process_async('startRouter',
            {'id': id},
            _class)

    def startSystemVm(self, id, _class=DataObject):
        return self.process_async('startSystemVm',
            {'id': id},
            _class)

    def startVirtualMachine(self, id, _class=DataObject):
        return self.process_async('startVirtualMachine',
            {'id': id},
            _class)

    def stopRouter(self, id, _class=DataObject):
        return self.process_async('stopRouter',
            {'id': id},
            _class)

    def stopSystemVm(self, id, _class=DataObject):
        return self.process_async('stopSystemVm',
            {'id': id},
            _class)

    def stopVirtualMachine(self, id, _class=DataObject):
        return self.process_async('stopVirtualMachine',
            {'id': id},
            _class)

    def updateAccount(self, newName, account, domainId, _class=DataObject):
        return self.process('updateaccountresponse',
            self.__execute__('updateAccount',
            {'newName': newName, 'account': account, 'domainId': domainId}),
            _class)

    def updateConfiguration(self, name, value, _class=DataObject):
        return self.process('updateconfigurationresponse',
            self.__execute__('updateConfiguration',
            {'name': name, 'value': value}),
            _class)

    def updateDiskOffering(self, id, name=None, displayText=None,
        _class=DataObject):
        return self.process('updatediskofferingresponse',
            self.__execute__('updateDiskOffering',
            {'id': id, 'name': name, 'displayText': displayText}),
            _class)

    def updateDomain(self, id, name=None, _class=DataObject):
        return self.process('updatedomainresponse',
            self.__execute__('updateDomain',
            {'id': id, 'name': name}),
            _class)

    def updateHost(self, id, osCategoryId=None, _class=DataObject):
        return self.process('updatehostresponse',
            self.__execute__('updateHost',
            {'id': id, 'osCategoryId': osCategoryId}),
            _class)

    def updateIso(self, id, name=None, displayText=None, osTypeId=None,
        bootable=None, _class=DataObject):
        return self.process('updateisoresponse',
            self.__execute__('updateIso',
            {'id': id, 'name': name, 'displayText': displayText,
            'osTypeId': osTypeId, 'bootable': bootable}),
            _class)

    def updatePod(self, id, name=None, cidr=None, startIp=None, endIp=None,
        gateway=None, _class=DataObject):
        return self.process('updatepodresponse',
            self.__execute__('updatePod',
            {'id': id, 'name': name, 'cidr': cidr, 'startIp': startIp,
            'endIp': endIp, 'gateway': gateway}),
            _class)

    def updatePortForwardingRule(self, ipAddress, publicPort, privatePort,
        protocol, virtualMachineId, _class=DataObject):
        return self.process('updateportforwardingruleresponse',
            self.__execute__('updatePortForwardingRule',
            {'ipAddress': ipAddress, 'publicPort': publicPort,
            'privatePort': privatePort, 'protocol': protocol,
            'virtualMachineId': virtualMachineId}),
            _class)

    def updateResourceLimit(self, resourceType, account=None, domainId=None,
        max=None, _class=DataObject):
        return self.process('updateresourcelimitresponse',
            self.__execute__('updateResourceLimit',
            {'resourceType': resourceType, 'account': account,
            'domainId': domainId, 'max': max}),
            _class)

    def updateServiceOffering(self, id, name=None, displayText=None,
        offerHa=None, _class=DataObject):
        return self.process('updateserviceofferingresponse',
            self.__execute__('updateServiceOffering',
            {'id': id, 'name': name, 'displayText': displayText,
            'offerHa': offerHa}),
            _class)

    def updateStoragePool(self, id=None, tags=None, _class=DataObject):
        return self.process('updatestoragepoolresponse',
            self.__execute__('updateStoragePool',
            {'id': id, 'tags': tags}),
            _class)

    def updateTemplate(self, name, displayText, format=None, osTypeId=None,
        passwordEnabled=None, _class=DataObject):
        return self.process('updatetemplateresponse',
            self.__execute__('updateTemplate',
            {'name': name, 'displayText': displayText, 'format': format,
            'osTypeId': osTypeId, 'passwordEnabled': passwordEnabled}),
            _class)

    def updateTemplatePermissions(self, id, isPublic=None, isFeatured=None,
        accounts=None, op=None, _class=DataObject):
        return self.process('updatetemplatepermissionsresponse',
            self.__execute__('updateTemplatePermissions',
            {'id': id, 'isPublic': isPublic, 'isFeatured': isFeatured,
            'accounts': accounts, 'op': op}),
            _class)

    def updateUser(self, id, username=None, password=None, email=None,
        firstName=None, lastName=None, timezone=None, apiKey=None,
        secretKey=None, _class=DataObject):
        return self.process('updateuserresponse',
            self.__execute__('updateUser',
            {'id': id, 'username': username, 'password': password,
            'email': email, 'firstName': firstName, 'lastName': lastName,
            'timezone': timezone, 'apiKey': apiKey, 'secretKey': secretKey}),
            _class)

    def updateVirtualMachine(self, id, displayName=None, group=None,
        haenable=None, _class=DataObject):
        return self.process('updatevirtualmachineresponse',
            self.__execute__('updateVirtualMachine',
            {'id': id, 'displayName': displayName, 'group': group,
            'haenable': haenable}),
            _class)

    def updateZone(self, id, name=None, dns1=None, dns2=None,
        internaldns1=None, internaldns2=None, guestCidrAddress=None, vnet=None,
        _class=DataObject):
        return self.process('updatezoneresponse',
            self.__execute__('updateZone',
            {'id': id, 'name': name, 'dns1': dns1, 'dns2': dns2,
            'internaldns1': internaldns1, 'internaldns2': internaldns2,
            'guestCidrAddress': guestCidrAddress, 'vnet': vnet}),
            _class)
