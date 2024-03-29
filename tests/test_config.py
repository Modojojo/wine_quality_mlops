import pytest
from prediction_service import prediction
import prediction_service

input_data = {
    "incorrect_range":
    {
        "fixed_acidity": 7897897,
        "volatile_acidity": 555,
        "citric_acid": 99,
        "residual_sugar": 99,
        "chlorides": 12,
        "free_sulfur_dioxide": 789,
        "total_sulfur_dioxide": 75,
        "density": 2,
        "pH": 33,
        "sulphates": 9,
        "alcohol": 9
    },

    "correct_range":
        {
        "fixed_acidity": 5,
        "volatile_acidity": 1,
        "citric_acid": 0.5,
        "residual_sugar": 10,
        "chlorides": 0.5,
        "free_sulfur_dioxide": 3,
        "total_sulfur_dioxide": 75,
        "density": 1,
        "pH": 3,
        "sulphates": 1,
        "alcohol": 9
    },

    "incorrect_col":
    {
        "fixed acidity": 5,
        "volatile acidity": 1,
        "citric acid": 0.5,
        "residual sugar": 10,
        "chlorides": 0.5,
        "free sulfur dioxide": 3,
        "total_sulfur dioxide": 75,
        "density": 1,
        "pH": 3,
        "sulphates": 1,
        "alcohol": 9
    },

    "no_data":
    {
        "fixed_acidity": "",
        "volatile_acidity": "",
        "citric_acid": "",
        "residual_sugar": "",
        "chlorides": "",
        "free_sulfur_dioxide": "",
        "total_sulfur_dioxide": "",
        "density": "",
        "pH": "",
        "sulphates": "",
        "alcohol": ""
    }
}

TARGET_RANGE = {
    "min": 3.0,
    "max": 8.0
}


def test_form_response_correct_range(data=input_data["correct_range"]):
    res = prediction.form_response(data)
    assert TARGET_RANGE["min"] <= res <= TARGET_RANGE["max"]


def test_api_response_correct_range(data=input_data["correct_range"]):
    res = prediction.api_response(data)
    assert TARGET_RANGE["min"] <= res["response"] <= TARGET_RANGE["max"]


def test_form_response_incorrect_range(data=input_data["incorrect_range"]):
    with pytest.raises(prediction_service.prediction.NotInRange):
        res = prediction.form_response(data)


def test_api_response_incorrect_range(data=input_data["incorrect_range"]):
    res = prediction.api_response(data)
    assert res["response"] == prediction_service.prediction.NotInRange().message


def test_api_response_incorrect_col(data=input_data["incorrect_col"]):
    res = prediction.api_response(data)
    assert res["response"] == prediction_service.prediction.NotInCols().message


def test_form_response_no_data(data=input_data["no_data"]):
    with pytest.raises(prediction_service.prediction.NoDataEntered):
        res = prediction.form_response(data)
