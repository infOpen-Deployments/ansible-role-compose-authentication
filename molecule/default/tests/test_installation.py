"""
Role tests
"""

import os
from testinfra.utils.ansible_runner import AnsibleRunner

testinfra_hosts = AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('all')


def test_listening_port(host):
    """
    Ensure host listening on 80 and 9000 ports
    """

    assert host.socket('tcp://0.0.0.0:80').is_listening
    assert host.socket('tcp://0.0.0.0:9000').is_listening
