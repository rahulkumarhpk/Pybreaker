from flask import Flask,render_template,request,Response,json
from flask_restplus import Api, Resource, fields
from flask_cors import CORS
from Server import server
from flask_restplus import Namespace, Resource, fields,Api
import LogListener

app, api = server.app, server.api


serviceNameAPI = Namespace('servicename', description='get servicename information')



@serviceNameAPI.route('/circuitBreaker')
@serviceNameAPI.produces('application/xml')
class checkCircuitBreaker(Resource):
    def get(self):
        try:
            return circuit_breaker_demo(), 200
        except (pybreaker.CircuitBreakerError):
            return "Service unavailable", 503
    


@serviceNameAPI.route('/circuitBreaker/1')
@serviceNameAPI.produces('application/xml')
class checkCircuitBreaker_1(Resource):
    def get(self):
        try:
            return circuit_breaker_demo_1(), 200
        except (pybreaker.CircuitBreakerError):
            return "Service unavailable", 503

time_breaker = pybreaker.CircuitBreaker(fail_max=3, reset_timeout=3.0)
time_breaker.add_listeners(LogListener(app))

#------------------------Called Functions---------------------------

@time_breaker
@retry(stop_max_attempt_number=3)
def circuit_breaker_demo():
    
    try:
        resp = requests.get('https://taspre-phx-mtls.apps.com/api/dataservice/measurements',timeout=3.0)
       
    except (requests.exceptions.ConnectionError,
        requests.exceptions.Timeout):              
        raise pybreaker.CircuitBreakerError
    print(time_breaker.current_state)        
    return json.loads(resp.text)

@time_breaker
@retry(stop_max_attempt_number=2)
def circuit_breaker_demo_1():
    try:
        resp = requests.get('https://taspre-phx-mtls.apps.com/api/measurements?ids=4401007',timeout=3.0)
    except (requests.exceptions.ConnectionError,
        requests.exceptions.Timeout):              
        raise pybreaker.CircuitBreakerError
    
    return json.loads(resp.text)
