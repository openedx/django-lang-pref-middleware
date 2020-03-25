from django.utils.deprecation import MiddlewareMixin


class LanguagePreferenceMiddleware(MiddlewareMixin):
    """
    Middleware for user language preference.

    Sets the user's language preference on the session, if it is not already set.
    """

    def process_request(self, request):
        """Set the language preference, if any, on the session."""
        user = request.user
        if user.is_authenticated and 'django_language' not in request.session:
            user_pref = self.get_user_language_preference(user)
            if user_pref:
                request.session['django_language'] = user_pref

    def get_user_language_preference(self, user):
        """
        Retrieve the given user's language preference.

        Returns None if no preference set.
        """
        raise NotImplementedError   # pragma: no cover
