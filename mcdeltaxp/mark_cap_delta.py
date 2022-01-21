from operator import truediv
import requests
import json
import datetime
from datetime import date
import os

cdata_site = "https://api.coinstats.app/public/v1/coins?skip=0&limit=1000000"

class MCDelta():

    def get_coin_stats():
        response = requests.get(cdata_site)
        #print(type(response))
        text = json.dumps(response.json(), sort_keys=True,indent=4)
        #print(text)
        #print("response.status_code ",response.status_code)
        return response

    def pull_coin_n_market_cap():
        response = requests.get(cdata_site)
        #print(type(response))
        text = json.dumps(response.json(), sort_keys=True,indent=4)
        #print(text)
        #print("response.status_code ",response.status_code)
        #print("walk the json tree, pull coin n cap")

    def displaytimestamp():
        ct = datetime.datetime.now()
        #print("current time:-", ct)
        ts = ct.timestamp()
        #print("timestamp:-", ts)
        #print(type(ts))
        ts_string = str(ts)
        #print("time stamp string ", ts_string)
        ts_float = float(ts_string)
        #print(ts_float)


    def create_file_with_timestamp_name():
        try:
            #print(os.getcwd())
            dirpath = os.getcwd()
            #print("current directory is : " + dirpath)
            foldername = os.path.basename(dirpath)
            #print("Directory name is : " + foldername)
            scriptpath = os.path.realpath(__file__)
            #print("Script path is : " + scriptpath)
            os.chdir('../mcdeltaxp/data')
            #print(os.getcwd())

            path = os.getcwd()
            #print(type(path))

            ct = datetime.datetime.now()
            #print("current time:-", ct)
            ts = ct.timestamp()
            #print("timestamp:-", ts)
            #print(type(ts))
            ts_string = str(ts)
            #print("time stamp string ", ts_string)

            pnn = path + os.path.sep + ts_string
            #print( pnn ) 

            #listOfFiles = os.listdir('.')
            #for entry in listOfFiles:
            #    print (entry)
            #https://stackabuse.com/python-list-files-in-a-directory/
        except:
            print("error in create_file_with_timestamp_name")

    def writejson_to_timestamp_file():
        try:
            os.chdir('../mcdeltaxp/data')
            # set in previous method call, most intreguing
            path_2_data = os.getcwd()

            ct = datetime.datetime.now()
            ts = ct.timestamp()
            ts_string = str(ts)
            pnn = path_2_data + os.path.sep + ts_string
            #print( pnn )

            date_time_str =  ct.strftime("%Y%m%d%H%M%S")

            print ("Current date and time : ")
            print (date_time_str)

            response = requests.get(cdata_site)
            text = json.dumps(response.json(), sort_keys=True,indent=4)
            data = json.loads(text)
            file = open( pnn, "w")
            json.dump(data, file)
            file.close()
        except:
            print("ERROR writejson_to_timestamp_file")

    def delete_file(name):
        print( "delete this file "+name )

    def list_data_files():
        listOfFiles = os.listdir('.')
        #for entry in listOfFiles:
        #    print (entry)
        #print(type(listOfFiles))
        #print("number of files is ",len(listOfFiles))

        more_than_10000 = True
        while more_than_10000:            
            if len(listOfFiles) > 10000:
                listOfFiles = os.listdir('.')
                #print(listOfFiles[0])
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
                more_than_10000 = False


    def read_last_data_file():
        #print("read_last_data_file()")
        listOfFiles = os.listdir('.')
        file_list_len = len(listOfFiles)        
        last_file = listOfFiles[ file_list_len - 1]
        path_2_data = os.getcwd()
        pnn = path_2_data + os.path.sep + last_file
        #print( pnn )
        f = open(pnn)
        data = json.load(f)
        f.close()
        text = json.dumps(data, sort_keys=True,indent=4)
        #print(text)
        text = json.dumps(data["coins"][0], sort_keys=True,indent=4)
        #print(text)
        #print(data["coins"][0])
        #print(data["coins"][0]["symbol"])
        #print(data["coins"][0]["rank"])

        #print(type(data["coins"]))
        number_of_coins = len(data["coins"])
        #print(number_of_coins)
        for s in range(0,number_of_coins):
            symbol = data["coins"][s]["symbol"]
            rank = data["coins"][s]["rank"]
            #print("  "+str(rank)+" "+symbol)

    def develop_mcdelta_json():
        mcdelta_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta.json"
        #print("")
        #print(" working file: " + mcdelta_json_dev_file)
        #print("")
        #print("")
        f = open(mcdelta_json_dev_file)
        data = json.load(f)
        f.close()
        text = json.dumps(data, sort_keys=True,indent=4)
        #print(text)


    def ruwb_json():
        print("read write update backup json")
        data_dir = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/data"
        os.chdir(data_dir)
        listOfFiles = os.listdir('.')
        for entry in listOfFiles:
            timestamp = date.fromtimestamp(float(entry))
            #print("Date =", timestamp)
            #print (entry)
        mcdelta_03_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_03.json"
        delta_json = open(mcdelta_03_json_dev_file)
        data = json.load(delta_json)
        delta_json.close()
        #print(data)


    def write_mcdelta_html_from_03json_data():
        #https://stackoverflow.com/questions/34818782/iterate-through-nested-json-object-and-get-values-with-python
        def write_header_row(data,f):
            f.write("<tr>")
            for key,value in data.items():
                f.write("<th style=\"left: 0px;\">")
                f.write(key)
                f.write("</th>")
                for element in data[key]:
                    f.write("<th>")
                    f.write(element)
                    f.write("</th>")
            f.write("</tr>")

        def write_row(data,f):
            f.write("<tr>")
            for key,value in data.items():
                f.write("<td style=\"left: 0px;\">")
                f.write(key)
                f.write("</td>")
                for element in data[key]:
                    f.write("<td>")
                    f.write(element)
                    f.write("</td>")
            f.write("</tr>")

        dev2_html_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/mcdelta/dev3.html"

        try:
            os.remove( dev2_html_file )
        except:
            print("file does not exist")

        f = open(dev2_html_file, "w")
        f.write("<!DOCTYPE html>\n")
        f.write("<html ng-app=\"plunker\">\n")
        f.write("  <head>\n")
        f.write("    <meta charset=\"utf-8\" />\n")
        f.write("    <title>MC Delta - Market Cap Changes</title>\n")
        f.write("    <script>document.write('<base href=\"' + document.location + '\" />');</script>")
        f.write("    <link rel=\"stylesheet\" href=\"style.css\" />")
        f.write("    <script data-require=\"angular.js@1.3.x\" src=\"https://code.angularjs.org/1.3.20/angular.js\" data-semver=\"1.3.20\"></script>")
        f.write("    <script data-require=\"jquery@3.1.1\" data-semver=\"3.1.1\" src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js\"></script>")
        f.write("    <script src=\"app.js\"></script>")
        f.write("    <script>")
        f.write("      $(document).ready(function() {")
        f.write("  $('tbody').scroll(function(e) { //detect a scroll event on the tbody")
        f.write("  	/*")
        f.write("    Setting the thead left value to the negative valule of tbody.scrollLeft will make it track the movement")
        f.write("    of the tbody element. Setting an elements left value to that of the tbody.scrollLeft left makes it maintain 			it's relative position at the left of the table.    ")
        f.write("    */\n")
        f.write("    $('thead').css(\"left\", -$(\"tbody\").scrollLeft()); //fix the thead relative to the body scrolling\n")
        f.write("    $('thead th:nth-child(1)').css(\"left\", $(\"tbody\").scrollLeft()); //fix the first cell of the header\n")
        f.write("    $('tbody td:nth-child(1)').css(\"left\", $(\"tbody\").scrollLeft()); //fix the first column of tdbody\n")
        f.write("  });")
        f.write("});")
        f.write("    </script>")
        f.write("  </head>")
        f.write("  <body ng-controller=\"MainCtrl\">")
        f.write("<br/>")
        f.write("<br/>")
        f.write("<br/>")
        f.write("<br/>")
        
        mcdelta_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_03.json"
        delta_json = open(mcdelta_json_dev_file)
        data = json.load(delta_json)
        delta_json.close()
        mcdelta_list = data["mcdelta"]
        header_row = True
        
        f.write("<table>")
        for val in mcdelta_list:
            if header_row:
                f.write("<thead>")
                write_header_row(val,f)
                header_row = False
                f.write("</thead>")
                f.write("<tbody>")
            else:
                write_row(val,f)

        f.write("</tbody>")
        f.write("</table>")
        f.write("")
        f.write("  </body>")
        f.write("</html>")
        f.close()


    def write_mcdelta_html_from_04json_data():
        print("04json work")
        def write_header_row(data,f):
            f.write("<tr>")
            for key,value in data.items():
                f.write("<th style=\"left: 0px;\">")
                f.write(key)
                f.write("</th>")
                for element in data[key]:
                    f.write("<th>")
                    f.write(element)
                    f.write("</th>")
            f.write("</tr>")

        ''''''
        def walk_through_cell_attribute_list(data,f):
            #print("walk_through_cell_attribute_list ", type(data), data)
            for x in data:
                #print(x)
                #print(x["delta"])
                #print(x["var1"])
                if x["delta"] == "+1":
                    #print("+1")
                    f.write("<td style=\"background-color:#a8d08d; text-align:center;\">")
                elif x["delta"] == "-1":
                    #print("-1")
                    f.write("<td style=\"background-color:#e99d9b; text-align:center;\">")

        def parse_cell_item(data,f):
            #print("parse cell item ", type(data), data)
            for key,value in data.items():
                cellString = key
                #print("key ",cellString)
                #print("value type ",type(value), value)
                if type(value) == type(list()):
                    walk_through_cell_attribute_list(value,f)
                f.write(cellString)
                f.write("</td>")

        ''''''
        def write_row(data,f):
            f.write("<tr>")
            for key,value in data.items():
                f.write("<td style=\" text-align:center; 0px;\">")
                f.write(key)
                f.write("</td>")
                for element in data[key]:
                    #print("element type ",type(element),element)
                    if type(element) == type(str()):
                        f.write("<td style=\"background-color:#a3cced; text-align:center;\">")
                        f.write(element)
                        f.write("</td>")
                    else:
                        parse_cell_item(element,f)
            f.write("</tr>")

        dev2_html_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/mcdelta/dev4.html"

        try:
            os.remove( dev2_html_file )
        except:
            #print("file does not exist")
            pass

        f = open(dev2_html_file, "w")
        f.write("<!DOCTYPE html>\n")
        f.write("<html ng-app=\"plunker\">\n")
        f.write("  <head>\n")
        f.write("    <meta charset=\"utf-8\" />\n")
        f.write("    <title>MC Delta - Market Cap Changes</title>\n")
        f.write("    <script>document.write('<base href=\"' + document.location + '\" />');</script>")
        f.write("    <link rel=\"stylesheet\" href=\"style.css\" />")
        f.write("    <script data-require=\"angular.js@1.3.x\" src=\"https://code.angularjs.org/1.3.20/angular.js\" data-semver=\"1.3.20\"></script>")
        f.write("    <script data-require=\"jquery@3.1.1\" data-semver=\"3.1.1\" src=\"https://ajax.googleapis.com/ajax/libs/jquery/3.1.1/jquery.min.js\"></script>")
        f.write("    <script src=\"app.js\"></script>")
        f.write("    <script>")
        f.write("      $(document).ready(function() {")
        f.write("  $('tbody').scroll(function(e) { //detect a scroll event on the tbody")
        f.write("  	/*")
        f.write("    Setting the thead left value to the negative valule of tbody.scrollLeft will make it track the movement")
        f.write("    of the tbody element. Setting an elements left value to that of the tbody.scrollLeft left makes it maintain 			it's relative position at the left of the table.    ")
        f.write("    */\n")
        f.write("    $('thead').css(\"left\", -$(\"tbody\").scrollLeft()); //fix the thead relative to the body scrolling\n")
        f.write("    $('thead th:nth-child(1)').css(\"left\", $(\"tbody\").scrollLeft()); //fix the first cell of the header\n")
        f.write("    $('tbody td:nth-child(1)').css(\"left\", $(\"tbody\").scrollLeft()); //fix the first column of tdbody\n")
        f.write("  });")
        f.write("});")
        f.write("    </script>")
        f.write("  </head>")
        f.write("  <body ng-controller=\"MainCtrl\">")
        f.write("<br/>")
        f.write("<br/>")
        f.write("<br/>")
        f.write("<br/>")
        
        mcdelta_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_04.json"
        delta_json = open(mcdelta_json_dev_file)
        data = json.load(delta_json)
        delta_json.close()
        mcdelta_list = data["mcdelta"]
        header_row = True
        
        f.write("<table>")
        for val in mcdelta_list:
            if header_row:
                f.write("<thead>")
                write_header_row(val,f)
                header_row = False
                f.write("</thead>")
                f.write("<tbody>")
            else:
                write_row(val,f)

        f.write("</tbody>")
        f.write("</table>")
        f.write("")
        f.write("  </body>")
        f.write("</html>")
        f.close()

    def generate_or_update_mcdelta_0x_json():
        #https://howtodoinjava.com/python/json/append-json-to-file/
        print("generate_or_update_mcdelta_0x_json")

        mcdelta_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_05.json"
        mcdelta_obj = {}

        if os.path.isfile(mcdelta_json_dev_file) is False:
            mcdelta_obj.update({
                "mcdelta":[]
            })
        else:
            with open(mcdelta_json_dev_file) as fp:
                mcdelta_obj = json.load(fp)

        #print(mcdelta_obj)
        obj = mcdelta_obj["mcdelta"]
        #print("type ",type(obj), obj)
        mcdelta_obj["mcdelta"].insert(0,{"dates":[]})
        #print(mcdelta_obj)

        with open(mcdelta_json_dev_file, 'w') as json_file:
            #json.dump(mcdelta_obj, json_file, 
            #    indent=2,  
            #    separators=(',',': '))
            json.dump(mcdelta_obj, json_file)
            
    def update_mcdelta_0x_from_raw_data():
        print("update_mcdelta_0x_from_raw_data()")
        #https://howtodoinjava.com/python/json/append-json-to-file/

        mcdelta_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_06.json"
        mcdelta_obj = {}

        if os.path.isfile(mcdelta_json_dev_file) is False:
            mcdelta_obj.update({
                "mcdelta":[]
            })
        else:
            with open(mcdelta_json_dev_file) as fp:
                mcdelta_obj = json.load(fp)

        #print(mcdelta_obj)
        obj = mcdelta_obj["mcdelta"]
        #print("type ",type(obj), obj)

        #---------------------------------------------------------------------------------

        listOfFiles = os.listdir('.')
        file_list_len = len(listOfFiles)        
        last_file = listOfFiles[ file_list_len - 1]
        path_2_data = os.getcwd()
        pnn = path_2_data + os.path.sep + last_file
        #print( pnn )
        f = open(pnn)
        data = json.load(f)
        f.close()
        text = json.dumps(data, sort_keys=True,indent=4)
        #print(text)
        text = json.dumps(data["coins"][0], sort_keys=True,indent=4)
        #print(text)
        #print(data["coins"][0])
        #print(data["coins"][0]["symbol"])
        #print(data["coins"][0]["rank"])

        if type(mcdelta_obj["mcdelta"]) == type(list()):
            mcdelta_length = len(mcdelta_obj["mcdelta"])
            #print("mcdelt_length", mcdelta_length)
            if mcdelta_length == 0:
                mcdelta_obj["mcdelta"].insert(0,{"dates":[]})
                #print("insert dates row, row 0")

        if type(mcdelta_obj["mcdelta"]) == type(list()):
            mcdelta_length = len(mcdelta_obj["mcdelta"])
            #print("mcdelt_length", mcdelta_length)
            if mcdelta_length == 1:
                #print(type(data["coins"]))
                number_of_coins = len(data["coins"])
                #print(number_of_coins)
                for s in range(0,number_of_coins):
                    x = s + 1
                    symbol = data["coins"][s]["symbol"]
                    rank = data["coins"][s]["rank"]
                    #print("  "+str(rank)+" "+symbol)
                    mcdelta_obj["mcdelta"].insert(x,{str(x):[]})
                print("contains dates row")
                print("               row 1")

        #print(mcdelta_obj["mcdelta"][0])
        #print(mcdelta_obj)

        with open(mcdelta_json_dev_file, 'w') as json_file:
            json.dump(mcdelta_obj, json_file)
