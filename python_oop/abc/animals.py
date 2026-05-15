#!/usr/bin/env python3
"""Abstract animal class and concrete implementations."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class for animals."""

    @abstractmethod
    def sound(self):
        """Return the sound the animal makes."""
        pass


class Dog(Animal):
    """A dog that barks."""

    def sound(self):
        """Return the dog's sound."""
        return "Bark"


class Cat(Animal):
    """A cat that meows."""

    def sound(self):
        """Return the cat's sound."""
        return "Meow"
