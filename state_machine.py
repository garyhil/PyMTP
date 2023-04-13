import sys
import time
import enum
import subprocess
from transitions import Machine, State

class MTP_Service(object):
    
    states = [
        State('IDLE', on_enter=['while_idle']),
        State('STARTING', on_enter=['while_starting']),
        State('EXECUTE', on_enter=['while_execute']),
        State('COMPLETING', on_enter=['while_completing']),
        State('COMPLETED', on_enter=['while_completed']),
        State('PAUSING', on_enter=['while_pausing']),
        State('PAUSED', on_enter=['while_paused']),
        State('RESUMING', on_enter=['while_resuming']),
        State('HOLDING', on_enter=['while_holding']),
        State('HELD', on_enter=['while_held']),
        State('UNHOLDING', on_enter=['while_unholding']),
        State('STOPPING', on_enter=['while_stopping']),
        State('STOPPED', on_enter=['while_stopped']),
        State('ABORTING', on_enter=['while_aborting']),
        State('ABORTED', on_enter=['while_aborted']),
        State('RESETTING', on_enter=['while_resetting'])
    ]

    transitions = [ 
        ['start', 'IDLE', 'STARTING'],
        ['restart', 'EXECUTE', 'STARTING'],
        ['sc_execute', ['STARTING', 'UNHOLDING', 'RESUMING'], 'EXECUTE'],
        ['pause', 'EXECUTE', 'PAUSING'],
        ['sc_pasued', 'PAUSING', 'PAUSED'],
        ['resume', 'PAUSED', 'RESUMING'],
        ['hold', ['RESUMING','PAUSED','PAUSING','STARTING','COMPLETING','UNHOLDING','EXECUTE'], 'HOLDING'],
        ['sc_held', 'HOLDING', 'HELD'],
        ['unhold', 'HELD', 'UNHOLDING'],
        ['complete', 'EXECUTE', 'COMPLETING'],
        ['sc_complete', 'EXECUTE', 'COMPLETING'],
        ['sc_completed', 'COMPLETING', 'COMPLETED'],
        ['reset', ['COMPLETED','STOPPED','ABORTED'], 'RESETTING'],
        ['stop', ['RESUMING','PAUSED','PAUSING','IDLE','STARTING','EXECUTE','COMPLETING','UNHOLDING','HELD','HOLDING','COMPLETED','RESETTING'], 'STOPPING'],
        ['sc_stopped', 'STOPPING', 'STOPPED'],
        ['abort', ['RESUMING','PAUSED','PAUSING','IDLE','STARTING','EXECUTE','COMPLETING','UNHOLDING','HELD','HOLDING','COMPLETED','RESETTING','STOPPING','STOPPED'], 'ABORTING'],
        ['sc_aborted', 'ABORTING', 'ABORTED'],
        ['sc_idle', 'RESETTING', 'IDLE']
    ]
    
    def __init__(self,name):
        self.name = name
        self.machine = Machine(model=self, states=self.states, transitions=self.transitions, initial='IDLE', auto_transitions=False)

    # functions describing the State Machines behavior in the specific states
    ### What to do in Idle State
    def while_idle(self):
        print("I am idle")

    ### What to do while Service is starting
    def while_starting(self):
        print("I am starting")
        self.sc_execute()

    ### What to do when Service is executing
    def while_execute(self):
        print("I am executing")
        subprocess.call(['bash', './run.bash'])


    ### What to do while Service is completing
    def while_completing(self):
        print("I am completing")
        self.sc_completed()

    ### What to do when Service is completed
    def while_completed(self):
        print("I am completed")

    ### What to do while Service is pausing
    def while_pausing(self):
        print("I am pausing")
        self.sc_pasued()

    ### What to do when Service is paused
    def while_paused(self):
        print("I am paused") 

    ### What to do while Service is resuming
    def while_resuming(self):
        print("I am resuming")
        self.sc_execute()

    ### What to do while Service is holding
    def while_holding(self):
        print("I am holding")
        self.sc_held()

    ### What to do when Service is held
    def while_held(self):
        print("I am held")

    ### What to do while Service unholding
    def while_unholding(self):
        print("I am unholding")
        self.sc_execute()

    ### What to do while Service is stopping
    def while_stopping(self):
        print("I am stopping") 
        self.sc_stopped()

    ### What to do when Service is stopped
    def while_stopped(self):
        print("I am stopped")  

    ### What to do while Service is aborting
    def while_aborting(self):
        print("I am aborting")
        self.sc_aborted()

    ### What to do when Service is aborted
    def while_aborted(self):
        print("I am aborted")

    ### What to do while Service is resetting
    def while_resetting(self):
        print("I am resetting") 
        self.sc_idle()
    
    def change_state(self, command):
        if command == "start":
            self.start()
        elif command == "restart":
            self.start()
        elif command ==  "complete":
            self.complete()
        elif command ==  "pause":
            self.pause()
        elif command ==  "resume":
            self.resume()
        elif command ==  "hold":
            self.hold()
        elif command ==  "unhold":
            self.unhold()
        elif command ==  "stop":
            self.stop()
        elif command ==  "abort":
            self.abort()
        elif command ==  "reset":
            self.reset()
        else:
            print("Not a valid command!")