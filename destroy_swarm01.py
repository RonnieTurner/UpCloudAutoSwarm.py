import base64, requests, pprint, json


url = "https://api.upcloud.com/1.2/"

def headers():
    auth = base64.b64encode("apidev:F1ghtwar".encode())
    headers = {"Authorization": "Basic " + auth.decode(),
               "Content-Type": "application/json"}
    return headers


def host_uuid_array():
    r = requests.get(f"{url}server", headers=headers())

    server_list = r.json()

    my_dict = {}
    my_list = []

    for i in server_list['servers']['server']:
        my_dict[i['hostname']] = i['uuid']

    return my_dict


data = host_uuid_array()

print(data['fra1test'])
