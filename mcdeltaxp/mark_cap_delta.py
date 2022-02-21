from operator import truediv
import requests
import json
import datetime
from datetime import date
import os
from operator import itemgetter
import sys

cdata_site = "https://api.coinstats.app/public/v1/coins?skip=0&limit=1000000"

class MCDelta():

    def get_raw_coinstats_on_run():
        pass
        try:
            os.chdir('../mcdeltaxp/00-raw-dev-data')
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
        

    '''    
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
    '''
    '''
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


        def walk_through_cell_attribute_list(data,f):
            for x in data:
                if x["delta"] == "+1":
                    f.write("<td style=\"background-color:#a8d08d; text-align:center;\">")
                elif x["delta"] == "-1":
                    f.write("<td style=\"background-color:#e99d9b; text-align:center;\">")

        def parse_cell_item(data,f):
            for key,value in data.items():
                cellString = key
                if type(value) == type(list()):
                    walk_through_cell_attribute_list(value,f)
                f.write(cellString)
                f.write("</td>")


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
    '''


    def write_mcdelta_html_from_11json_data():
        print("- 11json work")
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

        #dev11_html_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/mcdelta/dev11.html"
        #dev11_html_file = "/home/dlt05/git-work/git-mcdelta/mcdeltaxp/mcdelta/dev11.html"
        dev11_html_file = "/home/dlt05/git-work/git-mcdelta/mcdeltaxp/mcdeltaxp/mcdelta/dev11.html"

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
        
        #mcdelta_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_11.json"
        mcdelta_json_dev_file = "/home/dlt05/git-work/git-mcdelta/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_11.json"
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
        f.write("  <br/>")
        f.write("  Feb 18<br/>")
        f.write("  HBAR, https://hedera.com/, <br/>")
        f.write("          O'Leary pic<br/>")
        f.write("          The Hedera proof-of-stake public network, powered by hashgraph consensus, <br/>")
        f.write("          achieves the highest-grade of security possible (ABFT), with blazing-fast <br/>")
        f.write("          transaction speeds and incredibly low bandwidth consumption. By combining <br/>")
        f.write("          high-throughput, low fees, and finality in seconds, Hedera leads the way <br/>")
        f.write("          for the future of public ledgers.<br/>")
        f.write("  <br/>")
        f.write("  <pre>")
        f.write("  Feb 16<br/>")
        f.write("  OCEAN, https://oceanprotocol.com/, unlocks the value of data.<br/>")
        f.write("         Data owners and consumers use Ocean Market app to publish, discover,<br/>")
        f.write("         and consume data in a secure, privacy-preserving fashion. <br/>")
        f.write("         OCEAN holders stake liquidity to data pools.<br/>")
        f.write("  <br/>")
        f.write("  Feb 15<br/>")
        f.write("  <br/>")
        f.write("  FOAM, https://www.foam.space/, provides the tools to enable a crowdsourced map and decentralized location services.<br/>")
        f.write("        wallets; brave, chrome, opera or metamask<br/>")
        f.write("        https://www.foam.space/map<br/>")
        f.write("  AQUA, https://aqua.network/, adds liquidity management layer to Stellar and powers new generation of DeFi projects.<br/>")
        f.write("        https://lobstr.co/, https://www.stellarx.com/, https://stellarterm.com/<br/>")
        f.write("  PUSH, https://epns.io/, blockchain based notifications that are chain agnostic, platform independent and incentivized.<br/>")
        f.write("        https://app.epns.io/, connect with metamask, portis or wallet connect<br/>")
        f.write("  <br/>")
        f.write("  LUNA, https://www.terra.money/, able to host a multitude of algorithmic stablecoins on its network.<br/>")
        f.write("  GNY, https://www.gny.io/, The world's first decentralised machine learning platform.<br/>")
        f.write("  Feb 11<br/>")
        f.write("  PGIRL (1995,0212) -- first attractive NFT<br/>")
        f.write("  <br/>")
        f.write("  other interesting $#!^ coins<br/>")
        f.write("    FLOW (57,0212), on cro, dapperlabs invested says 500+ dev, 100+ known projects and <br/>")
        f.write("                            Dapps; games, NTFs, Defi, tools at ~7.30 <br/>")
        f.write("    STX (70,0212), on CRO, stacks.co, stacking, a new way to earn bitcoin.<br/>")
        f.write("                   Hold and temporarily lock STX, Stacks’ native currency, and <br/>")
        f.write("                   support the network’s security and consensus. As a reward, you’ll earn BTC.<br/>")
        f.write("                   wallets; Hiro, Xverse, D'cent, Boom, Cerebro, Neptune, <br/>")
        f.write("    Purchased 1000 SLP, on CRO, at about 0.028.<br/>")
        f.write("    Purchased 1000 IDEX, on CRO, at about 0.1781.<br/>")
        f.write("        IDEX is the first Hybrid Liquidity DEX,<br/>")
        f.write("        combining a high-performance order book and<br/>")
        f.write("        matching engine with Automated Market Making (AMM). <br/>")
        f.write("        https://docs.idex.io/<br/>")
        f.write("  <br/>")
        f.write("  https://stack.money/ connected to this brave wallet. No idea what this means<br/>")
        f.write("  but first Web3 app engagement.<br/>")
        f.write("  <br/>")
        f.write("  ROSE (oasisprotocol.org)<br/>")
        f.write("  upland.me<br/>")
        f.write("  <br/>")
        f.write("  OLeary list<br/>")
        f.write("        SOL<br/>")
        f.write("        MATIC<br/>")
        f.write("        HBAR<br/>")
        f.write("  <br/>")
        f.write("  Up when everthing else goes down<br/>")
        f.write("        INJ0<br/>")
        f.write("  <br/>")
        f.write("  <br/>")
        f.write("  Late Feb 10, 2022, into early Feb 11, 2002, CoinGecko broadcast corrupted data<br/>")
        f.write("  and bitcoin and other top coins dropped from the top and unkowns bubbled to the top.<br/>")
        f.write("  <br/>")
        f.write("  WAVES, on CRO, wscan.io, waves blockchain explorer. <br/>")
        f.write("  </pre>")
        f.write("  <br/>")
        f.write("</html>")
        f.close()

    '''
    def update_mcdelta_0x_from_raw_data():
        print("- update_mcdelta_0x_from_raw_data()")
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

        with open(mcdelta_json_dev_file, 'w') as json_file:
            json.dump(mcdelta_obj, json_file)
    '''

    def generate_from_scratch_mcdelta_11json_file():
        print("- generate_from_scratch_mcdelta_11json_file()")
        #---------------------------------------------------------------------------------
        #
        # If mcdelta_11.json does not exist then
        # create the file and update it with the root, json dict(ionary) object, mcdelta
        # 

        #mcdelta_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_11.json"
        mcdelta_json_dev_file = "/home/dlt05/git-work/git-mcdelta/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_11.json"
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
        referenceDir = '/home/dlt05/git-work/git-mcdelta/mcdeltaxp/mcdeltaxp/01-reference-data'
        #for file in sorted(os.listdir('/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/01-reference-data')):
        for file in sorted(os.listdir(referenceDir)):
            print(">> ",file)
            last_file = file

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
        # Write, dump, the file
        #
        with open(mcdelta_json_dev_file, 'w') as json_file:
            json.dump(mcdelta_obj, json_file)

    def update_mcdelta_11json_file():
        print("- update_mcdelta_11json_file")
        #---------------------------------------------------------------------------------
        # If mcdelta_11.json does not exist then 
        # ( what a pain, python can't call in methods in the class/file
        #   create the file and update it with the root, json dict(ionary ) object, mcdelta
        # the create did not work
        #mcdelta_json_dev_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_11.json"
        mcdelta_json_dev_file = "/home/dlt05/git-work/git-mcdelta/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_11.json"
        mcdelta_obj = {}
        try:
            with open(mcdelta_json_dev_file) as fp:
                mcdelta_obj = json.load(fp)
            fp.close()
        except FileNotFoundError:
            print("FileNotFoundError 01 in update_mcdelta_11json_file")
        except:
            print("ERROR 01 in update_mcdelta_11json_file")

        #--------------------------------------------------------------------------------
        # Pull out market data from the newest reference file  
        #
        last_file = ""
        referenceDir = '/home/dlt05/git-work/git-mcdelta/mcdeltaxp/mcdeltaxp/01-reference-data'
        #for file in sorted(os.listdir('/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/01-reference-data')):
        for file in sorted(os.listdir(referenceDir)):
            last_file = file

        #dir_and_file = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/01-reference-data/"+last_file
        #dir_and_file = referenceDir+"/"+last_file
        dir_and_file = "/home/dlt05/git-work/git-mcdelta/mcdeltaxp/mcdeltaxp/01-reference-data/"+last_file
        f = open(dir_and_file)
        crypto_market_data = json.load(f)
        f.close()

        #--------------------------------------------------------------------------------
        # The mcdelta date format
        #
        left_str = last_file.split(".")
        date_object = date.fromtimestamp(int(left_str[0]))
        time_object = date.fromtimestamp(int(left_str[1]))

        date_str = str(date_object)
        date_split = date_str.split('-')

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

        date_header = month + date_split[2] + year

        #--------------------------------------------------------------------------------
        # The mcdelta date format, add an item, mcdelta-date, to the reference file.
        # https://stackoverflow.com/questions/21035762/python-read-json-file-and-modify
        # Write the date_header, the column name for this info, into the file.
        # with open(last_file) as f:
        # print("---->",dir_and_file)
        with open(dir_and_file) as f:
            data = json.load(f)
            data["mcdelta-date"] = date_header
            json.dump(data, open(dir_and_file, "w"))
            f.close()

        #--------------------------------------------------------------------------------
        # open mcdelta_11.json
        #
        crypto_market_data = data
        mcdelta_date = crypto_market_data["mcdelta-date"]

        if type(mcdelta_obj["mcdelta"]) == type(list()):

            mcdelta_length = len(mcdelta_obj["mcdelta"])
            date_list = mcdelta_obj["mcdelta"][0]["dates"]

            # add column, start with date
            if type(date_list) == type(list()):

                date_list_len = len(date_list)

                if date_list_len == 0:

                    mcdelta_obj["mcdelta"][0]["dates"].append(mcdelta_date)

                    with open(mcdelta_json_dev_file, 'w') as json_file:
                        json.dump(mcdelta_obj, json_file)

                    try:
                        date_string = mcdelta_obj["mcdelta"][0]["dates"][date_list_len - 1]
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
                    add_column_data = False
                    for d in range(0,date_list_len):
                        if date_list[d] == date_header:
                            add_column_data = False
                        else:
                            add_column_data = True

                    if add_column_data:
                        mcdelta_obj["mcdelta"][0]["dates"].append(date_header)

                        number_of_coins = len(crypto_market_data["coins"])
                        print("number_of_coins  ",number_of_coins)
                        for s in range(0,number_of_coins):
                            symbol = data["coins"][s]["symbol"]
                            rank = data["coins"][s]["rank"]
                            sym_len = len(symbol)
                            if sym_len > 5:
                                mcdelta_obj["mcdelta"][rank][str(rank)].append("???")
                            else:
                                mcdelta_obj["mcdelta"][rank][str(rank)].append(symbol)

                        print("----> post for s in range(0,number_of_coins):")

            with open(mcdelta_json_dev_file) as f:
                try:
                    json.dump(mcdelta_obj, open(mcdelta_json_dev_file, "w"))
                except:
                    print("ERROR writing mcdelta_obj after added ")

        print("- update_mcdelta_11json_file")

    def market_cap_delta_scan_and_display_markups():
        print("- market_cap_delta_scan_and_display_markups()")
        #---------------------------------------------------------------------------------
        # If mcdelta_11.json does not exist then 
        # ( what a pain, python can't call in methods in the class/file
        #
        # create the file and update it with the root, json dict(ionary) object, mcdelta
        # the create did not work
        # 
        
        mcdelta_json_dev_file = "/home/dlt05/git-work/git-mcdelta/mcdeltaxp/mcdeltaxp/02-mcdelta-json/mcdelta_11.json"
        delta_json = open(mcdelta_json_dev_file)
        data = json.load(delta_json)
        delta_json.close()
        mcdelta_list = data["mcdelta"]

        #----------------------------------------------------------------------
        # 
        # find the delta
        #
        def find_the_delta(rank, coin):
            try:
                # print("find the delta for ", rank, coin)
                #--------------------------------------------------------------
                # This algorythmn finds the coin's last rank by looking first 
                # one row up, and then one row down and expanding outwards,
                # one row at a time.
                #
                looking = True
                delta_rank = -1
                upper_rank = rank
                lower_rank = rank
                in_upper_range_limit = True
                in_lower_range_limit = True
                while looking:
                    mc_rank_set = mcdelta_list[rank]
                    mc = "not set"

                    #----------------------------------------------------------
                    # redandant, isn't that the coin passed into this method
                    reference_coin = coin
                    #print("reference_coin type ",type(reference_coin))

                    #----------------------------------------------------------
                    # look UP one and back one column
                    if upper_rank == 1:
                        in_upper_range_limit = False
                    else:
                        upper_rank -= 1

                    mc_rank_set = mcdelta_list[upper_rank]

                    for j in mc_rank_set.keys():
                        mc = mc_rank_set[j]

                    column2_check_coin = "not set"
                    if isinstance(mc[mc_len-2],dict):
                        #print("mc[mc_len-2] type ",type(mc[mc_len-2]))
                        for k in mc[mc_len-2].keys():
                            column2_check_coin = k
                        #print("coin ", column2_check_coin)

                    if isinstance(mc[mc_len-2],str):
                        column2_check_coin = mc[mc_len-2]

                    #if (mc[mc_len-2] == reference_coin) & looking & in_upper_range_limit:
                    if (column2_check_coin == reference_coin) & looking & in_upper_range_limit:
                        local_upper = upper_rank
                        delta_rank = local_upper
                        looking = False

                    #----------------------------------------------------------
                    # look DOWN one row and back one column
                    if lower_rank == 2000:
                        in_lower_range_limit = False
                    else:
                        lower_rank += 1

                    mc_rank_set = mcdelta_list[lower_rank]
                    for j in mc_rank_set.keys():
                        mc = mc_rank_set[j]

                    '''
                    coin = "not set"
                    if isinstance(mc[mc_len-2],dict):
                        print("mc[mc_len-2] type ",type(mc[mc_len-2]))
                        for k in mc[mc_len-2].keys():
                            coin = k
                        print("coin ", coin)

                    if isinstance(mc[mc_len-2],str):
                        coin = mc[mc_len-2]
                    '''
                    column2_check_coin = "not set"
                    if isinstance(mc[mc_len-2],dict):
                        for k in mc[mc_len-2].keys():
                            column2_check_coin = k

                    if isinstance(mc[mc_len-2],str):
                        column2_check_coin = mc[mc_len-2]

                    if (column2_check_coin == reference_coin) & looking & in_lower_range_limit:
                        local_lower = lower_rank
                        delta_rank = local_lower
                        looking = False

                    if in_lower_range_limit == False & in_upper_range_limit == False:
                        looking = False

                if delta_rank > rank: # a delta_rank greater than rank then set coin to green
                    del(data["mcdelta"][rank][str(rank)][mc_len-1])
                    data["mcdelta"][rank][str(rank)].append({coin:[{"delta":"+1","var1":"tbd","var":"tbd"}]})

                elif delta_rank < rank: # set coin to red
                    del(data["mcdelta"][rank][str(rank)][mc_len-1])
                    data["mcdelta"][rank][str(rank)].append({coin:[{"delta":"-1","var1":"tbd","var":"tbd"}]})
                    #print("finding the cell ",data["mcdelta"][rank][str(rank)][mc_len-1])

                elif delta_rank == rank:
                    print("delta_rank == rank, ",rank)
                    print("the coin was not found in previous column")

            except IndexError as ie:
                print("upper rank = ", upper_rank, "; lower rank = ", lower_rank)
                print(ie)

    
        #---------------------------------------------------------------------------------
        #
        # run through last column, if the last column cell does not match then
        # call find_the_delta which locates the coin in the previous column
        # if it was a higher market cap then set the cell to red
        # if it was a lower market cap then set the cell to green
        #
        mcdelta_list_len = len(mcdelta_list)
        mc_rank = "not set"
        #for mc_rank in range(1,mcdelta_list_len):
        for mc_rank in range(1,2000):
            mc_set = mcdelta_list[mc_rank]

            mc = "not set"
            for j in mc_set.keys():
                mc = mc_set[j]

            mc_len = len(mc)

            column2_check_coin = "not set"
            if isinstance(mc[mc_len-2],dict):
                for k in mc[mc_len-2].keys():
                    column2_check_coin = k
            if isinstance(mc[mc_len-2],str):
                column2_check_coin = mc[mc_len-2]

            if (column2_check_coin != mc[mc_len-1]) & (type(mc[mc_len-1]) != dict) & (mc[mc_len-1] != "???"):
                find_the_delta(mc_rank, mc[mc_len-1])

        with open(mcdelta_json_dev_file) as f:
            try:
                json.dump(data, open(mcdelta_json_dev_file, "w"))
                f.close()
            except:
                print("ERROR writing mcdelta_obj after added ")

    def list_file_dates():
        #data_dir = "/home/dlt03/gitprojects/mcdeltaxp/mcdeltaxp/00-raw-dev-data"
        data_dir = "/home/dlt05/git-work/git-mcdelta/mcdeltaxp/mcdeltaxp/00-raw-dev-data"
        os.chdir(data_dir)
        listOfFiles = os.listdir('.')
        for entry in listOfFiles:
            print("Date = ", date.fromtimestamp(float(entry)),", File Name = ", entry)
            