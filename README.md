# Hello Swarm V1

## Hand Movement Controlled Particle Swarm Simulation

Hello Swarm V1 is an interactive computer vision project that allows users to control a particle swarm system using real-time hand movements.

The project creates a connection between **human physical movement and digital particle behavior**. Through a webcam, the system detects the movement of the user's hand and converts it into directional forces that control the movement of particles inside a virtual environment.

This first version focuses on building the foundation of the project by implementing **real-time hand tracking and particle swarm interaction**.

---

# Project Overview

Traditional computer interaction relies on keyboards and mice. Hello Swarm explores a more natural interaction method by allowing users to control digital objects through body movement.

In Version 1:

- A webcam captures hand movement.
- The hand tracking system detects motion direction.
- Movement information is processed.
- The particle swarm responds dynamically.

The result is an interactive particle environment where users can influence the behavior of the swarm using only their hand.

---

---

# Demo Video

The following video demonstrates the real-time interaction of **Hello Swarm V1**, showing how hand movement controls the particle swarm.

<p align="center">
  <video src="https://github.com/Mujtaba916/Holo-Swarm-/blob/main/Hol-Swarm-version-1%20(1).gif" controls width="700">
  </video>
</p>

---

# Features

## Real-Time Hand Tracking

The system uses computer vision technology to detect hand movement through a webcam.

Features:

- Real-time camera input
- Hand position tracking
- Movement direction calculation
- Continuous interaction between user and particles


---

## Hand Controlled Particle Movement

The user's hand movement directly affects the particle swarm.

Supported controls:

| Hand Movement | Particle Response |
|---------------|------------------|
| Move hand left | Particles move left |
| Move hand right | Particles move right |
| Move hand upward | Particles move upward |
| Move hand downward | Particles move downward |

---

## Particle Swarm Simulation

The project contains a custom particle system where each particle has independent properties.

Each particle includes:

- Position
- Velocity
- Movement direction
- Size
- Color

Particles move together as a group while maintaining individual motion.

---

## Dynamic Particle Animation

The project provides real-time visual effects through:

- Smooth particle movement
- Random particle colors
- Continuous animation
- Interactive feedback

---

# System Workflow

```
          Webcam Input

                ↓

        Hand Detection System

        (MediaPipe + OpenCV)

                ↓

       Hand Movement Analysis

                ↓

       Movement Vector Calculation

                ↓

        Particle Force Control

                ↓

        Real-Time Swarm Motion

                ↓

        Pygame Visualization
```

---

# How It Works

## 1. Camera Input

The webcam continuously captures frames from the user's environment.

---

## 2. Hand Detection

MediaPipe identifies hand landmarks and tracks the position of the hand.

The system analyzes changes in hand position between frames.

---

## 3. Movement Calculation

The movement of the hand is converted into directional values:

```
Previous Hand Position

          +

Current Hand Position

          ↓

Movement Direction

          ↓

Particle Movement
```

---

## 4. Particle Response

The calculated movement information is applied to the particle system.

Particles update their:

- Velocity
- Direction
- Position

creating a responsive swarm effect.

---

# Technologies Used

## Programming Language

- Python 3.x


## Libraries

### Pygame

Used for:

- Creating the visual environment
- Rendering particles
- Real-time animation


### OpenCV

Used for:

- Webcam access
- Image processing
- Camera frame handling


### MediaPipe

Used for:

- Hand landmark detection
- Real-time hand tracking


### NumPy

Used for:

- Mathematical calculations
- Vector operations

---

# Project Structure

```
Hello-Swarm-V1/

│
├── main.py
│   Main program entry point
│
├── particle.py
│   Particle class and particle behavior
│
├── swarm.py
│   Swarm movement rules
│
├── hand_tracking.py
│   Hand detection and movement calculation
│
├── colors.py
│   Particle color management
│
├── config.py
│   Project configuration settings
│
├── requirements.txt
│   Required Python libraries
│
└── README.md
    Project documentation
```

---

# Installation

## Requirements

Before running the project, install:

- Python 3.9+
- Webcam
- Required Python libraries


Install dependencies:

```bash
pip install -r requirements.txt
```

---

# Running The Project

Start the application:

```bash
python main.py
```

After launching:

1. Allow webcam access.
2. Place your hand in front of the camera.
3. Move your hand naturally.
4. Observe the particle swarm response.

---

# Controls

| Input | Function |
|------|----------|
| Hand movement | Controls particle swarm direction |
| Webcam | Provides real-time interaction |

---

# Version History

## Version 1.0

### Initial Release

Implemented:

- Basic particle swarm system
- Real-time hand tracking
- Hand movement interaction
- Webcam-based control
- Interactive particle visualization

---

# Current Limitations

Version 1 focuses only on movement interaction.

Not included:

- Gesture recognition
- Finger counting
- Particle image formation
- Shape transformation
- Advanced visual effects

These features can be added in future versions.

---

# Future Development

Possible improvements:

- Gesture-based controls
- Particle shape formation
- Image reconstruction using particles
- More advanced swarm intelligence
- Improved visual effects
- AI-based interaction methods

---

# Project Concept

Hello Swarm V1 explores the relationship between:

```
Human Movement

        +

Computer Vision

        +

Particle Simulation

        +

Interactive Design
```

The project demonstrates how natural human actions can be transformed into digital interactions through creative programming.

---

# Author

Created by:

**MUHAMMAD MUJTABA**

---

# License

This project is created for educational and experimental purposes.
