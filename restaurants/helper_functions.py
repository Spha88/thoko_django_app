
def add_num_of_star_list(objects):
    '''
        Add number_of_stars list to each attraction based on the "stars" field to be looped in template
    '''

    try: 
        edited_objects = []
        for object in objects:
            object.num_of_stars = [] #adding a new field in object
            for _ in range(object.stars):
                object.num_of_stars.append('star')
            edited_objects.append(object)
        return edited_objects

    except TypeError:
        """Type error means this is not an iterable, its a single object"""
        objects.number_of_stars = []
        for _ in range(objects.stars):
            objects.number_of_stars.append('star')
        print(objects.number_of_stars)
        return objects
    