import json
import requests

URL = "http://localhost:8000/studentapi/"

                  # GET METHOD

def get_data(id = None):
	data = {}
	if id is not None:
		data = {'id' : id}
	json_data = json.dumps(data)
	r = requests.get(url = URL, data = json_data)
	data = r.json()
	print(data)

#get_data(2)
   
                   # POST METHOD

def post_data():
	data = {
	 'name' : 'rohan',
	 'roll' : 198,
	 'city' : 'surat'
	}

	json_data = json.dumps(data)
	r = requests.post(url = URL, data = json_data)
	data = r.json()
	print(data)

#post_data()

                    # UPDATE METHOD

def update_data():
	data = {
	 'id' : 12,
	 'name' : 'jack',
	 'city' : 'ranch',
	 'roll' : '99'
	}
	json_data = json.dumps(data)
	r = requests.put(url = URL, data = json_data)
	data = r.json()
	print(data)

update_data()
           
                        # DELETE METHOD

def delete_data():
	data = {'id' : 7}
	json_data = json.dumps(data)
	r= requests.delete(url = URL, data = json_data)
	data = r.json()
	print(data)

#delete_data()



