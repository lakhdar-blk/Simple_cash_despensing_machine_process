import simpy
import random


def dispensing_machine(environment, users):
    
    print('--------------------------------------')

    while(users):

        users -= 1
        print('New user enter arrived at', environment.now)
        taken_time = random.choice([10, 15, 20, 25, 30])  #you can specify here the estimated spent time by machine users
        yield environment.timeout(taken_time)
        print('User took his money at', environment.now)
        leave_time = random.choice([2, 3, 4, 5])
        yield environment.timeout(leave_time)
        print('User leave at', environment.now)
        print("User time:", taken_time+leave_time)
        print('--------------------------------------')


if __name__ == '__main__':

    #=====specify the number of agents (users, clients, ...)
    while(True):
        
        users = input('Number of users:')
        try:
            users = int(users)
            break
        except:
            print('Invalid data !')
    #=====specify the number of agents (users, clients, ...)


    #=======create an environment
    environment = simpy.Environment()
    #=======create an environment

    #=======create_process=======#
    environment.process(dispensing_machine(environment, users))
    #=======create_process=========#
    
    #=========start_process========#
    environment.run()
    #=========start_process========#

    print('Total spent time: ', environment.now)
