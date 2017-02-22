# class MyCookieProcessingMiddleware(object):
#
#     # your desired cookie will be available in every django view
#     def process_request(self, request):
#         # will only add cookie if request does not have it already
#         if not request.META.get('X-Powered-By '):
#             request.META['X-Powered-By '] = 'ASP.NET'
#
#     # your desired cookie will be available in every HttpResponse parser like browser but not in django view
#     def process_response(self, request, response):
#         if not request.META.get('X-Powered-By'):
#             response.META['X-Powered-By '] = 'ASP.NET'
#         return response