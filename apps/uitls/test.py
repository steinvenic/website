import requests
#res = requests.get('https://www.biqiuge.com/book/4772/')
#print(res.content.decode("gbk"))
ser = '一剑'

header = {
    'ie':'gbk',
    'siteid':'biqiuge.com',
    's':'2758772450457967865',
    'q':ser.encode('gbk')
}
res = requests.get('https://so.biqusoso.com/s.php',header)
print(res.content.decode('utf8'))