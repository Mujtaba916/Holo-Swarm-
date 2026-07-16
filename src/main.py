import pygame
from shapes import heart
from camera import Camera
from config import *
from ui import UI
from particles import ParticleSystem


def main():

    pygame.init()

    # Create Window
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption(TITLE)

    # Clock
    clock = pygame.time.Clock()

    # UI
    ui = UI()

    # Camera
    camera = Camera()

    # Particle System (Animation Area Only)
    particles = ParticleSystem(
        ANIMATION_X,
        ANIMATION_Y,
        ANIMATION_WIDTH,
        ANIMATION_HEIGHT,
        PARTICLE_COUNT,
    )

    running = True

    while running:

        fps = clock.get_fps()

        # ---------------- Events ---------------- #

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.KEYDOWN:

                if event.key == pygame.K_ESCAPE:
                    running = False

        # ---------------- Update ---------------- #

        camera.update()

        particles.update(
             camera.hand_dx,
             camera.hand_dy,
             camera.is_fist,
             camera.hand_open_event
        )

        fingers = camera.hand_tracker.count_fingers()
        if fingers == 2:
             particles.form_shape(
                 heart(
                    600,
                    450,
                    PARTICLE_COUNT
                 )
             )

        # ---------------- Draw ---------------- #

        ui.draw(screen, fps)

        camera.draw(
            screen,
            WIDTH - 350,
            160,
            290,
            180
        )

        particles.draw(screen)

        pygame.display.flip()

        clock.tick(FPS)

    # Release Camera
    camera.release()

    pygame.quit()


if __name__ == "__main__":
    main()