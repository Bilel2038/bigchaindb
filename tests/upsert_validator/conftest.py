import pytest


@pytest.fixture
def b_mock(b, network_validators):
    b.get_validators = mock_get_validators(network_validators)

    return b


@pytest.fixture
def new_validator():
    public_key = '1718D2DBFF00158A0852A17A01C78F4DCF3BA8E4FB7B8586807FAC182A535034'
    power = 1
    node_id = 'fake_node_id'

    return {'public_key': public_key,
            'power': power,
            'node_id': node_id}


def mock_get_validators(network_validators):
    def validator_set():
        validators = []
        for public_key, power in network_validators.items():
            validators.append({
                'pub_key': {'type': 'AC26791624DE60', 'value': public_key},
                'voting_power': power
            })
        return validators

    return validator_set
