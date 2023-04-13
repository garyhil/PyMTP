import sys
import time
from opcua import ua, Server
from state_machine import MTP_Service

mtp_service = MTP_Service('robot_service')

if __name__ == "__main__":
    
    # setup our server
    server = Server()
    server.set_endpoint("opc.tcp://localhost:4840")

    # setup our own namespace, not really necessary but should as spec
    uri = "http://mtp-ros.methods"
    idx = server.register_namespace(uri)

    # get Objects node, this is where we should put our nodes
    objects = server.get_objects_node()

    # populating our address space
    sm = objects.add_object(idx, "StateMachine")
    state = sm.add_variable(idx, "State_Current", mtp_service.state)
    command = sm.add_variable(idx, "Command", "")
    command.set_writable()

    server.start()
    
    try:
        while True:
            time.sleep(2)
            new_command = command.get_value()
            print("Available commands are: ")
            for available_command in mtp_service.machine.get_triggers(mtp_service.state):
                print(available_command)
            if new_command in mtp_service.machine.get_triggers(mtp_service.state):
                print("That is a valid command!")
                mtp_service.change_state(new_command)
                command.set_value("")
                state.set_value(mtp_service.state)
                print("New State is: " + mtp_service.state)
            else:
                print("This is not a valid command!")
                print("Remaining in state: " + mtp_service.state)
    finally:
        #close connection, remove subcsriptions, etc
        server.stop()