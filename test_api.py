import pytest
import json
from api import app

def test_get_a_joke():
    response = app.test_client().get('/')
    assert response.status_code == 200

    res = json.loads(response.data.decode('utf-8'))
    assert type(res) == dict
    assert 'joke' in res
    assert len(res['joke']) > 0
    

def test_get_a_greeting():
    response = app.test_client().get('/hello')
    assert response.status_code == 200

    res = json.loads(response.data.decode('utf-8'))
    assert type(res) == dict
    assert 'hello' in res
    assert res['hello'] == 'world'
