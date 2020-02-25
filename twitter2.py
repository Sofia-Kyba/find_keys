import urllib.request, urllib.parse, urllib.error
import twurl
import json
import ssl

TWITTER_URL = 'https://api.twitter.com/1.1/friends/list.json'

# Ignore SSL certificate errors
ctx = ssl.create_default_context()
ctx.check_hostname = False
ctx.verify_mode = ssl.CERT_NONE


def friends_information():
    while True:
        try:
            print('')
            acct = input('Enter Twitter Account:')
            if len(acct) < 1:
                break
            url = twurl.augment(TWITTER_URL,
                                {'screen_name': acct, 'count': '100'})
            print('Retrieving', url)
            connection = urllib.request.urlopen(url, context=ctx)
            data = connection.read().decode()

            js = json.loads(data)
            with open('js.json', 'w') as f:
                json.dump(js, f, ensure_ascii=False, indent=4)
            dict = json.dumps(js, indent=2)
            return dict

            # headers = dict(connection.getheaders())
            # print('Remaining', headers['x-rate-limit-remaining'])

            # for u in js['users']:
            #     print(u['screen_name'])
            #     if 'status' not in u:
            #         print('   * No status found')
            #         continue
            #     s = u['status']['text']
            #     print('  ', s[:50])
        except:
            continue

# print(friends_information())