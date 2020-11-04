import pytest

from kitchen import utensils, appliances


@pytest.fixture(autouse=True)
def knife():
    knife = utensils.Knife()
    knife.sharpen()

    yield knife

    knife.clean()


@pytest.fixture(autouse=True)
def oven():
    oven = appliances.Oven()
    oven.preheat()

    yield oven

    oven.turn_off()
