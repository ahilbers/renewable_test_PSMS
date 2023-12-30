import pytest
import pandas as pd


def _get_ts_data_1_region():
    '''Create sample time series data for '1_region' model.'''
    ts_data_6_region = _get_ts_data_6_region()
    ts_data = ts_data_6_region.loc[:, ['demand_region5', 'wind_region5', 'solar_region5']]
    ts_data.columns = ['demand', 'wind', 'solar']
    return ts_data


def _get_ts_data_6_region():
    '''Create sample time series data for '6_region' model.'''
    ts_data = pd.DataFrame(
        data = [
            [44.68, 40.78, 28.38, 0.5412, 0.3456, 0.1399, 0.0000, 0.0000, 0.0000],
            [44.62, 38.51, 27.04, 0.5289, 0.3624, 0.1349, 0.0000, 0.0000, 0.0000],
            [45.37, 37.53, 26.13, 0.5137, 0.3609, 0.1299, 0.0000, 0.0000, 0.0000],
            [47.32, 38.41, 25.61, 0.4743, 0.3572, 0.1278, 0.0082, 0.0001, 0.0000],
            [52.58, 40.77, 26.06, 0.4711, 0.3480, 0.1225, 0.0608, 0.0124, 0.0017],
            [57.69, 44.34, 30.16, 0.4730, 0.3624, 0.1229, 0.1527, 0.0426, 0.0657],
            [61.11, 47.41, 35.57, 0.5049, 0.4005, 0.1845, 0.2625, 0.0790, 0.2228],
            [62.92, 49.53, 39.23, 0.6612, 0.4608, 0.2275, 0.3726, 0.1340, 0.4092],
            [64.61, 50.57, 41.01, 0.7429, 0.5247, 0.2865, 0.4721, 0.1919, 0.5826],
            [66.08, 51.25, 41.68, 0.7827, 0.5800, 0.3055, 0.5673, 0.2248, 0.7143],
            [65.79, 51.98, 42.18, 0.7915, 0.6310, 0.3465, 0.6617, 0.2682, 0.8204],
            [64.74, 51.00, 42.35, 0.7866, 0.6756, 0.4052, 0.7141, 0.3491, 0.8725],
            [63.39, 49.92, 41.79, 0.7493, 0.7112, 0.4643, 0.6913, 0.4588, 0.8643],
            [62.35, 48.39, 41.12, 0.6752, 0.7306, 0.4989, 0.6222, 0.5549, 0.8064],
            [61.27, 46.97, 40.77, 0.5736, 0.7486, 0.5111, 0.5168, 0.5573, 0.6960],
            [60.94, 46.24, 41.58, 0.4227, 0.7846, 0.4886, 0.3886, 0.4436, 0.5215],
            [60.85, 46.94, 42.39, 0.2636, 0.7935, 0.4216, 0.2661, 0.3073, 0.3312],
            [60.53, 47.75, 42.26, 0.1354, 0.8105, 0.3441, 0.1471, 0.2029, 0.1905],
            [58.87, 46.87, 41.71, 0.0558, 0.7880, 0.2766, 0.0520, 0.1208, 0.0770],
            [56.73, 45.93, 40.63, 0.0581, 0.7238, 0.1988, 0.0032, 0.0404, 0.0088],
            [54.58, 47.60, 39.16, 0.0834, 0.6645, 0.1467, 0.0000, 0.0018, 0.0000],
            [50.88, 48.66, 36.85, 0.1076, 0.6388, 0.1387, 0.0000, 0.0000, 0.0000],
            [47.71, 45.45, 33.13, 0.1158, 0.6313, 0.1308, 0.0000, 0.0000, 0.0000],
            [45.70, 42.43, 29.47, 0.1130, 0.6118, 0.1111, 0.0000, 0.0000, 0.0000]
        ],
        index=pd.date_range(start='2020-06-01', periods=24, freq='h'),
        columns=[
            'demand_region2', 'demand_region4', 'demand_region5',
            'wind_region2', 'wind_region5', 'wind_region6',
            'solar_region2', 'solar_region5', 'solar_region6'
        ]
    )
    return ts_data


@pytest.fixture()
def ts_data_dict() -> dict[str, pd.DataFrame]:
    '''Sample time series data for both '1_region' and '6_region' models.'''
    out_dict = {'1_region': _get_ts_data_1_region(), '6_region': _get_ts_data_6_region()}
    return out_dict


@pytest.fixture()
def fixed_caps_dict() -> dict[str, dict[str, float]]:
    return {
        '1_region': {
            'cap_baseload_total': 10.,
            'cap_peaking_total': 20.,
            'cap_wind_total': 20.,
            'cap_solar_total': 15.,
            'cap_storage_power_total': 10.,
            'cap_storage_energy_total': 50.
        },
        '6_region': {
            'cap_baseload_region1': 20.,
            'cap_peaking_region1': 25.,
            'cap_transmission_region1_region2': 30.,
            'cap_transmission_region1_region5': 20.,
            'cap_transmission_region1_region6': 10.,
            'cap_wind_region2': 40.,
            'cap_solar_region2': 20.,
            'cap_storage_power_region2': 20.,
            'cap_storage_energy_region2': 100.,
            'cap_transmission_region2_region3': 40.,
            'cap_baseload_region3': 50.,
            'cap_peaking_region3': 20.,
            'cap_transmission_region3_region4': 30.,
            'cap_transmission_region4_region5': 30.,
            'cap_wind_region5': 40.,
            'cap_solar_region5': 30.,
            'cap_storage_power_region5': 20.,
            'cap_storage_energy_region5': 100.,
            'cap_transmission_region5_region6': 10.,
            'cap_baseload_region6': 20.,
            'cap_peaking_region6': 20.,
            'cap_wind_region6': 30.,
            'cap_solar_region6': 20.,
            'cap_storage_power_region6': 20.,
            'cap_storage_energy_region6': 100.,
        }
    }
