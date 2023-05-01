import random

def one_loop(location_slots, validity_effect,delay,validity_variance=0,delay_variance=0):
    location_chosen = random.choice(range(location_slots)) #where the target will be

    truthfulness = 0.5+validity_effect
    invalidness = 0.5-validity_effect
    invalid = False
    
    validity_add = 0

    if validity_variance!=0:
        validity_add = random.choice([-1,1])*(random.choice((0,validity_variance)))
    
    v = random.random()
    if v<invalidness+validity_add:
        invalid=True
        list2 = list(range(location_slots))
        list2.remove(location_chosen)
        location_of_arrow = random.choice(list2)
    else:
        location_of_arrow = location_chosen
    if delay_variance!=0:
        delay_add = range(0,int(delay*delay_variance))
        delay = delay+(random.choice(delay_add)*random.choice([-1,1]))

    print(v,invalidness)
    return invalid,delay,location_chosen,location_slots,location_of_arrow