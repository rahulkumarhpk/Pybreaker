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

#method used to search a measurement based on measurement id.
@serviceNameAPI.route('/method')
class SampleController(Resource): 
    # @token_required
    # @cache.cached(timeout=1000)   
    def get(self):
        return  delegate_function(), 200


@serviceNameAPI.route('/method1')
class five_o__fiveController(Resource): 
    # @token_required
    # @cache.cached(timeout=1000)
    def get(self):
        return  '',500


@serviceNameAPI.route('/method2')
class fouroo_Controller(Resource): 
    # @token_required
    # @cache.cached(timeout=1000)
    def get(self):
        return  '',400



@serviceNameAPI.route('/method3')
class fouroone_Controller(Resource): 
    # @token_required
    # @cache.cached(timeout=1000)
    def get(self):
        return  '',401


@serviceNameAPI.route('/method4')
class fourothree_Controller(Resource): 
    # @token_required
    # @cache.cached(timeout=1000)
    def get(self):
        return  '',403
