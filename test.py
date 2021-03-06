from ncclient import manager

router = {"host": "ios-xe-mgmt.cisco.com", "port": "10000",
"username": "developer", "password": "Cisco12345"}

with manager.connect(host=router["host"], port=router["port"], username=router["username"], password=router["password"], hostkey_verify=False) as m:
    m.close_session()
