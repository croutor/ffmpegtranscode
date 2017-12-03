# coding: utf8
import json
import pprint
#import pymongo

# Could be retrieve, but for now, F... it
channelOrder = {
              'TF1'           :  1,
              'France 2'      :  2,
              'France 3'      :  3,
              'Canal+'        :  4,
              'France 5'      :  5,
              'M6'            :  6,
              'Arte'          :  7,
              'C8'            :  8,
              'W9'            :  9,
              'TMC'           : 10,
              'NT1'           : 11,
              'NRJ 12'        : 12,
              'LCP'           : 13,
              'France 4'      : 14,
              'BFM TV'        : 15,
              'CNEWS'         : 16,
              'CStar'         : 17,
              'Gulli'         : 18,
              'France Ô'      : 19,
              'HD1'           : 20,
              'L\'équipe 21'  : 21,
              '6ter'          : 22,
              'Numéro 23'     : 23,
              'RMC Découverte': 24,
              'Chérie 25'     : 25
         }
protocol = 'udp'
port = '8200'
imagePath = 'image/channels'

ChannelsLogo = {
              'TF1'           :  'TF1.png',
              'France 2'      :  'France2.png',
              'France 3'      :  'France3.png',
              'Canal+'        :  'Canal+.png',
              'France 5'      :  'France5.png',
              'M6'            :  'M6.png',
              'Arte'          :  'Arte.png',
              'C8'            :  'C8.png',
              'W9'            :  'W9.png',
              'TMC'           :  'TMC.png',
              'NT1'           :  'NT1.png',
              'NRJ 12'        :  'NRJ12.png',
              'LCP'           :  'LCP.png',
              'France 4'      :  'France4.png',
              'BFM TV'        :  'BFM_TV.png',
              'CNEWS'         :  'CNEWS.png',
              'CStar'         :  'CStar.png',
              'Gulli'         :  'Gulli.png',
              'France Ô'      :  'FranceÔ.png',
              'HD1'           :  'HD1.png',
              'L\'équipe 21'  : 'L\'équipe 21.png',
              '6ter'          : '6ter',
              'Numéro 23'     : 'Numéro23.png',
              'RMC Découverte': 'RMCDécouverte.png',
              'Chérie 25'     : 'Chérie25.png'
         }
         
def channelListWithIP(log_fh):
    currentDict = {}
    for line in log_fh:
        if "Channel" in line:
			# line containing the channel name:
            channel = line.split(':')[1].strip().rstrip('"').strip('"')
            # line containing the IP address:
            IP = log_fh.next().split(':')[1].strip()
            print( channel, IP)
            currentDict[channel] = IP
    return currentDict

def main():
    channelList = {}
    channelData = []
    pp = pprint.PrettyPrinter(indent=4)
    with open("channels_streamed_adaptor0_tuner0") as f:
        channelList = channelListWithIP(f)
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

