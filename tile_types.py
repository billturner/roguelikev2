from typing import Tuple

import numpy as np  # type: ignore


# tile type compatible with Console.tiles_rgb
graphic_dt = np.dtype(
    [
        ("ch", np.int32),  # Unicode codepoint.
        ("fg", "3B"),  # 3 unsigned bytes, for RGB colors
        ("bg", "3B"),
    ]
)

# tile struct for statically defined tile data
tile_dt = np.dtype(
    [
        ("walkable", np.bool8),  # True if can be walked over
        ("transparent", np.bool8),  # True if it does not block FOV
        ("dark", graphic_dt),  # graphics for when not in FOV
    ]
)


def new_tile(
    *,  # enforce use of keywords
    walkable: int,
    transparent: int,
    dark: Tuple[int, Tuple[int, int, int], Tuple[int, int, int]],
) -> np.ndarray:
    """Helper function for defining tile types"""
    return np.array((walkable, transparent, dark), dtype=tile_dt)


floor = new_tile(
    walkable=True, transparent=True, dark=(ord(" "), (255, 255, 255), (50, 50, 150))
)

wall = new_tile(
    walkable=False, transparent=False, dark=(ord(" "), (255, 255, 255), (0, 0, 100))
)
