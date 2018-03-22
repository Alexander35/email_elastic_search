from elasticsearch_dsl.connections import connections
from elasticsearch_dsl import DocType, Text, Date, Search
from elasticsearch.helpers import bulk
from elasticsearch import Elasticsearch
from . import models


connections.create_connection()

class EmailIndex(DocType):
	title = Text()
	sender = Text()
	date = Date()
	text = Text()

	class Meta:
		index = 'email-index'


def bulk_indexing():
	EmailIndex.init()
	es = Elasticsearch()
	bulk(client=es, actions=(b.indexing() for b in models.Email.objects.all().iterator()))		

def search(title):
	s = Search().filter('term', title=title)
	response = s.execute()

	return response	