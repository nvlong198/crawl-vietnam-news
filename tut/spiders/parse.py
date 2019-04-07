import scrapy, string
from w3lib.html import remove_tags
import re

def parse_link_k14(self, response):
	list_href = response.css('a::attr(href)').getall()
	list_href = list(set(filter(lambda x: re.match(r'^(\/)([\w-]){30,}(\.chn)$', x), list_href)))
	return list_href
	
def parse_kenh14(self, response):
	list_elements = []
	list_elements.extend(response.css('h1.kbwc-title::text').getall())
	list_elements.extend(response.css('h2.knc-sapo::text').getall())
	list_elements.extend(response.css('div.knc-content p').getall())
	# list_elements = [for e in list_elements]
	list_elements = [remove_tags(e).strip() for e in list_elements]
	list_elements = [e.strip() for e in list_elements if e.strip()!='']
	list_elements = list(filter(lambda item: item not in string.punctuation, list_elements))
	
	return list_elements

def parse_link_dantri(self, response):
	list_href = response.css('a::attr(href)').getall()
	list_href = list(set(filter(lambda x: re.match(r'^(\/)(\w+\-){1,}(\w+\/)(\w+\-){3,}\d+.htm$', x), list_href)))
	return list_href

def parse_dantri(self, response):
	list_elements = []
	list_elements.extend(response.css('h1.fon33::text').getall())
	list_elements.extend(response.css('h1.fon31::text').getall())
	list_elements.extend(response.css('div#divNewsContent p').getall())
	list_elements.extend(response.css('figcaption p::attr(alt)').getall())
	list_elements = [remove_tags(e).strip() for e in list_elements]
	list_elements = list(filter(None, [element.strip() for element in list_elements] ))
	list_elements = list(filter(lambda item: item not in string.punctuation, list_elements))
	return (list_elements)

def parse_link_vnex(self, response):
	list_href = response.css('a::attr(href)').getall()
	list_href = list(set(filter(lambda x: re.match(r'^((^|, )((https:\/\/vnexpress.net\/)|(https:\/\/ione.vnexpress.net\/))).+.html$', x), list_href)))
	return list_href

def parse_vnex(self, response):
	list_elements = []
	list_elements.append(response.css("h1.title_news_detail::text").get().strip()+". ")
	list_elements.append(response.css("p.description::text").get().strip())
	category_set = {'Thể thao','Sức khỏe','Pháp luật','Đời sống','Du lịch', 'Khoa học', 'Xe', 'Ý kiến', 'Tâm sự', 'Cười'}
	if response.css('a.active::text').get().strip() in category_set:
		return parse_vnex_thethao(self, response, list_elements)
	else:# response.css('a.active::text').get() == 'Kinh doanh, thoi su, the gioi, giai tri':
		return parse_vnex_kinhdoanh(self, response, list_elements)

def parse_vnex_thethao(self, response, list_elements):
	list_elements.extend(response.css('article.content_detail p').getall())
	# for n, element in enumerate(list_elements):
	list_elements = [remove_tags(element).strip() for element in list_elements]
	list_elements = list(filter(None, [element.strip() for element in list_elements] ))
		# print(list_elements[n])
	return list_elements


def parse_vnex_kinhdoanh(self, response, list_elements):
	# response.css('div.title_news h1::text').get()
	#response.css('h2.short_intro::text').get()
	list_elements.extend(response.css("p.Normal").getall())
	list_elements.extend(response.css("div.desc_cation").getall())
	list_elements.extend(response.css("p.Image").getall())
	list_elements = [remove_tags(element).strip() for element in list_elements] 
	list_elements = list(filter(None, [element.strip() for element in list_elements] ))
	return list_elements
	