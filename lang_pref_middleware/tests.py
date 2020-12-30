import uuid
from django.test import TestCase
from django.test.client import RequestFactory
from django.contrib.auth.models import User
from django.contrib.sessions.middleware import SessionMiddleware
from lang_pref_middleware.middleware import LanguagePreferenceMiddleware


class LangPrefMiddlewareTestCaseMixin():
    middleware_class = None

    def setUp(self):
        # pylint: disable=not-callable
        self.middleware = self.middleware_class()
        self.session_middleware = SessionMiddleware()
        self.user = self.get_user()
        self.request = RequestFactory().get('/somewhere')
        self.request.user = self.user
        self.session_middleware.process_request(self.request)

    def get_user(self):
        raise NotImplementedError

    def set_user_language_preference(self, user, language):
        raise NotImplementedError

    def test_no_language_set_in_session_or_prefs(self):
        """
        If no language set in session or user preferences, no language
        should be set in the session.
        """
        self.middleware.process_request(self.request)
        self.assertNotIn('django_language', self.request.session)

    def test_language_in_user_prefs(self):
        """
        If user has a preferred language set, and no language is already
        set on the session, the user's preferred language should be set
        on the session.
        """
        self.set_user_language_preference(self.user, 'eo')
        self.middleware.process_request(self.request)
        self.assertEqual(self.request.session['django_language'], 'eo')

    def test_language_in_session(self):
        """
        If the session already has a language set, it should not be changed
        by the middleware.
        """
        self.request.session['django_language'] = 'en'
        self.set_user_language_preference(self.user, 'eo')
        self.middleware.process_request(self.request)

        self.assertEqual(self.request.session['django_language'], 'en')


class DummyLanguagePreferenceMiddleware(LanguagePreferenceMiddleware):
    """
    Simplified implementation of LanguagePreferenceMiddleware.

    This should not be used for any purpose outside of testing.
    """

    def __init__(self):
        self._cache = {}
        super().__init__()

    def get_user_language_preference(self, user):
        return self._cache.get(user, None)


class LangPrefMiddlewareTests(LangPrefMiddlewareTestCaseMixin, TestCase):
    middleware_class = DummyLanguagePreferenceMiddleware

    def get_user(self):
        username = uuid.uuid4().hex[0:20]
        return User.objects.create_user(username)

    def set_user_language_preference(self, user, language):
        # pylint: disable=protected-access
        self.middleware._cache[user] = language
