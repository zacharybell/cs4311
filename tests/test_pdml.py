import datetime
import pytest
import sys

from ntbsg.pdml import Pdml

@pytest.fixture
def pdml():
    return Pdml.unmarshall('mocks/cubic.pdml')

class TestPdml:

    def test_properties(self, pdml):
        assert pdml.creator      == 'wireshark/2.0.5'
        assert type(pdml.date)   == datetime.datetime
        assert len(pdml.packets) == 22