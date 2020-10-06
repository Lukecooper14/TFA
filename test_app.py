from unittest import TestCase
import app
import models


class Test(TestCase):
    def test_register(self):
        rv = self.app.get('/register', follow_redirects=True)
        self.assertEqual(rv.status_code, 200)


    def test_login(self, user, form):
        return user.password, form.password.data, user.email, form.email.data
            self.fail()


    def test_load_user(self, userid):
        if models.User.get(models.User.id == userid):
            return "Success"
            self.fail()









