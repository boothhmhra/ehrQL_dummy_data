from ehrql import create_dataset
from ehrql.tables.core import patients, ons_deaths
from ehrql.tables.tpp import apcs, practice_registrations

dataset = create_dataset()
dataset.configure_dummy_data(population_size=50)

study_start_date = "2022-01-01"
study_end_date = "2023-01-01"

possible_icd10 = ["I50", "I500", "I501", "I509"]

https://docs.opensafely.org/ehrql/tutorials/dummy-data/provide-dummy-tables/