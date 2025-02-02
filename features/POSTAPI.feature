Feature: DummyJSON - LoginUser_GetTokens

    Scenario: Get the access token for the user

        Given User Details
        When we execute the POST method to generate the access token
        Then access token and refresh token is generated.