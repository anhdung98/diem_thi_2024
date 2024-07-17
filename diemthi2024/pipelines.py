# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from sqlite3 import dbapi2 as sqlite


class Diemthi2024Pipeline:
    def __init__(self):
        self.connection = sqlite.connect('./diem.db')
        self.cursor = self.connection.cursor()
        self.cursor.execute('CREATE TABLE IF NOT EXISTS diem '
                            '(sbd TEXT PRIMARY KEY, toan REAL, ngu_van REAL, ngoai_ngu REAL, '
                            'vat_li REAL, hoa_hoc REAL, sinh_hoc REAL, lich_su REAL, dia_li REAL, gdcd REAL, ma_ngoai_ngu VARCHAR(2))')
                            
    def process_item(self, item, spider):
        self.cursor.execute("select sbd from diem where sbd=(?)", [item['sbd']])
        result = self.cursor.fetchone()
        if not result:
            self.cursor.execute(
                "insert into diem (sbd, toan, ngu_van, ngoai_ngu, vat_li, hoa_hoc, sinh_hoc, lich_su, dia_li, gdcd, ma_ngoai_ngu) values (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)",
                [item['sbd'], item['dm01'], item['dm02'], item['dm07'], item['dm03'], item['dm04'], item['dm05'], item['dm08'], item['dm09'], item['dm10'], item['dmText']])
            self.connection.commit()
        return item
