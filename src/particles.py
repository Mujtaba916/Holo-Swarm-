import pygame
import random
import math

from colors import *
from swarm import cohesion, separation, alignment
from config import MAX_SPEED


class Particle:

    def __init__(self, x, y, w, h):

        self.left = x
        self.top = y
        self.right = x + w
        self.bottom = y + h

        self.x = random.uniform(self.left, self.right)
        self.y = random.uniform(self.top, self.bottom)

        angle = random.uniform(0, math.pi * 2)
        speed = random.uniform(2, 2.5)

        self.dx = math.cos(angle) * speed
        self.dy = math.sin(angle) * speed

        self.radius = random.randint(2, 3)

        self.color = (
            random.randint(50,255),
            random.randint(50,255),
            random.randint(50,255)
        )

        self.target_x = self.x
        self.target_y = self.y


    def update(
        self,
        hand_dx=0,
        hand_dy=0,
        gather=False,
        scatter=False,
        center_x=None,
        center_y=None,
        all_particles=None
    ):


        # Hand movement force

        self.dx += hand_dx * 20
        self.dy += hand_dy * 20



        # Gather particles

        if gather and center_x is not None and center_y is not None:

            ax = (center_x - self.x) * 0.01
            ay = (center_y - self.y) * 0.01

            self.dx += ax
            self.dy += ay



        # Scatter particles

        if scatter:

            angle = random.uniform(0, math.pi * 2)

            force = random.uniform(3,7)

            self.dx += math.cos(angle) * force
            self.dy += math.sin(angle) * force



        # Swarm intelligence

        if all_particles:


            cx, cy = cohesion(
                self,
                all_particles
            )


            sx, sy = separation(
                self,
                all_particles
            )


            ax, ay = alignment(
                self,
                all_particles
            )


            self.dx += cx + sx + ax
            self.dy += cy + sy + ay



        # Friction

        self.dx *= 0.99
        self.dy *= 0.99



        # Limit speed

        speed = math.sqrt(
            self.dx*self.dx +
            self.dy*self.dy
        )


        if speed > MAX_SPEED:

            self.dx = (
                self.dx / speed
            ) * MAX_SPEED


            self.dy = (
                self.dy / speed
            ) * MAX_SPEED



        # Move

        self.x += self.dx
        self.y += self.dy



        # Border collision

        if self.x < self.left:

            self.x = self.left
            self.dx *= -1


        elif self.x > self.right:

            self.x = self.right
            self.dx *= -1



        if self.y < self.top:

            self.y = self.top
            self.dy *= -1


        elif self.y > self.bottom:

            self.y = self.bottom
            self.dy *= -1



        # Shape attraction

        tx = self.target_x - self.x
        ty = self.target_y - self.y


        self.dx += tx * 0.002
        self.dy += ty * 0.002



    def draw(self, screen):


        # Glow

        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            self.radius + 6,
            1
        )


        # Ring

        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            self.radius + 3,
            1
        )


        # Core

        pygame.draw.circle(
            screen,
            self.color,
            (int(self.x), int(self.y)),
            self.radius
        )




class ParticleSystem:


    def __init__(self, x, y, w, h, count):

        self.particles = [

            Particle(
                x,
                y,
                w,
                h
            )

            for _ in range(count)

        ]



    def update(
        self,
        hand_dx=0,
        hand_dy=0,
        gather=False,
        scatter=False
    ):


        center_x = (
            self.particles[0].left +
            self.particles[0].right
        ) / 2


        center_y = (
            self.particles[0].top +
            self.particles[0].bottom
        ) / 2



        for p in self.particles:


            p.update(

                hand_dx,

                hand_dy,

                gather,

                scatter,

                center_x,

                center_y,

                self.particles

            )



    def draw(self, screen):

        for p in self.particles:

            p.draw(screen)



    def form_shape(self, points):

        for particle, point in zip(
            self.particles,
            points
        ):

            particle.target_x = point[0]
            particle.target_y = point[1]