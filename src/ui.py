import pygame
from colors import *


class UI:

    def __init__(self):

        self.title_font = pygame.font.SysFont("Segoe UI", 42, True)
        self.subtitle_font = pygame.font.SysFont("Segoe UI", 22)
        self.status_font = pygame.font.SysFont("Segoe UI", 20)
        self.fps_font = pygame.font.SysFont("Consolas", 18)

    def draw(self, screen, fps):

        width = screen.get_width()
        height = screen.get_height()

        # Background

        screen.fill(BACKGROUND)
        # Top Bar

        pygame.draw.rect(screen, PANEL, (0, 0, width, 90))

        pygame.draw.line(screen, BORDER, (0, 90), (width, 90), 2)

        # Title

        title = self.title_font.render("HoloSwarm", True, WHITE)

        screen.blit(title, (35, 18))

        # Tagline

        tag = self.subtitle_font.render(
            "Control Light with a Gesture.",
            True,
            BLUE
        )

        screen.blit(tag, (38, 58))

        # Webcam Panel

        panel_width = 330
        panel_height = 240

        panel_x = width - panel_width - 40
        panel_y = 120

        pygame.draw.rect(
            screen,
            PANEL,
            (panel_x, panel_y, panel_width, panel_height),
            border_radius=12
        )

        pygame.draw.rect(
            screen,
            BORDER,
            (panel_x, panel_y, panel_width, panel_height),
            2,
            border_radius=12
        )

        webcam = self.status_font.render("Webcam", True, WHITE)

        screen.blit(webcam, (panel_x + 20, panel_y + 15))

        # Animation Area

        pygame.draw.rect(
            screen,
            PANEL,
            (35, 120, width - 450, height - 200),
            border_radius=12
        )

        pygame.draw.rect(
            screen,
            BORDER,
            (35, 120, width - 450, height - 200),
            2,
            border_radius=12
        )

        # Status

        pygame.draw.rect(
            screen,
            PANEL,
            (0, height - 60, width, 60)
        )

        status = self.status_font.render(
            "Status : Waiting for hand...",
            True,
            GRAY
        )

        screen.blit(status, (30, height - 38))

        # FPS

        fps_text = self.fps_font.render(
            f"FPS : {int(fps)}",
            True,
            BLUE
        )

        screen.blit(fps_text, (width - 120, 30))