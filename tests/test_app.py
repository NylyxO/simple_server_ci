def test_get_home(web_client):
    response = web_client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello, world!"

def test_post_home(web_client):
    response = web_client.post("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello, world!"
