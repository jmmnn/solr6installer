# -*- coding: utf-8 -*-

"""This is code for quick deletion of the solr index."""

import solr

############# CONFIGURATION #############
#file and folders

search_collection = 'new'
search_server = 'http://localhost:8080/solr/' + str(search_collection)

#########################################


s = solr.SolrConnection(search_server)  # Search server details 

#s.add(sentence = phrase, sdg = SDGs , publication = pub_name)

s.delete_query('*:*')
s.commit()

# response = s.query('*:*') # you can use this to see results

# for hit in response.results:
#     #print hit['sentence']
#     print hit
