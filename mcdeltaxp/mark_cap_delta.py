from operator import truediv
import json
from datetime import date
import os

cdata_site = "https://api.coinstats.app/public/v1/coins?skip=0&limit=1000000"

class MCDelta():

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


    def write_mcdelta_html_from_11json_data():
        print("11json work")
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

        dev11_html_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/mcdelta/dev11.html"

        try:
            os.remove( dev11_html_file )
        except:
            #print("file does not exist")
            pass

        f = open(dev11_html_file, "w")
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
        
        mcdelta_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_11.json"
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
        f = open(last_file)
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
            if mcdelta_length == 1:   # <==== meaning, only the header, date, row exists
                #print(type(data["coins"]))
                number_of_coins = len(data["coins"])
                #print(number_of_coins)
                for s in range(0,number_of_coins):  # <=== add a row for each coin
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


    def generate_from_scratch_mcdelta_11json_file():
        #---------------------------------------------------------------------------------
        #
        # If mcdelta_11.json does not exist then
        # create the file and update it with the root, json dict(ionary) object, mcdelta
        # 

        mcdelta_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_11.json"
        mcdelta_obj = {}
        if os.path.isfile(mcdelta_json_dev_file) is False:
            mcdelta_obj.update({
                "mcdelta":[]
            })
            with open(mcdelta_json_dev_file, 'w') as json_file:
                json.dump(mcdelta_obj, json_file)

        else:
            with open(mcdelta_json_dev_file) as fp:
                mcdelta_obj = json.load(fp)

        #with open(mcdelta_json_dev_file, 'w') as json_file:
        #    json.dump(mcdelta_obj, json_file)

        #--------------------------------------------------------------------------------
        #
        # Pull out market data from a reference file  
        #
        '''
        os.chdir('/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/01-reference-data')
        listOfFiles = os.listdir('.')
        file_list_len = len(listOfFiles)        
        last_file = listOfFiles[ file_list_len - 1 ]
        path_2_data = os.getcwd()
        pnn = path_2_data + os.path.sep + last_file
        print( pnn )
        '''

        for file in sorted(os.listdir('/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/01-reference-data')):
            print(">> ",file)
            last_file = file
            pnn = file

        last_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/01-reference-data/"+last_file
        print(">>> last file", last_file)
        f = open(last_file)
        crypto_market_data = json.load(f)
        f.close()

        #--------------------------------------------------------------------------------
        #
        # Add column 1: date for header row
        #               rows for cap ex listing, current 2000 rows
        #

        if type(mcdelta_obj["mcdelta"]) == type(list()):
            mcdelta_length = len(mcdelta_obj["mcdelta"])
            if mcdelta_length == 0:
                mcdelta_obj["mcdelta"].insert(0,{"dates":[]})

        if type(mcdelta_obj["mcdelta"]) == type(list()):
            mcdelta_length = len(mcdelta_obj["mcdelta"])
            if mcdelta_length == 1:   # <==== meaning, only the header row exists

                number_of_coins = len(crypto_market_data ["coins"])

                for s in range(0,number_of_coins):  # <=== add a row for each coin
                    x = s + 1
                    mcdelta_obj["mcdelta"].insert(x,{str(x):[]})

        #--------------------------------------------------------------------------------
        #
        # Write, dump, the file
        #

        with open(mcdelta_json_dev_file, 'w') as json_file:
            json.dump(mcdelta_obj, json_file)

    def update_mcdelta_11json_file():
        print("update_mcdelta_11json_file")
        #---------------------------------------------------------------------------------
        #
        # If mcdelta_11.json does not exist then 
        # ( what a pain, python can't call in methods in the class/file
        #
        # create the file and update it with the root, json dict(ionary) object, mcdelta
        # the create did not work
        # 
        mcdelta_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_11.json"
        mcdelta_obj = {}
        try:
            with open(mcdelta_json_dev_file) as fp:
                mcdelta_obj = json.load(fp)
        except FileNotFoundError:
            print("FileNotFoundError 01 in update_mcdelta_11json_file")
        except:
            print("ERROR 01 in update_mcdelta_11json_file")

        #--------------------------------------------------------------------------------
        #
        # Pull out market data from the newest reference file  
        #
        last_file = ""
        for file in sorted(os.listdir('/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/01-reference-data')):
            last_file = file

        dir_and_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/01-reference-data/"+last_file
        print(">>> last file", dir_and_file)
        f = open(dir_and_file)
        crypto_market_data = json.load(f)
        f.close()

        #--------------------------------------------------------------------------------
        #
        # The mcdelta date format
        #
        print("last file name ", last_file)
        left_str = last_file.split(".")
        print(left_str)
        print(left_str[0])
        date_object = date.fromtimestamp(int(left_str[0]))
        print(date_object)
        time_object = date.fromtimestamp(int(left_str[1]))
        print(time_object)

        print("date_object type ", type(date_object))
        date_str = str(date_object)
        print(date_str)
        date_split = date_str.split('-')
        print(date_split)
        print(date_split[1])

        year = "not set"
        if date_split[0] == "2022":
            year = "2"
        elif date_split[0] == "2023":
            year = "3"

        month = "not set"
        if date_split[1] == "01":
            month = "Ja"
        elif date_split[1] == "02":
            month = "Fe"
        elif date_split[1] == "03":
            month = "Mr"
        elif date_split[1] == "04":
            month = "Ap"
        elif date_split[1] == "05":
            month = "Ma"
        elif date_split[1] == "06":
            month = "Jn"
        elif date_split[1] == "07":
            month = "Jl"
        elif date_split[1] == "08":
            month = "Au"
        elif date_split[1] == "09":
            month = "Sp"
        elif date_split[1] == "10":
            month = "Oc"
        elif date_split[1] == "11":
            month = "Nv"
        elif date_split[1] == "12":
            month = "De"

        #print(month) #  dead code, remove it
        date_header = month + date_split[2] + year
        print(date_header)

        #--------------------------------------------------------------------------------
        #
        # The mcdelta date format, add an item, mcdelta-date, to the reference file.
        # https://stackoverflow.com/questions/21035762/python-read-json-file-and-modify
        #
        # Write the date_header, the column name for this info, into the file.
        # with open(pnn) as f:
        # with open(last_file) as f:
        print("---->",dir_and_file)
        with open(dir_and_file) as f:
            data = json.load(f)
            data["mcdelta-date"] = date_header
            json.dump(data, open(dir_and_file, "w"))
            f.close()

        #--------------------------------------------------------------------------------
        # open mcdelta_11.json
        #
        crypto_market_data = data
        print("mcdelta-date ", crypto_market_data["mcdelta-date"])
        mcdelta_date = crypto_market_data["mcdelta-date"]
        print("             ", mcdelta_date)

        if type(mcdelta_obj["mcdelta"]) == type(list()):

            mcdelta_length = len(mcdelta_obj["mcdelta"])
            print("mcdelta_length", mcdelta_length)
            date_list = mcdelta_obj["mcdelta"][0]["dates"]
            print("date_list ",type(date_list))

            # add column, start with date
            if type(date_list) == type(list()):

                print(date_list)
                date_list_len = len(date_list)
                print("date list len ", date_list_len)

                if date_list_len == 0:

                    mcdelta_obj["mcdelta"][0]["dates"].append(mcdelta_date)

                    with open(mcdelta_json_dev_file, 'w') as json_file:
                        json.dump(mcdelta_obj, json_file)

                    try:
                        date_string = mcdelta_obj["mcdelta"][0]["dates"][date_list_len - 1]
                        print(date_string)
                        print("date list len "+str(date_list_len)+" => "+date_string)
                    except:
                        print("ERROR printing last date")

                    # 
                    # the date index will be used to insert ...
                    # actaully insert is wrong ... date will be appended
                    # 
                    # looping through crypto_market_data
                    # print index and crypto str
                    #
                    # print(type(data["coins"]))
                    ''''''
                    number_of_coins = len(crypto_market_data["coins"])
                    print(number_of_coins)
                    for s in range(0,number_of_coins):
                        symbol = data["coins"][s]["symbol"]
                        rank = data["coins"][s]["rank"]
                        #print("  "+str(s)+"   "+str(rank)+" "+symbol)
                        sym_len = len(symbol)
                        if sym_len > 5:
                            mcdelta_obj["mcdelta"][rank][str(rank)].append("???")
                        else:
                            mcdelta_obj["mcdelta"][rank][str(rank)].append(symbol)
                    ''''''
                else: # there's at least one column of data
                    # 
                    # the date index will be used to insert ...
                    # actaully insert is wrong ... date will be appended
                    # 
                    # looping through crypto_market_data
                    # print index and crypto str
                    #
                    # print(type(data["coins"]))
                    # loop through dates row
                    print(">>>>>>  loop through dates row")
                    add_column_data = False
                    for d in range(0,date_list_len):
                        print(date_list[d], "  new date ", date_header)
                        if date_list[d] == date_header:
                            print("date in header row, DO NOT add")
                            add_column_data = False
                        else:
                            print("date does not exist, but is this the latest data")
                            add_column_data = True
                    print("add_column_data ",add_column_data)

                    if add_column_data:
                        print("date not in last, presumed latest, append data")
                        print("mcdelta_obj[mcdelta][0][dates].append(__mcdelta_date__)")
                        print("   date to append is ", date_header)
                        print("mcdelta_obj[mcdelta][0][dates].append( date_header )")
                        mcdelta_obj["mcdelta"][0]["dates"].append(date_header)

                        number_of_coins = len(crypto_market_data["coins"])
                        print("number_of_coins  ",number_of_coins)
                        for s in range(0,number_of_coins):
                            symbol = data["coins"][s]["symbol"]
                            rank = data["coins"][s]["rank"]
                            sym_len = len(symbol)
                            print("  "+str(s)+"   "+str(rank)+" "+symbol+"  sym_len "+str(sym_len))
                            if sym_len > 5:
                                mcdelta_obj["mcdelta"][rank][str(rank)].append("???")
                                print("sym_len > 5 append")
                            else:
                                mcdelta_obj["mcdelta"][rank][str(rank)].append(symbol)
                                print("sym_len WHATEVER append -- why!!!")

                        print("----> post for s in range(0,number_of_coins):")

                    print("RIGHT NOW A 3rd COLUMN BETTER NOT APPEAR")
                    print("NOW COMPARE THE LAST TWO COLUMNS")
                    print("ADD COLOR TO THE CHANGES - if any exist")


            with open(mcdelta_json_dev_file) as f:
                try:
                    json.dump(mcdelta_obj, open(mcdelta_json_dev_file, "w"))
                except:
                    print("ERROR writing mcdelta_obj after added ")