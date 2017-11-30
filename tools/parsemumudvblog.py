
def generateDicts(log_fh):
    currentDict = {}
    for line in log_fh:
        if "Channel" in line:
            print line
    yield currentDict

def main():
    ChannelList = []
    with open("mumudvb_card0.log") as f:
        channelList = list(generateDicts(f))
    print ChannelList

if __name__ == "__main__":
    main()

