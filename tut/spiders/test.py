import hashlib

link1 = 'https://vnexpress.net/kinh-doanh/chan-dung-hai-ty-phu-moi-cua-viet-nam-3890172.html'
link2 = 'https://vnexpress.net/kinh-doanh/dung-hai-ty-phu-moi-cua-viet-nam-3890172.html'


hash_obj = (hashlib.sha1(link1.encode()).hexdigest()) 
hash_obj2 = (hashlib.sha1(link2.encode()).hexdigest())
# print(hash_obj)
# print(hash_obj2)