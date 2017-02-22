class MyCookieProcessingMiddleware(object):
	def process_request(self, request):
		if request.COOKIE.get('X-Powered-By',False):
			pass
		else:
			request.COOKIE['X-Powered-By'] = 'ASP.NET'

