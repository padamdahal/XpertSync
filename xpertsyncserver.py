#!/usr/bin/python
import logging
from astm.asynclib import loop
from astm.server import Server, BaseRecordsDispatcher

# global astm logging channel configuration
log_root = logging.getLogger('astm')
handler = logging.StreamHandler()
handler = logging.FileHandler('/home/ntc/astm-server.log')
handler.setFormatter(logging.Formatter(
    '[%(asctime)s] [%(name)s] [%(levelname)s] %(message)s'
))
log_root.addHandler(handler)
log_root.setLevel(logging.DEBUG)

# special logging configuration for server connection handler
log_conn = logging.getLogger('astm.server.conn')
handler = logging.StreamHandler()
handler = logging.FileHandler('/home/ntc/astm.log')

handler.setFormatter(logging.Formatter(
    '[%(asctime)s] [%(name)s] [%(levelname)s] [%(host)s:%(port)s] %(message)s'
))
log_conn.addHandler(handler)
log_conn.setLevel(logging.DEBUG)
log_conn.propagate = False


class RecordsDispatcher(BaseRecordsDispatcher):
    log = logging.getLogger('astm.server.dispatcher')

    def on_header(self, record):
        self.log.info('Header: %r', record)

    def on_patient(self, record):
        self.log.info('Patient: %r', record)

    def on_order(self, record):
        self.log.info('Order: %r', record)

    def on_result(self, record):
        self.log.info('Result: %r', record)

    def on_comment(self, record):
        self.log.info('Comment: %r', record)

    def on_unknown(self, record):
        self.log.warn('Unknown record: %r', record)
        print (record)
    def on_terminator(self, record):
        self.log.info('Terminator: %r', record)


if __name__ == '__main__':
    server = Server('0.0.0.0', 3000, dispatcher=RecordsDispatcher, timeout=10)
    print ("server listening on port 3000")
    loop(timeout=10)
