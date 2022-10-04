import random
from SearchNode import SearchNode
import collections

#==============================================================================
# GRAPH_SEARCH
#
# The fringe and closed list must be drawn while the thinking takes place.
# - Draw the closed list blue (255, 0, 0).
# - Draw the fringe in green (0, 255, 0).
#
# There must be NO console printing in this python file. Make sure you remove
# them or comment them out when you are done.
#==============================================================================
def graph_search(problem=None,
                 Node=None,
                 fringe=None,
                 closed_list=None,
                 view0=None,
                 ):

    #==========================================================================
    # TODO: The code here creates a *random* solution starting at state (0,0).
    # Replace with the correct late version of graph search algorithm.
    #==========================================================================
    solution = []
    """
    This is the incorrect Version, Needs to be fixed.

    Correct solution looks like:
    closed list is empty
    fringe has the initial state
    While fringe not empty:
        pull a state,s, from the fringe.
        check to see if s is a goal state.
        if it is:
            return the search node, for walking back to root.
        else:
            add s.state() to closed list
            expand s to s0 with action a0 ... sn to an
            if s0 not in fringe or closed list:
                add s0 to fringe
                point s0 to s with parent action a0
            repeat for s1 ... sn
    """


#Test Code:
    fringe.put(Node)
    maze = problem.maze
    while len(fringe) > 0:
        s = fringe.get()
        state = s.state
        #print(state)
        if problem.goal_test(state):
            solution.append(s)
            while s.parent != None:
                s = s.parent
                solution.append(s)
                solution = solution[::-1]
                #for node in solution:
                    #print(node.state, ' ', node.parent_action)
            return solution
        closed_list.put(state)
        for nodes in problem.successors(state):
            action = nodes[0]
            r,c = nodes[1]
            if (r,c) in closed_list.xs:
                pass
            else:
                fringe.put(SearchNode((r,c), s, action))
            if view0:
                if len(closed_list) == 1:
                    view0['maze'].background[(r,c)] = (0,255,0)
                else:
                    for state in closed_list.xs:
                        r,c = state
                        if view0['maze'].background[r,c] != [0,0,0] or view0['maze'].background[r,c] != [0,255,0]:
                            view0['maze'].background[r,c] = [255,0,0]
                            for node in fringe:
                                r,c = node.state
                                view0['maze'].background[r,c] = [0,0,255]
                view0.run() # Draw everything
            
        
    return None # None is used to indicate no solution

    

"""
    while 1:
                
        (r, c) = (0, 0)
        maze = problem.maze
        for action in solution:
            (r, c) = maze.get_adj_tuple((r, c), action)
        dirs = maze.get_directions((r, c))
        if dirs != []:
            action = random.choice(dirs)
            solution.append(action)
            print("actions:", dirs, ",", end='')
            print("choose:", action, ",", end='')
            print("resulting pos:", maze.get_adj_tuple((r, c), action))
            print("solution:", solution)
            print()
    
            
        if random.randrange(0, 200) == 0:
            return solution

"""
        #======================================================================
        # TODO: The following randomly colors the maze cells with red and blue.
        # Replace with the following:
        # - Iterate through the fringe and color the states of the search
        #   nodes with blue
        # - Iterate through the closed list and color the states with red
	# - Color the initial state green (Done on init)
        #======================================================================
"""
        if view0:
            if random.randrange(2) == 0:
                r = random.randrange(maze.rows)
                c = random.randrange(maze.cols)
                if random.choice([0,1]) == 0:
                    view0['maze'].background[(r,c)] = (255,0,0) # color it red
                else:
                    view0['maze'].background[(r,c)] = (0,0,255) # color it blue
            view0.run() # Draw everything
        """
