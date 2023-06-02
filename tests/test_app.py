def test_get_home(web_client):
    response = web_client.get("/")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Hello, world!"

def test_get_goodbye(web_client):
    response = web_client.get("/goodbye")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "Farewell, to all the earthly remains~"

def test_get_specific_message(web_client):
    response = web_client.get("/message?message=I can drink, I can feast. There's beauty in your beast.")
    assert response.status_code == 200
    assert response.data.decode("utf-8") == "I can drink, I can feast. There's beauty in your beast."