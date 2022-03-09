import time
from subprocess import Popen
from rest_framework.test import APITestCase

class LoginTestCase(APITestCase):
    """Check login flow."""

    def setUp(self):
        self.mock_server = Popen(['python', 'login/test_server.py'])
        time.sleep(1)

    def test_login(self):
        """Test if SSO login works."""

        # Check validation
        # Without code
        url = 'http://localhost/api/login?redir=REDIRECT_URI'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 400)

        # Without redir
        url = 'http://localhost/api/login?code=TEST_CODE'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 400)

        # Try to log in with wrong code
        url = 'http://localhost/api/login?code=T_CODE&redir=REDIRECT_URI'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 400)

        # Try to log in with bad code
        url = 'http://localhost/api/login?code=BAD_TEST_CODE&redir=REDIRECT_URI&fcm_id=testfcm'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 400)

        # Try to log in with insufficient SSO privileges
        url = 'http://localhost/api/login?code=TEST_CODE_LP&redir=REDIRECT_URI&fcm_id=testfcm'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 403)

        # Try to log in
        url = 'http://localhost/api/login?code=TEST_CODE&redir=REDIRECT_URI&fcm_id=testfcm'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data['profile']['name'], "First Name Last Name")

        
        # Test logout
        url = 'http://localhost/api/logout'
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, 200)