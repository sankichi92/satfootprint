from datetime import datetime

import pytest

from satfootprint import SensorSpec, compute_footprint


def test_compute_footprint():
    # Given
    position = [7000.0, 0.0, 0.0]
    epoch = datetime(2025, 12, 6)
    sensor_spec = SensorSpec(fov_across=8.0, fov_along=4.5)

    # When
    with pytest.raises(NotImplementedError):
        compute_footprint(position, epoch, sensor_spec)
