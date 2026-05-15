#!/usr/bin/env python3
"""Multiple inheritance example with Fish, Bird, and FlyingFish."""


class Fish:
    """A fish that swims in water."""

    def swim(self):
        """Print that the fish is swimming."""
        print("The fish is swimming")

    def habitat(self):
        """Print the fish's habitat."""
        print("The fish lives in water")


class Bird:
    """A bird that flies in the sky."""

    def fly(self):
        """Print that the bird is flying."""
        print("The bird is flying")

    def habitat(self):
        """Print the bird's habitat."""
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """A flying fish that inherits from both Fish and Bird."""

    def swim(self):
        """Override swim to print the flying fish swimming."""
        print("The flying fish is swimming!")

    def fly(self):
        """Override fly to print the flying fish flying."""
        print("The flying fish is soaring!")

    def habitat(self):
        """Override habitat to describe both water and sky."""
        print("The flying fish lives both in water and the sky!")
