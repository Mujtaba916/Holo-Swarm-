import math


def limit(value, maximum):

    if value > maximum:
        return maximum

    if value < -maximum:
        return -maximum

    return value



def distance(p1, p2):

    dx = p1.x - p2.x
    dy = p1.y - p2.y

    return math.sqrt(dx*dx + dy*dy)



def cohesion(particle, particles):

    center_x = 0
    center_y = 0
    count = 0


    for other in particles:

        if other != particle:

            center_x += other.x
            center_y += other.y
            count += 1


    if count == 0:
        return 0,0


    center_x /= count
    center_y /= count


    return (
        (center_x-particle.x)*0.0005,
        (center_y-particle.y)*0.0005
    )



def separation(particle, particles):

    force_x = 0
    force_y = 0


    for other in particles:

        if other != particle:

            d = distance(particle, other)


            if d < 35 and d > 0:

                force_x += (particle.x-other.x)/d
                force_y += (particle.y-other.y)/d


    return force_x*0.05, force_y*0.05



def alignment(particle, particles):

    velocity_x = 0
    velocity_y = 0
    count = 0


    for other in particles:

        if other != particle:

            velocity_x += other.dx
            velocity_y += other.dy
            count += 1


    if count == 0:
        return 0,0


    velocity_x /= count
    velocity_y /= count


    return (
        (velocity_x-particle.dx)*0.02,
        (velocity_y-particle.dy)*0.02
    )