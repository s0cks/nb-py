import socket
from threading import Thread
from Queue import Queue


class Sign(object):
    def __init__(self, name, address, port):
        self.name = name
        self.address = address
        self.port = port
        self.worker = Thread(target=self._connect)
        self.queue = Queue()
        self.zones = {}

    def get_zone_by_id(self, zid):
        return self.zones[zid]

    def get_zone_by_name(self, name):
        for zone in self.zones:
            if zone.name is name:
                return zone
        return None

    def send(self, event):
        self.queue.put(event)

    def _connect(self):
        #self.client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        #self.client.connect((self.address, self.port))
        while True:
            work = self.queue.get()
            print "Work:", work
            self.queue.task_done()
        #self.client.close()

    def connect(self):
        self.worker.setName("SymonNetBrite-Sign-%s" % self.name)
        self.worker.setDaemon(True)
        self.worker.start()

    def disconnect(self, timeout=None):
        self.worker.join(timeout)
        self.queue.join()
