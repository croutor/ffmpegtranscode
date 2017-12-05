# coding: utf8
import json
import os
import pprint
from pymongo import MongoClient

MONGO_URL='10.42.0.10'
MONGO_DB='tv'
MONGO_COLLECTION='channels'

imagePath = '/images/channels'
mumuConfDir = '/var/run/mumudvb/'
protocol = 'udp'
port = '8200'
# Could be retrieve, but for now, F... it
# http://www.csa.fr/Television/Les-chaines-de-television/Les-chaines-hertziennes-terrestres/La-numerotation-des-chaines
channelOrder = {
              'TF1'           :  1,
              'France 2'      :  2,
              'France 3'      :  3,
              'CANAL+'        :  4,
              'France 5'      :  5,
              'M6'            :  6,
              'Arte'          :  7,
              'C8'            :  8,
              'W9'            :  9,
              'TMC'           : 10,
              'NT1'           : 11,
              'NRJ12'         : 12,
              'LCP'           : 13,
              'France 4'      : 14,
              'BFM TV'        : 15,
              'CNEWS'         : 16,
              'CSTAR'         : 17,
              'Gulli'         : 18,
              'France Ô'      : 19,
              'HD1'           : 20,
              'L\'Equipe 21'  : 21,
              '6ter'          : 22,
              'NUMERO 23'     : 23,
              'RMC Découverte': 24,
              'Chérie 25'     : 25,
              'LCI'           : 26,
              'franceinfo'    : 27,
              'F3 Bretagne'   : 30, 
              'TVR'           : 35,
              'PARIS PREMIERE': 41,
              'CANAL+ SPORT'  : 42
         }

ChannelsLogo = {
              'TF1'           : 'TF1.png',
              'France 2'      : 'France2.png',
              'France 3'      : 'France3.png',
              'CANAL+'        : 'Canal.png',
              'France 5'      : 'France5.png',
              'M6'            : 'M6.png',
              'Arte'          : 'Arte.png',
              'C8'            : 'Canal_8.png',
              'W9'            : 'W9.png',
              'TMC'           : 'TMC.png',
              'NT1'           : 'NT1.png',
              'NRJ12'         : 'NRJ12.png',
              'LCP'           : 'LCP.png',
              'France 4'      : 'France4.png',
              'BFM TV'        : 'BFMTV.png',
              'CNEWS'         : 'cnews.png',
              'CSTAR'         : 'CStar.png',
              'Gulli'         : 'gulli.png',
              'France Ô'      : 'FranceO.png',
              'HD1'           : 'hd1.png',
              'L\'Equipe 21'  : 'lequipe21.png',
              '6ter'          : '6ter',
              'NUMERO 23'     : 'numero23.png',
              'RMC Découverte': 'rmcdecouverte.png',
              'Chérie 25'     : 'cherie25.png',
              'LCI'           : 'LCI.png',
              'franceinfo'    : 'FranceInfo.png',
              'F3 Bretagne'   : 'France3.png',
              'TVR'           : 'TVRennes.png',
              'PARIS PREMIERE': 'paris_premiere.png',
              'CANAL+ SPORT'  : 'canal_plus_sport.png'
         }
         
def channelListWithIPOneFile(log_fh):
    currentDict = {}
    for line in log_fh:
        splitList = line.split(':')
        IP = splitList[0]
        port = splitList[1]
        channel = splitList[2]
        currentDict[channel] = IP
    return currentDict

def channelListWithIP():
    currentDict = {}
    for filename in os.listdir(mumuConfDir):
        if filename.startswith('channels_streamed_adapter'):
            with open(mumuConfDir + '/' + filename) as f:
                channelList = channelListWithIPOneFile(f)
                currentDict.update(channelList)
    return currentDict

def updateMongo(channels):
    client = MongoClient('mongodb://' + MONGO_URL + ':27017')
    db = client[MONGO_DB]
    collection = db[MONGO_COLLECTION]
    for channel in channels:
        jChannel = json.dumps(channel)
        print jChannel
        collection.insert(channel)



def main():
    pp = pprint.PrettyPrinter(indent=4)
    channelData = []
    channelList = channelListWithIP()
    print channelList
    for channelName, IP in channelList.iteritems():
		channel = {
		'label' : channelName,
		'logo' : {
			'filepath' : imagePath,
			'filename' : ChannelsLogo[channelName]
		},
                'protocol' : protocol,
                'url': '@' + IP + ':' + port,
		'order' : channelOrder[channelName]
		}
		
		channelData.append(channel)
    #print channelData
    #jChannelData = json.dumps(channelData)
    #print json.dumps(channelData, indent=4, sort_keys=True)
    updateMongo(channelData)

if __name__ == "__main__":
    main()
