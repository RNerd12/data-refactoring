from get_headers import getHeaders
from upload_to_mongo import uploadToMongo
from remap_excel import remapExcel
dirs = [
   r'89. Metals Minerals Industries Database\metals',
]
for i in dirs:
   # getHeaders(i)
   remapExcel(i)
   uploadToMongo(i + ' csv')
   pass
