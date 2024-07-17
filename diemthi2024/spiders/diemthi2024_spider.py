import scrapy
import json
import requests
from sqlite3 import dbapi2 as sqlite
        
class DiemThiSpider(scrapy.Spider):  
    name = "diemthi2024"
    # api_endpoint = "https://api.giaoducthoidai.vn/api/diem-thi"
    api_endpoint = "https://api.viettimes.vn/api/diem-thi"
    # api_endpoint = "https://api.giaoduc.net.vn/api/diem-thi"
    # api_endpoint = "https://api.sggp.org.vn/api/diem-thi"
    pattern_province = api_endpoint + "?type=0&keyword={:02d}0*&kythi=THPT&nam=2024&cumthi=0"
    pattern_group = api_endpoint + "?type=0&keyword={:02d}{:04d}*&kythi=THPT&nam=2024&cumthi=0"
    
    def __init__(self):
        self.connection = sqlite.connect('././diem.db')
        self.cursor = self.connection.cursor()
                            
    def start_requests(self):
        urls = []
        for province in range (0, 99):
            # Get each province
            contents = requests.get(self.pattern_province.format(province)).text
            js = json.loads(contents)
            if js['error_code'] == 0:
                results = js['data']['results']
                if len(results) > 0 and results[0] != None:
                    # Get last group
                    # print('Start find last group of province', province)
                    last_group = self.searchLastGroup(province)
                    print('Province', province, 'has last group', last_group)
                    for group in range(0, last_group+1):
                        result = self.cursor.execute("select * from diem where sbd like '{:02d}{:04d}%'".format(province,group)).fetchall()
                        if (group == 0 and len(result) != 99) or (group != 0 and len(result) != 100):
                            print('--> Crawl group', group, '- in database has', len(result), 'record(s)')
                            url = self.pattern_group.format(province,group)
                            yield scrapy.Request(url=url, callback=self.parse, meta={'length': len(result)})

    def parse(self, response):
        js = json.loads(response.body)
        length = response.meta.get('length')
        if js['error_code'] == 0:
            results = js['data']['results']
            if length == len(results):
                return
            for result in results:
                for key in result:
                    if result[key].startswith('-') or len(result[key]) == 0:
                        result[key] = None
                    elif key == 'sbd' or key == 'dmText':
                        result[key] = result[key]
                    else:
                        result[key] = float(result[key])
                yield result

    def searchLastGroup(self, province):
        low = 0
        high = 9999
        mid = 0
    
        while low <= high:
            mid = (high + low) // 2
            if self.isValidGroup(province,mid):
                low = mid + 1
            else:
                high = mid - 1
        return high
        
    
    def isValidGroup(self, province, group):
        contents = requests.get(self.pattern_group.format(province,group)).text
        js = json.loads(contents)
        if js['error_code'] == 0 and len(js['data']['results']) > 0:
            return True
        return False