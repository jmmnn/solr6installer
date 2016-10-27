# -*- coding: utf-8 -*-

"""This program injests data into a Solr Server in schemaless mode.
    """
import solr  # More about this python package see: https://github.com/edsu/solrpy

############# CONFIGURATION #############

search_collection = 'new'     ##define the collection name
search_server = 'http://localhost:8080/solr/' + str(search_collection)

#########################################

### Injestion function ####
  
def injest ():
    ###### Search server details 
    s = solr.SolrConnection(search_server)  
    
    ###### Inject results to solr
    try:
        s.add ( Source = 'MySource', SDG = '17' , Sentence = 'hello world' , Type = 'article') # This is a sample doc
        print 'Injested a doc'
        s.commit()           
    except:
        print 'Error'
        
#Trigger the work
injest()
