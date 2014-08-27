Django Language Preference Middleware
=====================================

This repo contains basic middleware that retrieves a user's language 
preference and sets it on the request session.

Usage
=====
Subclass `LanguagePreferenceMiddleware` and override the
`get_user_language_preference` method.

Your new middleware should be
tested by including `LangPrefMiddlewareTestCaseMixin` in your test case and
overriding the `middleware_class`, `get_user`, and 
`set_user_language_preference` attributes.

Testing
=======

    $ make validate


How to Contribute
-----------------

Contributions are very welcome, but for legal reasons, you must submit a signed
[individual contributor's agreement](http://code.edx.org/individual-contributor-agreement.pdf)
before we can accept your contribution. See our
[CONTRIBUTING](https://github.com/edx/edx-platform/blob/master/CONTRIBUTING.rst)
file for more information -- it also contains guidelines for how to maintain
high code quality, which will make your contribution more likely to be accepted.
