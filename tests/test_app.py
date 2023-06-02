def test_get_home(web_client):
    response = web_client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello, world!"

def test_get_goodbye(web_client):
    response = web_client.get("/goodbye")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Farewell, to all the earthly remains~"
