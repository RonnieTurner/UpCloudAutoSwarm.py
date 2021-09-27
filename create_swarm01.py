import requests, base64, pprint, json, textwrap

def headers():
    auth = base64.b64encode("<apiuser>:<apipasswd>".encode())
    headers = {"Authorization": "Basic " + auth.decode(),
               "Content-Type": "application/json"}
    return headers


url = "https://api.upcloud.com/1.2/"
ssh = "ssh-rsa AAAAB3NzaC1yc2EAAAADAQABAAABAQC8Ag+afN9Ppcz1Wxxy91UBHt5BOh6lqRokSJZXlvduNcTvKCz1JmGKoFt3rgPLdZON2aTrQjVAwOIwajVw8FbR2uwt5rYnWlyB3qUj1Y6b62t7y3m5Cv0cwMHBcUHkGiXVi0LrqQTBgfuBtvBB62hkortyvgNrbKTnK+Y84eUVrZHmArjZPDPyD4rA/gZ3FK3KntLEKsovemmPLjI2TISc9BKGmT/pthMvlvjOXUqF9f9rrvwHrU7FqO6HKEr1agAK87US6wCzKVK+eFS9hITCWP53+FoFBQO2zZMtLYEBFEx6Dc36lmXImUjdREsMqXjEcjv6ud4sKBrsdoqJ/yQF ronnieturner@Ronnies-MacBook-Pro-2.local"
#user_data = "#!/bin/bash\nyum updrade -y\nyum install -y vim epel-release\nyum update -y\nyum install -y git python python-devel python-pip openssl ansible\nsed -i '22s/#//' /etc/ansible/ansible.cfg\nsed -i '14s/#//' /etc/ansible/ansible.cfg"
#user_data = "https://github.com/CloudAF/init_ans_master.sh"
zone = input("where will you deploy master_node: ")
def payload(zone, title, hostname, vda_title):
    payload = {
      "server": {
        "zone": f"{zone}",
        "title": f"{title}",
        "hostname": f"{hostname}",
        "plan": "4xCPU-8GB",
        #"avoid_host": "7653311107",
        "storage_devices": {
          "storage_device": [
            {
              "action": "clone",
              "storage": "01000000-0000-4000-8000-000020040100",
              "size": 50,
              "title": f"{vda_title}",
              "tier": "maxiops"
            },
          ]
        },
        "login_user": {
          "username": "root",
          "ssh_keys": {
            "ssh_key": [
              f"{ssh}",
            ]
           }
        },
        #"user_data": f"{user_data}"
      }
    }
    return payload


def get_templates(headers, url):
    r = requests.get(f"{url}storage/template/", headers=headers())
    server_list = r.json()
    pprint.pprint(server_list)

def get_server_info(headers, url, uuid):
    r = requests.get(f"{url}server/{uuid}", headers=headers())
    server_info = r.json()
    pprint.pprint(server_info)

'''def create_server_master(payload, headers, url):
    title = f"swarm01_master_node_{zone}"
    hostname = f"swarm01.master.{zone}"
    vda_title = f"swarm01-master-{zone}"
    #user_data = "https://raw.githubusercontent.com/hackspls/CloudAF/master/init_ans_master.sh"
    user_data = "#!/bin/bash\nyum updrade\nyum install -y vim epel-release\nyum update\nyum install -y git python python-devel python-pip openssl ansible\nsed -i '22s/#//' /etc/ansible/ansible.cfg\nsed -i '14s/#//' /etc/ansible/ansible.cfg"
    #user_data = myfile
    r = requests.post(f"{url}server/", data=json.dumps(payload(
        zone, title, hostname, vda_title, user_data)), headers=headers())
    pprint.pprint(r.json())
    server_data = r.json()
    #pprint.pprint(server_data)
    uuid = server_data['server']['uuid']
    print(uuid)
    with open('uuid.json', 'w') as list:
        list = json.dump([uuid], list)

    return server_data
'''

'''def create_swarm_ams1(payload, headers, url, zone):
    if zone != "nl-ams1":
        zone = "nl-ams1"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum upgrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        uuid = server_data['server']['uuid']
        print(uuid)
    else:
        pass

def create_swarm_lon1(payload, headers, url, zone):
    if zone != "uk-lon1":
        zone = "uk-lon1"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum upgrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        return server_data
    else:
        pass

def create_swarm_fra1(payload, headers, url, zone):
    if zone != "de-fra1":
        zone = "de-fra1"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum updrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        return server_data
    else:
        pass

def create_swarm_sin1(payload, headers, url, zone):
    if zone != "sg-sin1":
        zone = "sg-sin1"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum updrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        uuid = server_data["server"]["uuid"]
        return server_data
    else:
        pass



def create_swarm_sjo1(payload, headers, url, zone):
    if zone != "us-sjo1":
        zone = "us-sjo1"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum updrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        return server_data
    else:
        pass

def create_swarm_chi1(payload, headers, url, zone):
    if zone != "us-chi1":
        zone = "us-chi1"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum updrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        return server_data
    else:
        pass

def create_swarm_hel1(payload, headers, url, zone):
    if zone != "fi-hel1":
        zone = "fi-hel1"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum updrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        return server_data['server']['uuid']
    else:
        pass

def create_swarm_hel2(payload, headers, url, zone):
    if zone != "fi-hel2":
        zone = "fi-hel2"
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        user_data = "#!/bin/bash\nyum updrade\n"
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title, user_data)),
            headers=headers())
        pprint.pprint(r.json())
        server_data = r.json()
        return server_data
    else:
        pass


def create_numbered_swarm():
    server_count = input("how many servers will be built?: ")
    for num in range(int(server_count)):
        x =+ 1
        print(x)
'''
#WEEEE
def create_swarm(payload, headers, url):
    datacenters = ['fi-hel1', 'uk-lon1']# add list of DCs]

    for zone in datacenters:
        datacenters = zone
        title = f"swarm01-{zone}"
        hostname = f"swarm01.{zone}"
        vda_title = f"swarm01-{zone}-vda"
        #user_data = (textwrap.dedent(f'''\
        #!/bin/bash\n
        #yum updrade\n
        #yum install -y vim epel-release\n
        #yum update\n
        #yum install -y git python python-devel python-pip openssl ansible\n
        #sed -i '22s/#//' /etc/ansible/ansible.cfg\n
        #sed -i '14s/#//' /etc/ansible/ansible.cfg"
        #    '''))
        r = requests.post(f"{url}server/", data=json.dumps(
            payload(zone, title, hostname, vda_title)),
            headers=headers())
        pprint.pprint(r.json())
        pass



create_swarm(payload, headers, url)

'''
master_server_data = create_server_master(payload, headers, url)


#ip_parser(master_server_data = create_server_master(payload, headers, url))
#ip_addr = master_server_data["server"]["ip_addresses"]["ip_address"][0]["address"]



#uuid_list = []
#uuid = server_data['server']['uuid']

# = create_swarm_ams1(payload, headers, url, zone)
#ams1_server_data = create_swarm_ams1(payload, headers, url, zone)
lon1_server_data = create_swarm_lon1(payload, headers, url, zone)
fra1_server_data = create_swarm_fra1(payload, headers, url, zone)
sin1_server_data = create_swarm_sin1(payload, headers, url, zone)
sjo1_server_data = create_swarm_sjo1(payload, headers, url, zone)
chi1_server_data = create_swarm_chi1(payload, headers, url, zone)
hel1_server_data = create_swarm_hel1(payload, headers, url, zone)
hel2_server_data = create_swarm_hel2(payload, headers, url, zone)'''
#uuid = server_data["server"]["uuid"]
