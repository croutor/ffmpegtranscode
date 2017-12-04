# coding: utf8
import json
import os
import pprint
#import pymongo

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
protocol = 'udp'
port = '8200'
imagePath = 'image/channels'
mumuConfDir = '/var/run/mumudvb/'

ChannelsLogo = {
              'TF1'           :  'TF1.png',
              'France 2'      :  'France2.png',
              'France 3'      :  'France3.png',
              'CANAL+'        :  'Canal+.png',
              'France 5'      :  'France5.png',
              'M6'            :  'M6.png',
              'Arte'          :  'Arte.png',
              'C8'            :  'C8.png',
              'W9'            :  'W9.png',
              'TMC'           :  'TMC.png',
              'NT1'           :  'NT1.png',
              'NRJ12'         :  'NRJ12.png',
              'LCP'           :  'LCP.png',
              'France 4'      :  'France4.png',
              'BFM TV'        :  'BFM_TV.png',
              'CNEWS'         :  'CNEWS.png',
              'CSTAR'         :  'CStar.png',
              'Gulli'         :  'Gulli.png',
              'France Ô'      :  'FranceÔ.png',
              'HD1'           :  'HD1.png',
              'L\'Equipe 21'  : 'L\'Equipe 21.png',
              '6ter'          : '6ter',
              'NUMERO 23'     : 'Numéro23.png',
              'RMC Découverte': 'RMCDécouverte.png',
              'Chérie 25'     : 'Chérie25.png',
              'LCI'           : 'LCI.png',
              'franceinfo'    : 'franceinfo.png',
              'F3 Bretagne'   : 'France3Breatagne.png',
              'TVR'           : 'TVR.png',
              'PARIS PREMIERE': 'Paris_Premiere.png',
              'CANAL+ SPORT'  : 'Canal+sport.png'
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

def main():
    pp = pprint.PrettyPrinter(indent=4)
    channelData = []
    channelList = channelListWithIP()
    print channelList
    for channelName, IP in channelList.iteritems():
		channel = {
		'name' : channelName,
		'address': protocol + IP + port,
		'image' : {
			'path' : imagePath,
			'logo' : ChannelsLogo[channelName]
		},
		'order' : channelOrder[channelName]
		}
		
		channelData.append(channel)
    #print channelData
    jChannelData = json.dumps(channelData)
    pp.pprint(jChannelData)

if __name__ == "__main__":
    main()
