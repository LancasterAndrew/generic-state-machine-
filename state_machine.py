'''
sample state machine idea
three states with 2 substates each
'''

class state_machine():
    def __init__(self):
        #def the constants
        self.state1 = "state1"
        self.state2 = "state2"
        self.state3 = "state3"
        
        self.substate11 = "1substate1"
        self.substate12 = "1substate2"
        
        self.substate21 = "2substate1"
        self.substate22 = "2substate2"
        
        self.substate31 = "3substate1"
        self.substate32 = "3substate2"
       
        
        self.condition1 = False
        self.condition2 = False
        self.condition3 = False
        self.condition4 = False
        self.condition5 = False
        self.condition6 = False
        
        #create initial point
        self.mach_state = "state1"
        self.mach_substate = "1substate1"
    
    
    #dummy test function only for testing

        
    def print_states(self):
        print('Machine state: {}'.format(self.mach_state))
        print('Machine substate: {}\n'.format(self.mach_substate))
        
    def reset_states(self):
        self.mach_state = self.state1
        self.mach_substate = self.substate11
           
    def change_state(self):
        #current state - subcondition => change condition
        
        #if state1, substate1, and condition1 is true then move to state1, substate2

        if(self.mach_state == self.state1):
            if(self.mach_substate == self.substate11):
                if(self.condition1 == True):
                    self.mach_substate = self.substate12
            elif(self.mach_substate == self.substate12):
                if(self.condition2 == True):
                    self.mach_state = self.state2
                    self.mach_substate = self.substate21
            else:
                self.print_states()
                raise Exception('State machine failure during substate transition. Next command should be "reset_states()"')
        elif(self.mach_state == self.state2):
            if(self.mach_substate == self.substate21):
                if(self.condition3 == True):
                    self.mach_substate = self.substate22
            elif(self.mach_substate == self.substate22):
                if(self.condition4 == True):
                    self.mach_state = self.state3
                    self.mach_substate = self.substate31
            else:
                self.print_states()
                raise Exception('State machine failure during substate transition. Next command should be "reset_states()"')
        elif(self.mach_state == self.state3):
            if(self.mach_substate == self.substate31):
                if(self.condition5 == True):
                    self.mach_substate = self.substate32
            elif(self.mach_substate == self.substate32):
                if(self.condition6 == True):
                    print('Reached final state. Good work.')
            else:
                self.print_states()
                raise Exception('State machine failure during substate transition. Next command should be "reset_states()"')
        else:
            self.print_states()
            raise Exception('State machine failure during state transition. Next command should be "reset_states()"')

        
        self.print_states()
    
           
    
    def change_condition(self,i):
        print('\nChanging condition {}'.format(str(i)))
    
        if(i == 1):
            self.condition1 = not (self.condition1)
        elif(i == 2):
            self.condition2 = not self.condition2
        elif(i == 3):
            self.condition3 = not self.condition3
        elif(i == 4):
            self.condition4 = not self.condition4
        elif(i == 5):
            self.condition5 = not self.condition5
        elif(i == 6):
            self.condition6 = not self.condition6
        if(i>0 and i<7):
            try:
                self.change_state()
            except Exception as err_msg:
                print(str(err_msg))
        else:
            print('junk command')
            
        