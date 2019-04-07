import urllib.request, json
# a = urllib.request.urlopen('http://theodoibaochi.com/export/article_data.json')
# a = a.read().decode("utf-8")
# a.replace('\"',"\'")
with open('tut/spiders/article_data.json') as f:
   a = f.readline()

def filter_json(paper_name):
   json_obj = json.loads(a)
   paper_links = []

   for segment in json_obj['article_list']:
      if segment['newspaper'] == paper_name:
         paper_links.append(segment['href'])
   return list(set(paper_links))