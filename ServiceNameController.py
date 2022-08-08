from flask import Flask,render_template,request,Response,json
from flask_restplus import Api, Resource, fields
from flask_cors import CORS
from Server import server
from flask_restplus import Namespace, Resource, fields,Api
from Service.Util.util import *
from Service.Deligate.ServiceDeligate import *
from Service.Util.CircuitBreakerListener import LogListener

app, api = server.app, server.api


serviceNameAPI = Namespace('servicename', description='get servicename information')



@serviceNameAPI.route('/circuitBreaker')
@serviceNameAPI.produces('application/xml')
class checkCircuitBreaker(Resource):
    def get(self):
        # response = circuit_breaker_demo(app).decode("utf-8")
        # return Response(response, content_type='text/xml; charset=utf-8') ,200
        
        return circuit_breaker_demo(), 200
    


@serviceNameAPI.route('/circuitBreaker/1')
@serviceNameAPI.produces('application/xml')
class checkCircuitBreaker_1(Resource):
    def get(self):
        # response = circuit_breaker_demo_1().decode("utf-8")
        # return Response(response, content_type='text/xml; charset=utf-8') ,200
        return circuit_breaker_demo_1(), 200

time_breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=3.0)
time_breaker.add_listeners(LogListener(app))

# @time_breaker
# def get_circuit_data(send):
#     try:
#         resp = requests.get(send,timeout=3.0)
#     except (requests.exceptions.ConnectionError,
#         requests.exceptions.Timeout):              
#         raise pybreaker.CircuitBreakerError
#     return json.loads(resp.text)

@time_breaker
@retry(stop_max_attempt_number=3)
def circuit_breaker_demo():
    # send = 'https://daedalusdataservice.taspre-phx-mtls.apps.boeing.com/api/daedalusdataservice/measurements'
    
    try:
        resp = requests.get('https://daedalusdataservice.taspre-phx-mtls.apps.boeing.com/api/daedalusdataservice/measurements',timeout=3.0)
       
    except (requests.exceptions.ConnectionError,
        requests.exceptions.Timeout):              
        raise pybreaker.CircuitBreakerError
    print(time_breaker.current_state)
    # if time_breaker.open:
        
    return json.loads(resp.text)
    # return get_circuit_data(send)

@time_breaker
@retry(stop_max_attempt_number=2)
def circuit_breaker_demo_1():
    # send='https://daedalusdataservice.taspre-phx-mtls.apps.boeing.com/api/daedalusdataservice/measurements/measurements?ids=4401007'
    
    try:
        resp = requests.get('https://daedalusdataservice.taspre-phx-mtls.apps.boeing.com/api/daedalusdataservice/measurements/measurements?ids=4401007',timeout=3.0)
    except (requests.exceptions.ConnectionError,
        requests.exceptions.Timeout):              
        raise pybreaker.CircuitBreakerError
    
    return json.loads(resp.text)
