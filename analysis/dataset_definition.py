from ehrql import create_dataset, show
from ehrql.tables.core import patients, clinical_events

dataset = create_dataset()


age = patients.age_on("2020-03-31")
first_event_date = clinical_events.sort_by(clinical_events.date).first_for_patient().date

dataset.define_population((age > 18) & (age < 80) & (patients.sex == "female"))
dataset.configure_dummy_data(population_size=30)
dataset.age = age
dataset.sex = patients.sex
dataset.first_event_date = first_event_date

dataset.after_dob = first_event_date > patients.date_of_birth
dataset.before_dod = (first_event_date < patients.date_of_death) | patients.date_of_death.is_null()

# show the date column from the original clinical_events table
show(clinical_events.date)
# filter to a patient frame, with the first event for each patient
first_event_date = clinical_events.sort_by(clinical_events.date).first_for_patient().date
# show the date column from the filtered first_events frame
show(first_event_date)