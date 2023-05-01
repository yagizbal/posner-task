import random

def one_loop(location_slots, validity_effect,delay,validity_variance=0,delay_variance=0):
    location_chosen = random.choice(range(location_slots)) #where the target will be

    truthfulness = 0.5+validity_effect
    invalidness = 0.5-validity_effect
    invalid = False
    
    validity_add = 0

    if validity_variance!=0:
        validity_add = random.choice([-1,1])*(random.choice((0,validity_variance)))
    
    if random.random()<invalidness+validity_add:
        invalid=True

    if delay_variance!=0:
        delay_add = range(0,int(delay*delay_variance))
        delay = delay+(random.choice(delay_add)*random.choice([-1,1]))
    


    return invalid,delay