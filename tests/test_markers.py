import pytest

@pytest.mark.web
def test_one():
	assert True

@pytest.mark.api
def test_two():
	assert True

@pytest.mark.p0
def test_three():
	assert True