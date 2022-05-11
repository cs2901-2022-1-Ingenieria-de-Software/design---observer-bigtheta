
class Publisher():
	def __init__(self):
			self.subscribers = []

	def notify(self, *args, **kwargs):
		for subscriber in self.subscribers:
			subscriber.update(self, *args, **kwargs)

	def subscribe(self, subscriber):
		self.subscribers.append(subscriber)
	
	def unsubscribe(self, subscriber):
		self.subscribers.remove(subscriber)