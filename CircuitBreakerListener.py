#==================================================================================
#Author        : Gopi 
#File Info     : Log Config if any
#Created Date  : 08-02-2020
#----------------------------------------------------------------------------------
#-- Change Log --
#==================================================================================
#-----------------------------------Begin Import-----------------------------------

import pybreaker
#---------------------------------End Of Import------------------------------------


#Circuit breaker Listener and logging
class LogListener(pybreaker.CircuitBreakerListener):
    """ Listener used to log circuit breaker events. """

    def __init__(self, app):
        self.app = app

    def state_change(self, cb, old_state, new_state):
        "Called when the circuit breaker `cb` state changes."
        self.app.logger.error('circuit breaker state change: %r => %r',
                              old_state.name, new_state.name)
        print("**************catched********************")

    def failure(self, cb, exc):
        """ This callback function is called when a function called by the
        circuit breaker `cb` fails.

        """
        self.app.logger.error('failure: %r, count: %r', exc, cb.fail_counter)
        print("**************failed********************")
