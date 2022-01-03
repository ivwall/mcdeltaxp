import requests
import json
import datetime
import os
import subprocess

cdata_site = "https://api.coinstats.app/public/v1/coins?skip=0&limit=1000000"

class MCDelta():

    def wud():
        print("what's up doc?")

    def get_coin_stats():
        response = requests.get(cdata_site)
        print(type(response))
        text = json.dumps(response.json(), sort_keys=True,indent=4)
        print(text)

        print("response.status_code ",response.status_code)
        return response

    def pull_coin_n_market_cap():
        response = requests.get(cdata_site)
        print(type(response))
        text = json.dumps(response.json(), sort_keys=True,indent=4)
        print(text)

        print("response.status_code ",response.status_code)
        print("walk the json tree, pull coin n cap")

    def displaytimestamp():
        ct = datetime.datetime.now()
        print("current time:-", ct)
        ts = ct.timestamp()
        print("timestamp:-", ts)
        print(type(ts))
        ts_string = str(ts)
        print("time stamp string ", ts_string)
        ts_float = float(ts_string)
        print(ts_float)


    def create_file_with_timestamp_name():
        try:
            print(os.getcwd())
            dirpath = os.getcwd()
            print("current directory is : " + dirpath)
            foldername = os.path.basename(dirpath)
            print("Directory name is : " + foldername)
            scriptpath = os.path.realpath(__file__)
            print("Script path is : " + scriptpath)
            os.chdir('../mcdeltaxp/data')
            print(os.getcwd())

            path = os.getcwd()
            print(type(path))

            ct = datetime.datetime.now()
            print("current time:-", ct)
            ts = ct.timestamp()
            print("timestamp:-", ts)
            print(type(ts))
            ts_string = str(ts)
            print("time stamp string ", ts_string)

            pnn = path + os.path.sep + ts_string
            print( pnn ) 

            with open(pnn,"w") as variable_name:
                variable_name.write('incremental steps')            

            listOfFiles = os.listdir('.')
            #pattern = "*.py"
            for entry in listOfFiles:
                #if fnmatch.fnmatch(entry, pattern):
                print (entry)

            '''
            https://stackabuse.com/python-list-files-in-a-directory/
            # define the ls command
            ls = subprocess.Popen(["ls", "-p", "."],
                                stdout=subprocess.PIPE,
                                )

            # define the grep command
            grep = subprocess.Popen(["grep", "-v", "/$"],
                                    stdin=ls.stdout,
                                    stdout=subprocess.PIPE,
                                    )

            # read from the end of the pipe (stdout)
            endOfPipe = grep.stdout

            # output the files line by line
            for line in endOfPipe:
                print (line)
            '''
        except:
            print("error in create_file_with_timestamp_name")

    def writejson_to_timestamp_file():
        try:
            #os.chdir('../mcdeltaxp/data')
            # !!!!!!!!!!!!!!!!!!!!!!!
            # set in previous method call, most intreguing
            #
            path_2_data = os.getcwd()

            ct = datetime.datetime.now()
            ts = ct.timestamp()
            ts_string = str(ts)
            pnn = path_2_data + os.path.sep + ts_string
            print( pnn ) 

            response = requests.get(cdata_site)
            text = json.dumps(response.json(), sort_keys=True,indent=4)
            data = json.loads(text)
            file = open( pnn, "w")
            json.dump(data, file)
            file.close()

            '''
            listOfFiles = os.listdir('.')
            #pattern = "*.py"
            for entry in listOfFiles:
                #if fnmatch.fnmatch(entry, pattern):
                print (entry)
            '''
        except:
            print("ERROR writejson_to_timestamp_file")

    def delete_file(name):
        print( "delete this file "+name )

    def list_data_files():
        listOfFiles = os.listdir('.')
        for entry in listOfFiles:
            print (entry)
        print(type(listOfFiles))
        print("number of files is ",len(listOfFiles))

        more_than_10 = True
        while more_than_10:            
            if len(listOfFiles) > 10:
                listOfFiles = os.listdir('.')
                print(listOfFiles[0])
                file_number_1 = listOfFiles[0]
                file_number_2 = listOfFiles[1]
                file_number_3 = listOfFiles[2]
                path_2_data = os.getcwd()
                pnn = path_2_data + os.path.sep + file_number_1
                os.remove( pnn )
                pnn = path_2_data + os.path.sep + file_number_2
                os.remove( pnn )
                pnn = path_2_data + os.path.sep + file_number_3
                os.remove( pnn )
            else:
                more_than_10 = False


    def read_last_data_file():
        listOfFiles = os.listdir('.')
        file_list_len = len(listOfFiles)        
        last_file = listOfFiles[ file_list_len - 1]
        path_2_data = os.getcwd()
        pnn = path_2_data + os.path.sep + last_file
        print( pnn )
        f = open(pnn)
        data = json.load(f)
        f.close()
        #print(data)
        #text = json.dumps(response.json(), sort_keys=True,indent=4)
        text = json.dumps(data, sort_keys=True,indent=4)
        print(text)
        text = json.dumps(data["coins"][0], sort_keys=True,indent=4)
        print(text)
        print(data["coins"][0])
        print(data["coins"][0]["symbol"])
        print(data["coins"][0]["rank"])

        print(type(data["coins"]))
        number_of_coins = len(data["coins"])
        print(number_of_coins)
        for s in range(0,number_of_coins):
            symbol = data["coins"][s]["symbol"]
            rank = data["coins"][s]["rank"]
            print("  "+str(rank)+" "+symbol)





