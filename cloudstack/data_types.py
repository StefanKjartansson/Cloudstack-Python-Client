import logging

from dataobject import DataObject, expect_single


__all__ = ['Account', 'VirtualMachine', 'User', 'VMSTATE']


logger = logging.getLogger('cloud.data_types')


class VMSTATE:
    RUNNING = 'Running'
    STOPPED = 'Stopped'


class User(DataObject):

    @expect_single
    def get_domain(self):
        return self.api_client.listDomains(id=self.domainid)

    @expect_single
    def get_account(self):
        return self.api_client.listAccounts(keyword=self.account)


class Account(DataObject):

    @expect_single
    def get_domain(self):
        return self.api_client.listDomains(id=self.domainid)

    def disable(self):
        result = False
        if self.valid_api:
            result = self.api_client.disableAccount(self.id,
                self.domainid).success
        return result

    def enable(self):
        if self.valid_api:
            return self.api_client.enableAccount(self.id,
                self.domainid).success
        return False

    def lock(self):
        if self.valid_api:
            return self.api_client.lockAccount(self.id, self.domainid).success
        return False


class VirtualMachine(DataObject):

    @expect_single
    def get_account(self):
        return self.api_client.listAccounts(keyword=self.account)

    @expect_single
    def get_zone(self):
        return [zone for zone in self.api_client.listZones() if
            zone.id == self.zoneid]

    @expect_single
    def get_router(self):
        if self.valid_api:
            return self.api_client.listRouters(account=self.account)
        return None

    def get_service_offering(self):
        if self.valid_api:
            try:
                sos = self.api_client.listServiceOfferings(
                    virtualMachineId=self.id)
            except:
                sos = None
            if not sos:
                logger.error(
                    '''Service offering missing for VM id: %d,
                    ServiceOffering id: %d''' % (self.id,
                        self.serviceofferingid))
                return None
            return sos[0]
        return None

    @property
    def public_ip(self):
        """
        Returns the public ip address. If a VM belongs to a virtual network,
        it returns the ip of the router.
        """
        so = self.get_service_offering()
        if not so:
            logger.warning('Service offering was not listed.')
            return None
        if so.usevirtualnetwork:
            return self.get_router().publicip
        else:
            return self.ipaddress

    def start(self):
        if self.valid_api and self.state != VMSTATE.RUNNING:
            self.state = self.api_client.startVirtualMachine(self.id).state

    def stop(self, cb=None):
        if self.valid_api and self.state != VMSTATE.STOPPED:
            self.state = self.api_client.stopVirtualMachine(self.id).state

    def reset_password(self):
        if self.valid_api and self.state != VMSTATE.STOPPED:
            self.password = self.api_client.resetPasswordForVirtualMachine(
                self.id).password

    def change_service(self, serviceOffering, force=False):
        id = serviceOffering.id if isinstance(serviceOffering, DataObject) \
            else serviceOffering
        if self.valid_api:
            if self.state != VMSTATE.STOPPED:
                return self.api_client.changeServiceForVirtualMachine(self.id,
                    id).success
            elif force:
                self.stop()
                self.change_service(serviceOffering)
        return False

    def reboot(self):
        if self.valid_api:
            return self.api_client.rebootVirtualMachine(self.id).success
        return False

    def destroy(self):
        if self.valid_api:
            return self.api_client.destroyVirtualMachine(self.id).success
        return False

    def update(self):
        if self.valid_api:
            return self.api_client.updateVirtualMachine(self.id,
                self.displayname, None, self.haenable).success
        return False
