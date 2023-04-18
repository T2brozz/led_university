import threading
import time

import uvicorn

import api
import mensa
import public_transport


def api_start():
    uvicorn.run('api:app', host='0.0.0.0', port=8080, debug=False)


def crawl_data():
    c = 0
    try:
        public_transport.start()
        mensa.start()
    except:
        pass

    while True:
        c += 1
        if c % 5 == 0:
            try:
                public_transport.start()
            except:
                pass
        if c >= 60:
            try:
                mensa.start()
            except:
                pass
            c = 0
        time.sleep(60)


def start_everything():
    thread1 = threading.Thread(target=api_start, name="api")
    thread2 = threading.Thread(target=crawl_data, name="data crawler")
    thread1.start()
    thread2.start()
