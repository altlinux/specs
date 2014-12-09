%define mname ftw
%define oname %mname.participation
Name: python-module-%oname
Version: 1.3.7
Release: alt1.dev0.git20141208
Summary: Invite other users (registered or unregistered) to a context in plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.participation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.participation.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests
BuildPreReq: python-module-archetypes.schemaextender
BuildPreReq: python-module-ftw.upgrade
BuildPreReq: python-module-plone.app.registry
BuildPreReq: python-module-plone.formwidget.autocomplete
BuildPreReq: python-module-plone.principalsource
BuildPreReq: python-module-plone.z3cform
BuildPreReq: python-module-z3c.form
BuildPreReq: python-module-zope.testing
BuildPreReq: python-module-collective.testcaselayer
BuildPreReq: python-module-Products.PloneTestCase
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.globalrequest
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.testbrowser
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-ftw.tabbedview

%py_provides %oname
%py_requires archetypes.schemaextender ftw.upgrade plone.app.registry
%py_requires plone.formwidget.autocomplete plone.principalsource
%py_requires plone.z3cform z3c.form

%description
With ftw.participation users can invite other users to a participate in
a area (e.g. Workspace) of a Plone installation.

A privileges user is able to invite another person by going to the
invite view and entering the e-mail address of the other person. The
person receives a email with a link to the Plone installation where he /
she can log in with a existing user or create a new one. On the
invitations view he / she can now accept or deny the invitation. When
the invitation is accepted the user gets the configured privileges on
the context where he / she is invited.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing collective.testcaselayer plone.app.testing
%py_requires Products.PloneTestCase zope.globalrequest
%py_requires ftw.testbrowser ftw.testing ftw.tabbedview
%py_requires ftw.builder.testing

%description tests
With ftw.participation users can invite other users to a participate in
a area (e.g. Workspace) of a Plone installation.

A privileges user is able to invite another person by going to the
invite view and entering the e-mail address of the other person. The
person receives a email with a link to the Plone installation where he /
she can log in with a existing user or create a new one. On the
invitations view he / she can now accept or deny the invitation. When
the invitation is accepted the user gets the configured privileges on
the context where he / she is invited.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/tests

%files tests
%python_sitelibdir/%mname/*/tests

%changelog
* Tue Dec 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.7-alt1.dev0.git20141208
- Initial build for Sisyphus

