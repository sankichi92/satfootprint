from collections.abc import Sequence
from datetime import datetime

from .models import Footprint, SensorSpec

__all__ = ["compute_footprint", "Footprint", "SensorSpec"]


def compute_footprint(
    position: Sequence[float],
    epoch: datetime,
    sensor_spec: SensorSpec,
) -> Footprint:
    """Compute the satellite footprint.

    Args:
        position: Satellite position in ECI coordinates [x, y, z] in kilometers.
        epoch: Epoch time of the position.
        sensor_spec: Sensor specification.

    Returns:
        Footprint: Computed footprint object.
    """
    raise NotImplementedError()
