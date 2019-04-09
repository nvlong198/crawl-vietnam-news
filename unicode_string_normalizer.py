unicode_tohop = ['ẻ', 'é', 'è', 'ẹ', 'ẽ', 'ể', 'ế', 'ề', 'ệ', 'ễ', 'ỷ', 'ý', 'ỳ', 'ỵ', 'ỹ', 'ủ', 'ú', 'ù', 'ụ', 'ũ', 'ử', 'ứ', 'ừ', 'ự', 'ữ', 'ỉ', 'í', 'ì', 'ị', 'ĩ', 'ỏ', 'ó', 'ò', 'ọ', 'õ', 'ở', 'ớ', 'ờ', 'ợ', 'ỡ', 'ổ', 'ố', 'ồ', 'ộ', 'ỗ', 'ả', 'á', 'à', 'ạ', 'ã', 'ẳ', 'ắ', 'ằ', 'ặ', 'ẵ', 'ẩ', 'ấ', 'ầ', 'ậ', 'ẫ', 'Ẻ', 'É', 'È', 'Ẹ', 'Ẽ', 'Ể', 'Ế', 'Ề', 'Ệ', 'Ễ', 'Ỷ', 'Ý', 'Ỳ', 'Ỵ', 'Ỹ', 'Ủ', 'Ú', 'Ù', 'Ụ', 'Ũ', 'Ử', 'Ứ', 'Ừ', 'Ự', 'Ữ', 'Ỉ', 'Í', 'Ì', 'Ị', 'Ĩ', 'Ỏ', 'Ó', 'Ò', 'Ọ', 'Õ', 'Ở', 'Ớ', 'Ờ', 'Ợ', 'Ỡ', 'Ổ', 'Ố', 'Ồ', 'Ộ', 'Ỗ', 'Ả', 'Á', 'À', 'Ạ', 'Ã', 'Ẳ', 'Ắ', 'Ằ', 'Ặ', 'Ẵ', 'Ẩ', 'Ấ', 'Ầ', 'Ậ', 'Ẫ']
unicode_dungsan = ['ẻ', 'é', 'è', 'ẹ', 'ẽ', 'ể', 'ế', 'ề', 'ệ', 'ễ', 'ỷ', 'ý', 'ỳ', 'ỵ', 'ỹ', 'ủ', 'ú', 'ù', 'ụ', 'ũ', 'ử', 'ứ', 'ừ', 'ự', 'ữ', 'ỉ', 'í', 'ì', 'ị', 'ĩ', 'ỏ', 'ó', 'ò', 'ọ', 'õ', 'ở', 'ớ', 'ờ', 'ợ', 'ỡ', 'ổ', 'ố', 'ồ', 'ộ', 'ỗ', 'ả', 'á', 'à', 'ạ', 'ã', 'ẳ', 'ắ', 'ằ', 'ặ', 'ẵ', 'ẩ', 'ấ', 'ầ', 'ậ', 'ẫ', 'Ẻ', 'É', 'È', 'Ẹ', 'Ẽ', 'Ể', 'Ế', 'Ề', 'Ệ', 'Ễ', 'Ỷ', 'Ý', 'Ỳ', 'Ỵ', 'Ỹ', 'Ủ', 'Ú', 'Ù', 'Ụ', 'Ũ', 'Ử', 'Ứ', 'Ừ', 'Ự', 'Ữ', 'Ỉ', 'Í', 'Ì', 'Ị', 'Ĩ', 'Ỏ', 'Ó', 'Ò', 'Ọ', 'Õ', 'Ở', 'Ớ', 'Ờ', 'Ợ', 'Ỡ', 'Ổ', 'Ố', 'Ồ', 'Ộ', 'Ỗ', 'Ả', 'Á', 'À', 'Ạ', 'Ã', 'Ẳ', 'Ắ', 'Ằ', 'Ặ', 'Ẵ', 'Ẩ', 'Ấ', 'Ầ', 'Ậ', 'Ẫ']

normalizer = dict([('oà','òa'),('oá','óa'),('oả','ỏa'),('oã','õa'),('oạ','ọa'),('oè','òe'),('oé','óe'),('oẻ','ỏe'),('oẽ','õe'),('oẹ','ọe'),('uỳ','ùy'),('uý','úy'),('uỷ','ủy'),('uỹ','ũy'),('uỵ','ụy'),('Uỷ','Ủy')])
dic = dict(zip(unicode_tohop, unicode_dungsan)) # Make a pair of 2 lists and convert them to dict()

def compound_unicode(text):
  for tohop, dungsan in dic.items():
    text = text.replace(tohop, dungsan)
  return text

def nomalize_text(text):
  for absurd, normal in normalizer.items():
    text = text.replace(absurd, normal)
  return text

train = os.path.join('sentence-split','splitfilelower_number')
with open(train) as fopen:
  lines = fopen.readlines()
  lines = [nomalize_text(line) for line in lines]
with open(train, 'w') as fwrite:
  for line in lines:
        fwrite.write(line)
