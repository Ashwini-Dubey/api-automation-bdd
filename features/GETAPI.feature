Feature: DummyJSON - GetCurrentAuthUser

    Scenario: Get the CurrentAuthUser with accessToken

        Given accessToken
        When we execute the GET method to parse the CurrentAuthUser
        Then CurrentAuthUser details are parsed