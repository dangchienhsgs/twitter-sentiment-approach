import sys
from itertools import izip
import uuid
import base64


# get a UUID - URL safe, Base64
def get_a_uuid():
    r_uuid = base64.urlsafe_b64encode(uuid.uuid4().bytes)
    return r_uuid.replace('=', '')


f1 = open("test_small.csv")
f2 = open("test_tweet_tokenised.txt")

data = []
for line1, line2 in izip(f1, f2):
    words1 = line1.strip().split('|||')
    words2 = line2.strip().split('\t')
    string = get_a_uuid() + '\t' + words2[0] + '\t' + words2[1] + '\t' + words1[0] + '\n'
    print line1
    print line2
    data.append(string)

f1.close()
f2.close()

f = open("final_small_test.csv", 'w')
f.write("".join(data))
f.close()
