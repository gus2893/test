    // Define a custom component that mocks the Okta context
    await page.addScriptTag({
        content: `
        window.mockOktaAuth = {
            isAuthenticated: true,
            accessToken: 'mocked_access_token',
            idToken: 'mocked_id_token',
            userinfo: {
                sub: 'mocked_user_id',
                name: 'Test User',
                email: 'testuser@example.com',
            }
        };
        `
    });

    // Override the useOktaAuth hook in the app to use mocked values
    await page.addScriptTag({
        content: `
        const originalUseOktaAuth = window.OktaAuth?.useOktaAuth;

        // Create a mock implementation of useOktaAuth
        window.OktaAuth = {
            ...window.OktaAuth,
            useOktaAuth: () => {
                return {
                    authState: {
                        isAuthenticated: true,
                        accessToken: 'mocked_access_token',
                        idToken: 'mocked_id_token',
                        userinfo: {
                            sub: 'mocked_user_id',
                            name: 'Test User',
                            email: 'testuser@example.com',
                        },
                    },
                    // Other methods of useOktaAuth can be mocked if needed
                    login: jest.fn(),
                    logout: jest.fn(),
                    getIdToken: jest.fn(),
                };
            },
        };
        `
    });
