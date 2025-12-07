from dataclasses import dataclass
from typing import Any, Literal


@dataclass
class SensorSpec:
    """Sensor specification for footprint computation.

    Attributes:
        fov_across: Field of view across track in degrees.
        fov_along: Field of view along track in degrees.
    """

    fov_across: float
    fov_along: float


@dataclass
class Footprint:
    """Footprint representation.

    Attributes:
        geometry_type: Type of the geometry (e.g., "Polygon").
        coordinates: List of (longitude, latitude) tuples defining the footprint geometry.
        meta: Metadata dictionary.
    """

    geometry_type: Literal["Polygon"]
    coordinates: list[tuple[float, float]]
    meta: dict[str, Any]
