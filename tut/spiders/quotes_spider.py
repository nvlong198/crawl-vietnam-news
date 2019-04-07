import scrapy
import unicodedata
from w3lib.html import remove_tags
from .parse import parse_vnex, parse_link_vnex, parse_dantri, parse_link_dantri, parse_link_k14, parse_kenh14
from .jsonparser import filter_json
f = open('kenh14.txt', 'a') # 'a' 
url_set = set()
class QuotesSpider(scrapy.Spider):
    name = "quotes"
    def start_requests(self):
        # list_of_paper = ['Vnexpress'] #'', 'Dân Trí', 'Kenh14.vn' Vnexpress
        # urls = ['https://vnexpress.net/', 'https://vnexpress.net/24h-qua', 'https://vnexpress.net/thoi-su', 'https://vnexpress.net/goc-nhin', 'https://vnexpress.net/the-gioi', 'https://vnexpress.net/kinh-doanh', 'https://vnexpress.net/giai-tri', 'https://vnexpress.net/the-thao', 'https://vnexpress.net/phap-luat', 'https://vnexpress.net/giao-duc', 'https://vnexpress.net/suc-khoe', 'https://vnexpress.net/doi-song', 'https://vnexpress.net/du-lich', 'https://vnexpress.net/khoa-hoc', 'https://vnexpress.net/si-hoa', 'https://vnexpress.net/oto-xe-may', 'https://vnexpress.net/y-kien', 'https://vnexpress.net/tam-su', 'https://vnexpress.net/cuoi', 'https://ione.vnexpress.net/', 'https://ione.vnexpress.net/tin-tuc/sao', 'https://ione.vnexpress.net/tin-tuc/phim', 'https://ione.vnexpress.net/tin-tuc/thoi-trang', 'https://ione.vnexpress.net/tin-tuc/nhip-song', 'https://ione.vnexpress.net/tin-tuc/chiem-tinh', 'https://ione.vnexpress.net/tin-tuc/quiz', 'https://ione.vnexpress.net/tin-tuc/ti-te']
        # urls = ['http://kenh14.vn/', 'http://kenh14.vn/star.chn', 'http://kenh14.vn/tv-show.chn', 'http://kenh14.vn/cine.chn', 'http://kenh14.vn/musik.chn', 'http://kenh14.vn/fashion.chn', 'http://kenh14.vn/doi-song.chn', 'http://kenh14.vn/an-ca-the-gioi.chn', 'http://kenh14.vn/xa-hoi.chn', 'http://kenh14.vn/the-gioi.chn', 'http://kenh14.vn/sport.chn', 'http://kenh14.vn/hoc-duong.chn', 'http://kenh14.vn/2-tek.chn']
        # urls = ['https://dantri.com.vn/', 'https://dantri.com.vn/su-kien.htm', 'https://dantri.com.vn/xa-hoi.htm', 'https://dantri.com.vn/the-gioi.htm', 'https://dantri.com.vn/the-thao.htm', 'https://dantri.com.vn/giao-duc-khuyen-hoc.htm', 'https://dantri.com.vn/tam-long-nhan-ai.htm', 'https://dantri.com.vn/kinh-doanh.htm', 'https://dantri.com.vn/bat-dong-san.htm', 'https://dantri.com.vn/van-hoa.htm', 'https://dantri.com.vn/giai-tri.htm', 'https://dantri.com.vn/phap-luat.htm', 'https://dantri.com.vn/nhip-song-tre.htm', 'https://dantri.com.vn/suc-khoe.htm', 'https://dantri.com.vn/suc-manh-so.htm', 'https://dantri.com.vn/o-to-xe-may.htm', 'https://dantri.com.vn/tinh-yeu-gioi-tinh.htm']
        
        # for paper in list_of_paper:
            # urls.extend(filter_json(paper))
            # url_set.update(filter_json(paper))
        # urls = ['https://dantri.com.vn/o-to-xe-may/mercedes-benz-viet-nam-chua-ro-co-bao-nhieu-xe-glc-bi-nuoc-vao-cau-20180828064320354.htm']
        with open('linkk142.txt') as f2:
            urls = f2.readlines()
        urls = [url.strip() for url in urls]
        url_set.update(urls)
        for url in urls:
            # f.write(url+'\n')
            yield scrapy.Request(url=url, callback=self.parse)
    
    def parse(self, responses):
        content = parse_kenh14(self, responses)
        # print('content+', content)
        for element in content:
            element = unicodedata.normalize("NFKD", element)
            f.write(element +'\n') 
    
    def parse_href_vnex(self, responses):
        urls = parse_link_vnex(self, responses)
        urls = [url for url in urls if url not in url_set]
        for element in urls:
            print(element)
            element = unicodedata.normalize("NFKD", element)
            f.write(element+'\n') 
        url_set.update(set(urls))

    def parse_href_dantri(self, responses):
        urls = parse_link_dantri(self, responses)
        urls = [url for url in urls if url not in url_set]
        for element in urls:
            element = unicodedata.normalize("NFKD", element)
            f.write('http://www.dantri.com.vn'+element + '\n') 
        url_set.update(set(urls))

    def parse_href_kenh14(self, responses):
        urls = parse_link_k14(self, responses)
        urls = ['http://kenh14.vn'+url for url in urls if 'http://kenh14.vn'+url not in url_set]
        for element in urls:
            element = unicodedata.normalize("NFKD", element)
            f.write(element +'\n') 
        url_set.update(set(urls))

