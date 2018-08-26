import requests, random, time, cfg

header = {'User-Agent': 'Mozilla/5.0 (iPhone; CPU iPhone OS 8_3 like Mac OS X) AppleWebKit/600.1.4 (KHTML, like Gecko) CriOS/42.0.2311.47 Mobile/12F70 Safari/600.1.4'}
js = {
 'OSVersion': '8.0.0',
 'android_channel': 'google',
 'android_id': cfg.android_id,
 'cid': None,
 'content_id': None,
 'content_type': '1',
 'deviceCode': cfg.deviceCode,
 'device_brand': 'samsung',
 'device_ip': None,
 'device_version': 'SM-A730F',
 'dtu': '001',
 'id': None,
 'lat': None,
 'lon': None,
 'network': 'wifi',
 'pack_channel': 'google',
 'sign': cfg.sign,
 'time': None,
 'tk': cfg.tk,
 'token': cfg.token,
 'uuid': cfg.uuid,
 'version': '10047',
 'versionName': '1.4.7'
}
url = []
id = []
print("[KubikBot-Python] - Ditulis oleh Rendyindo, berdasarkan kode radenvodka.")
print("[INFO] Downloading articles")
for cid in range(0,10):
    for page in range(0,5):
        print("[INFO] Downloading CID: {} | Page: {}".format(cid,page))
        r = requests.get('http://api.beritaqu.net/content/getList?cid='+ str(cid) +'&page=' + str(page)).json()
        if r['code'] != 0:
            print("[WARN] Skipping because non-0 response")
            continue
        for i in r['data']['data']:
            id.append(i['id'])
        page += 1

print("[INFO] Removing duplicate member and randomizing")
ids = list(set(id))
random.shuffle(ids)

for i in ids:
    print("[POST] ID: " + i)
    js['time'] = int(time.time()) + (30 * 60)
    js['content_id'] = i
    js['id'] = i
    js['cid'] = i
    js['device_ip'] = '114.124.239.{}'.format(str(random.randint(0,255)))
    res = requests.post("http://api.beritaqu.net/timing/read", data=js, headers=header).json()
    print("[RESULT] Message: {} | Amount: {} | Read second: {}".format(res['message'], res['data']['amount'], res['data']['current_read_second']))
    if res['message'] == "saat ini baca sudah capai max kesempatan":
        print("[WARN] Reached day limit. Exiting.")
        break
    time.sleep(5)
input()