#!/usr/bin/env python3
"""Verbose list implementation with notifications."""


class VerboseList(list):
    """A list that prints messages when modified."""

    def append(self, item):
        """Append an item and report it."""
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, items):
        """Extend the list and report how many items were added."""
        count = len(items)
        super().extend(items)
        print(f"Extended the list with [{count}] items.")

    def remove(self, item):
        """Remove an item and report it."""
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """Pop an item and report it."""
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
