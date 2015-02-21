%define mname ftw.notification
%define oname %mname.email
Name: python-module-%oname
Version: 2.0.10
Release: alt1.dev0.git20141107
Summary: Send edit-notifications by email
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.notification.email/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.notification.email.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-StoneageHTML
BuildPreReq: python-module-BeautifulSoup
BuildPreReq: python-module-ftw.journal
BuildPreReq: python-module-ftw.notification.base
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-zope.sendmail
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-zope.annotation

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname stoneagehtml BeautifulSoup ftw.journal zope.sendmail
%py_requires ftw.notification.base Products.CMFPlone zope.publisher
%py_requires zope.component zope.i18nmessageid zope.i18n zope.event
%py_requires zope.interface

%description
This package is an extension for ftw.notification.base providing email
notification after editing a content.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing ftw.builder.testing ftw.testing
%py_requires zope.configuration zope.annotation

%description tests
This package is an extension for ftw.notification.base providing email
notification after editing a content.

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
%python_sitelibdir/ftw/notification/email
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/ftw/notification/email/test*

%files tests
%python_sitelibdir/ftw/notification/email/test*

%changelog
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.10-alt1.dev0.git20141107
- Initial build for Sisyphus

