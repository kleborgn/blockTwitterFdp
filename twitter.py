import re
import requests

# Exemple: 
# https://twitter.com/saintheee/status/1291319479339802624

def get_likes(tweet_id):
    val = 'https://twitter.com/i/activity/favorited_popup?id=%s' % (tweet_id)
    r = requests.get(val, stream=False, headers={'User-Agent':'facebookexternalhit/1.1 (+http://www.facebook.com/externalhit_uatext.php)'}, timeout=10, verify=True)
    text = r.text
    x = re.findall('div class=\\\\"account  js-actionable-user js-profile-popup-actionable \\\\" data-screen-name=\\\\"(.+?)\\\\" data-user-id=\\\\"', text)
    return x

print get_likes(1291319479339802624)