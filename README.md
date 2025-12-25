# RPG Battle Simulator

A terminal-based RPG battle simulator written in Python.

## Purpose
This project was built as a **foundational Object-Oriented Programming (OOP) practice** to develop strong intuition for class design, inheritance, and polymorphism before moving on to larger AI- and robotics-oriented systems.

The focus of this project is **clean OOP design and logic**, not graphics or UI.

## Features
- Turn-based combat in the terminal
- Player and enemy characters with distinct behaviors
- Different character classes with overridden abilities
- Simple battle loop demonstrating polymorphism
- Extendable design for adding new characters, skills, or items

## OOP Concepts Practiced
- **Classes and Objects**
- **Encapsulation** of state (HP, attack, defense)
- **Inheritance** (base `Character` class with derived classes)
- **Polymorphism** through overridden methods (`special()`)
- **Method overriding** for class-specific behavior
- **Separation of concerns** between game logic and character behavior

## Why a Terminal-Based Game?
A terminal-based design keeps the focus on:
- program structure
- object interactions
- clean logic flow

This allows the project to serve as a strong OOP warm-up before building more complex systems.

## How to Run
Make sure Python 3 is installed, then run:

```bash
python rpg_battle_sim.py
