# -*- coding: utf-8 -*-
"""
Created on Fri Aug 05 15:05:57 2016

@author: SHIVDEEP
"""
import         sys
from           pool import ResourcePool 


def get_last_pada(d,k):
    #print type(d)
    if d.has_key(k):
        return d[k][1]

def get_total_padas(db):
    raag_keys = db.get_db_dict()[u"raag_range"].keys()
    raag_dict = db.get_db_dict()[u"raag_range"] 
    # corresponding to each key, which is the raag name, we have a
    # list of [start,end] number of padas in that raag.
    # make a list of ending number of each raag and find the largest to
    # find the total number of padas.
    
    list_last_pada_per_raga = []
    for i in raag_keys:
        list_last_pada_per_raga.append(get_last_pada(raag_dict,i))
    return max(list_last_pada_per_raga)

# Main Application Code
def main(arg):
	pool = ResourcePool()
	pool.pada_json_file   = "../db/kabir_pad_indexed.json"
	pool.sakhi_json_file  = "../db/sakhi_indexed.json"

	pool.prepare()

	resource_list         = pool.show_resource_list()

	pada_db               = pool.get_resource(resource_list[0])
	sakhi_db              = pool.get_resource(resource_list[1])

	# Here we get a pada as a resource

	# Prepare resource for usage
	pada_db.prepare()
	sakhi_db.prepare()

	# getting list of sakhis
	sakhi_list            = sakhi_db.sakhi_sequence
	print                   sakhi_list.__len__()
 
    # get the sakhi name from sakhi list
 	sakhi_num_20          = sakhi_list[11]
    # get the 12th sakhi name
    # get the 1st sakhi
 	print "Sakhi :%s"     % sakhi_num_20
	sakhi20               = sakhi_db.get_sakhi_pada(sakhi_num_20,1)
	print                   sakhi20.text	
 
    # print pada
	pada_number           = 69
	print "\nPada  number: %s" % pada_number
	pada_202              = pada_db.get_objn(pada_number)
	print                   pada_202.text

    # total number of padas
	total_padas           = get_total_padas(pada_db)
    
	#search a word in a pada or sakhi
    
	search                = u"नाम"
	print "Searching for: %s" % search
	if pada_202.has_text(search):
		print pada_202.get_line_containing(search)

	print "Searching in sakhi_db"
   # Easy way to search, just search the database
	foundlist             = sakhi_db.search(search)
	for result in foundlist:
		sakhi_chap        = result[0]
		sakhi_num         = result[1]
		print             sakhi_db.get_sakhi_pada(sakhi_chap,sakhi_num).text
	# TBD move this functionality to db from pada
	# Easy way to search, just search the database
	foundlist             = pada_db.search(search)
	for result in foundlist:
		print "Pada %s"   % result
		print             pada_db.get_objn(int(result)).get_line_containing(search)
	
if __name__ == "__main__":
    main(sys.argv)
