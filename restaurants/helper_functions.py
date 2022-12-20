
def add_num_of_star_list(objects):
    '''
        Add number_of_stars list to each attraction based on the "stars" field to be looped in template
    '''
    
    edited_objects = []
    for object in objects:
        object.num_of_stars = [] #adding a new field in object
        for _ in range(object.stars):
            object.num_of_stars.append('star')
        edited_objects.append(object)
    return edited_objects