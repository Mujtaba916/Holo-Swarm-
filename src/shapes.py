import math


def heart(cx,cy,count):

    points=[]

    for i in range(count):

        t = math.pi*2*i/count

        x = 16*math.sin(t)**3

        y = (
            13*math.cos(t)
            -5*math.cos(2*t)
            -2*math.cos(3*t)
            -math.cos(4*t)
        )


        points.append(
            (
                cx+x*8,
                cy-y*8
            )
        )

    return points