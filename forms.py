from flask_wtf import FlaskForm
import pandas as pd
from wtforms import (
    SelectField,
    DateField,
    TimeField,
    IntegerField,
    SubmitField

)
from wtforms.validators import DataRequired

train = pd.read_csv("data/train.csv")
test = pd.read_csv("data/test.csv")
x_data = pd.concat([train, test], axis=0).drop(columns="price")


class InputForm(FlaskForm):
    airline = SelectField(
        label="AIRLINE",
        choices=x_data.airline.unique().tolist(),
        validators=[DataRequired()]
    )

    date_of_journey = DateField(
        label="DATE OF JOURNEY",
        validators=[DataRequired()]
    )

    source = SelectField(
        label="SOURCE",
        choices=x_data.source.unique().tolist(),
        validators=[DataRequired()]
    )

    destination = SelectField(
        label="SOURCE",
        choices=x_data.destination.unique().tolist(),
        validators=[DataRequired()]
    )

    dep_time = TimeField(
        label="DEPARTURE TIME",
        validators=[DataRequired()]
    )

    arrival_time = TimeField(
        label="ARRIVAL TIME",
        validators=[DataRequired()]
    )

    duration = IntegerField(
        label="DURATION",
        validators=[DataRequired()]
    )

    total_stops = IntegerField(
        label="TOTAL STOPS",
        validators=[DataRequired()]
    )

    additional_info = SelectField(
        label="ADDITIONAL FIELD",
        choices=x_data.additional_info.unique().tolist(),
        validators=[DataRequired()]
    )

    submit = SubmitField("PREDICT")
