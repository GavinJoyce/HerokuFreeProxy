class MyMiddleware(object):
    def process_response(self, request, response):
        response['X-Frame-Options'] = "allow-from https://some.domain.com/"
        response['Access-Control-Allow-Origin'] = "*"
        del response['Content-Security-Policy']
        return response
