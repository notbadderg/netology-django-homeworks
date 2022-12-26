import pytest

from rest_framework.test import APIClient
from model_bakery import baker

from students.models import Course, Student

API_V1_COURSES_URL = '/api/v1/courses'


@pytest.fixture
def client():
    return APIClient()


@pytest.fixture
def course_factory():
    def factory(*args, **kwargs):
        return baker.make(Course, *args, **kwargs)
    return factory


@pytest.fixture
def student_factory():
    def factory(*args, **kwargs):
        return baker.make(Student, *args, **kwargs)
    return factory


@pytest.mark.django_db
def test_get_course_single(client, course_factory):
    courses = course_factory(_quantity=1)
    eval_course_index = 0
    eval_course_id = courses[eval_course_index].id

    response = client.get(f'{API_V1_COURSES_URL}/{eval_course_id}/')
    data = response.json()

    assert response.status_code == 200
    assert data['name'] == courses[int(eval_course_index)].name


@pytest.mark.django_db
def test_get_courses_list(client, course_factory):
    courses = course_factory(_quantity=100)

    response = client.get(f'{API_V1_COURSES_URL}/')
    data = response.json()

    assert response.status_code == 200
    for i, c in enumerate(data):
        assert c['name'] == courses[i].name


@pytest.mark.django_db
def test_get_courses_list_filter_id(client, course_factory):
    courses = course_factory(_quantity=100)
    eval_course_index = 42
    eval_course_id = courses[eval_course_index].id

    response = client.get(f'{API_V1_COURSES_URL}/?id={eval_course_id}')
    data = response.json()

    assert response.status_code == 200
    assert data[0]['name'] == courses[eval_course_index].name


@pytest.mark.django_db
def test_get_courses_list_filter_name(client, course_factory):
    courses = course_factory(_quantity=100)
    eval_course_index = 69
    eval_course_name = courses[eval_course_index].name

    response = client.get(f'{API_V1_COURSES_URL}/?name={eval_course_name}')
    data = response.json()

    assert response.status_code == 200
    assert data[0]['id'] == courses[eval_course_index].id


@pytest.mark.django_db
def test_post_course_create(client):
    count = Course.objects.count()
    course_test_name = 'test_course123'

    response = client.post(f'{API_V1_COURSES_URL}/', data={'name': course_test_name})
    data = response.json()

    assert response.status_code == 201
    assert Course.objects.count() == count + 1
    assert data['name'] == course_test_name


@pytest.mark.django_db
def test_patch_course_update(client, course_factory):
    courses = course_factory(_quantity=100)
    eval_course_index = 32
    eval_course_id = courses[eval_course_index].id
    course_old_name = courses[eval_course_index].name
    course_test_new_name = 'test_course123321'

    response = client.patch(f'{API_V1_COURSES_URL}/{eval_course_id}/', data={'name': course_test_new_name})
    data = response.json()

    assert response.status_code == 200
    assert data['name'] != course_old_name
    assert data['name'] == course_test_new_name


@pytest.mark.django_db
def test_delete_course(client, course_factory):
    courses = course_factory(_quantity=100)
    eval_course_index = 99
    eval_course_id = courses[eval_course_index].id

    response_1 = client.delete(f'{API_V1_COURSES_URL}/{eval_course_id}/')
    response_2 = client.get(f'{API_V1_COURSES_URL}/{eval_course_id}/')

    assert response_1.status_code == 204
    assert response_2.status_code == 404
