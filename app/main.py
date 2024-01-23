from typing import Union


class Distance:
    def __init__(self, km: float) -> None:
        self.km = km

    def __str__(self) -> str:
        return f"Distance: {self.km} kilometers."

    def __repr__(self) -> str:
        return f"Distance(km={self.km})"

    def __add__(self, new_dist: Union["Distance", int, float]) -> "Distance":
        if isinstance(new_dist, (int, float)):
            new_distance = new_dist
        elif isinstance(new_dist, Distance):
            new_distance = new_dist.km
        return Distance(self.km + new_distance)

    def __iadd__(self, new_dist: Union["Distance", int, float]) -> "Distance":
        if isinstance(new_dist, Distance):
            self.km += new_dist.km
        elif isinstance(new_dist, (int, float)):
            self.km += new_dist
        return self

    def __mul__(self, multiplier: Union["Distance", int, float]) -> "Distance":
        if isinstance(multiplier, Distance):
            raise TypeError("not for Distance data type")
        elif isinstance(multiplier, (int, float)):
            return Distance(self.km * multiplier)

    def __truediv__(self, div: Union[int, float]) -> "Distance":
        if isinstance(div, (int, float)) and div != 0:
            return Distance(round(self.km / div, 2))

    def __lt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km < other.km
        return self.km < other

    def __gt__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km > other.km
        return self.km > other

    def __eq__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km == other.km
        return self.km == other

    def __le__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km <= other.km
        return self.km <= other

    def __ge__(self, other: Union["Distance", int, float]) -> bool:
        if isinstance(other, Distance):
            return self.km >= other.km
        return self.km >= other
