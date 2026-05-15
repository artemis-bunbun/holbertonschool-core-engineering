#!/usr/bin/env python3
"""Mixin-based dragon example."""


class SwimMixin:
    """Provide swimming behavior."""

    def swim(self):
        """Print the swimming action."""
        print("The creature swims!")


class FlyMixin:
    """Provide flying behavior."""

    def fly(self):
        """Print the flying action."""
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """A dragon composed from swim and fly mixins."""

    def roar(self):
        """Print the roaring action."""
        print("The dragon roars!")
