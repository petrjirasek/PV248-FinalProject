import urllib2, re
import Queue
import threading

class TitlesThread(threading.Thread):
    def __init__(self, interface):
        threading.Thread.__init__(self)
        self.__active = True
        self.__i = interface
        self.__tasks = Queue.Queue()

	def titles(self, url):
		if url != None:
			self.__tasks.put(url)
			return None
		else:
			self.stop()

    def stop(self):
        self.__active = False

    def run(self):
        while self.__active:
            if not self.__tasks.empty():
				url = self.__tasks.get()

				regex = re.compile('<title>(.*?)</title>', re.IGNORECASE|re.DOTALL)

				try:
					response = urllib2.urlopen(url)
					html = response.read()
					output = regex.search(html).group(1)
				except Exception:
					output = 'error: ' + str(e)

				self.__i.write(output)

