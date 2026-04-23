def test_get_activities_returns_expected_shape(client):
    # Arrange
    expected_activity = "Chess Club"
    expected_fields = {"description", "schedule", "max_participants", "participants"}

    # Act
    response = client.get("/activities")
    payload = response.json()

    # Assert
    assert response.status_code == 200
    assert isinstance(payload, dict)
    assert expected_activity in payload

    activity = payload[expected_activity]
    assert expected_fields.issubset(activity.keys())
    assert isinstance(activity["description"], str)
    assert isinstance(activity["schedule"], str)
    assert isinstance(activity["max_participants"], int)
    assert isinstance(activity["participants"], list)
