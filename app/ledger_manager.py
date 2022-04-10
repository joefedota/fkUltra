import json

class Ledger():
    #this class is meant as a placeholder to be configured for the type of
    #ledger to be used and to expose an interface for creating/managing DIDs
    dids = {}
    count = 0
    def __init__(self, dids, count):
        #dids dictionary and current count will be passed in from a file
        #loaded on boot
        self.dids = dids
        self.count = count

    def get_protected_datastore(self, did):
        return dids[did]["services"]["serviceEndpoint"]

    def register_did(self):
        self.count += 1
        self.dids[self.count] = {"services": {"serviceEndpoint": str(self.count) + ".json"}}

        #write a commit of new did dictionary to file
        f = open("ledger.json", "w")
        dump = {"data": {"dids": self.dids, "count": self.count}}
        json_serialized = json.dumps(dump)
        f.write(json_serialized)
        f.close()

        return self.count
        