
from state_machine import *

'''
test plan

'''

sm = state_machine()

sm.print_states()

#move from substate1 to substate2
sm.change_condition(1)    

#throw junk at it to show it doesn't move
sm.change_condition(4)
sm.change_condition(4)

#change to state 2
sm.change_condition(2)    

#throw junk at it to show it doesn't move
sm.change_condition(4)
sm.change_condition(4)

#change to substate2
sm.change_condition(3)

#change to state 3
sm.change_condition(4)    

#throw junk at it to show it doesn't move
sm.change_condition(1)
sm.change_condition(1)

#change to substate2
sm.change_condition(5)

#throw junk at it to show it doesn't move
sm.change_condition(1)
sm.change_condition(1)
sm.change_condition(-1)
sm.change_condition(7)

#change to end of state machine
sm.change_condition(6)
