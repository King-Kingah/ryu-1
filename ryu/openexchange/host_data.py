"""
This file define hosts' data structure.
Author:www.muzixing.com
Date                Work
2015/5/29           new this file
2015/7/27           define class host.
"""
from . import data_base
from ryu.lib.ip import ipv4_to_bin
from ryu.lib.ip import ipv4_to_str
from ryu.openexchange.oxproto_v1_0 import OXPP_INACTIVE, OXPP_ACTIVE

'''
plan to delete

class Host(data_base.DataBase):
    def __init__(self, ip=None, MAC=None, mask=None, state=OXPP_INACTIVE):
        self.ip = ip
        self.MAC = MAC
        self.mask = mask
        self.state = state

        IP2HOST[self.ip] = self
        HOSTLIST.append(self)
'''


class Location(object):
    def __init__(self, locations={}):
        # locations: {domain:set([ip1,ip2,...])}
        self.locations = locations
        self.hosts = set()
        self.ip_host = {}

    def update(self, domain, hosts):
        for host in hosts:
            if host.state == OXPP_ACTIVE:
                self.hosts.add(host)
                self.locations[domain].add(ipv4_to_str(host.ip))

                self.ip_host.setdefault(host.ip, None)
                self.ip_host[host.ip] = host
            else:
                if host.ip in self.locations[domain]:
                    self.locations[domain].remove(host.ip)
                    self.hosts.remove(hosts)
                    del self.ip_host[host.ip]
