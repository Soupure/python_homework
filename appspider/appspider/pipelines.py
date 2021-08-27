# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from models import  App, Session

class AppspiderPipeline:
    def __init__(self):
        self.session = Session()

    def process_item(self, item, spider):
        #save item to database
        game = App()
        game.title = item['title']
        game.url =item['url']
        game.icon = item['icon']
        game.desc = item['desc']
        game.source = spider.name

        session = self.session
        try:
            session.add(game)
            session.commit()
        except:
            session.rollback()
            raise

        finally:
            session.close()

        return item
