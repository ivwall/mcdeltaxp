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

            listOfFiles = os.listdir('.')
            for entry in listOfFiles:
                print (entry)
            #https://stackabuse.com/python-list-files-in-a-directory/
        except:
            print("error in create_file_with_timestamp_name")

    def writejson_to_timestamp_file():
        try:
            #os.chdir('../mcdeltaxp/data')
            # set in previous method call, most intreguing
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

        more_than_10000 = True
        while more_than_10000:            
            if len(listOfFiles) > 10000:
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
                more_than_10000 = False


    def read_last_data_file():
        print("read_last_data_file()")
        listOfFiles = os.listdir('.')
        file_list_len = len(listOfFiles)        
        last_file = listOfFiles[ file_list_len - 1]
        path_2_data = os.getcwd()
        pnn = path_2_data + os.path.sep + last_file
        print( pnn )
        f = open(pnn)
        data = json.load(f)
        f.close()
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

    def develop_mcdelta_json():
        mcdelta_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta.json"
        print("")
        print(" working file: " + mcdelta_json_dev_file)
        print("")
        print("")
        f = open(mcdelta_json_dev_file)
        data = json.load(f)
        f.close()
        text = json.dumps(data, sort_keys=True,indent=4)
        print(text)


    def ruwb_json():
        print("read write update backup json")
        data_dir = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/data"
        os.chdir(data_dir)
        listOfFiles = os.listdir('.')
        for entry in listOfFiles:
            timestamp = date.fromtimestamp(float(entry))
            print("Date =", timestamp)
            print (entry)
        mcdelta_03_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_03.json"
        delta_json = open(mcdelta_03_json_dev_file)
        data = json.load(delta_json)
        delta_json.close()
        print(data)


    def write_mcdelta_html_from_json_data():
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

        mcdelta_03_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_03.json"
        delta_json = open(mcdelta_03_json_dev_file)
        data = json.load(delta_json)
        delta_json.close()

        dev2_html_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/mcdelta/dev4.html"

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
