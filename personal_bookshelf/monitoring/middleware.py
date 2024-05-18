import logging
from rest_framework.status import is_success

class BookshelfMonitoringMiddleware:


    def __init__(self,get_response):
        self.get_response= get_response
        self.logger = logging.getLogger()
        



    def __call__(self,request):

        try:
            self.process_request(request)
            response = self.get_response(request)
            response = self.process_request(request,response)
            if is_success(response.status_code):
                self._log_succesful_request(request.response)
            return response

        except Exception as exc:
            self.logger.error(exc)
            return self.get_response(request)



    def process_request(self,request,response):
        self._log_message(
            f"[proces_request]=> request:{request}"
        )



    def process_response(self,request,response):
        self._log_message(
            f"[proces_response]=>response:{response}"
        )
        return response


    def _log_message(self,message):
        self.logger.info(
            f'[{self.__class__.__name__}.Monitoring{message} ]'
        )


    def _log_succesful_message(self,request,response):
        self.logger.info(
            f"[{self.__class__.__name__}.MonitoringMiddleware][succesful_request]=>"
            f"{request.method} {request.path} - {response.status_code}"
        )