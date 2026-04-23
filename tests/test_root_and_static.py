def test_root_redirects_to_static_index(client):
    # Arrange
    expected_location = "/static/index.html"

    # Act
    response = client.get("/", follow_redirects=False)

    # Assert
    assert response.status_code == 307
    assert response.headers["location"] == expected_location


def test_static_index_is_served(client):
    # Arrange
    expected_text = "Mergington High School"

    # Act
    response = client.get("/static/index.html")

    # Assert
    assert response.status_code == 200
    assert "text/html" in response.headers["content-type"]
    assert expected_text in response.text


def test_static_css_and_js_are_served(client):
    # Arrange
    css_path = "/static/styles.css"
    js_path = "/static/app.js"

    # Act
    css_response = client.get(css_path)
    js_response = client.get(js_path)

    # Assert
    assert css_response.status_code == 200
    assert "text/css" in css_response.headers["content-type"]
    assert js_response.status_code == 200
    assert "javascript" in js_response.headers["content-type"]
