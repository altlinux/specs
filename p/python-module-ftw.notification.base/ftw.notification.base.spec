%define mname ftw.notification
%define oname %mname.base
Name: python-module-%oname
Version: 1.2.7
Release: alt1.dev0.git20141107
Summary: Send notifications when editing a plone content
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.notification.base/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.notification.base.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-ftw.table
BuildPreReq: python-module-plone.principalsource
BuildPreReq: python-module-ftw.testing
BuildPreReq: python-module-ftw.builder-tests
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-Products.CMFPlone
BuildPreReq: python-module-Products.statusmessages
BuildPreReq: python-module-plone.app.layout
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.i18n
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires ftw.table plone.principalsource Products.CMFCore zope.i18n
%py_requires Products.CMFPlone Products.statusmessages plone.app.layout
%py_requires zope.component zope.interface zope.i18nmessageid zope.event
%py_requires zope.schema

%description
This package provides a notification system for plone for sending
notifications when a content is changed.

Every edit-form is extended with a checkbox for sending a notification
after the modification on the content is done. When checked, the user
will see a form after submitting the changes, where he can select
multiple persons to be notified and add a comment.

This package does not contain the actual implementation of sending the
notification. It is designed so that the type of notification can be
replaced. Any type of notification can be implemented like this (e.g.
email, jabber, irc, physical letter).

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires ftw.testing ftw.builder.testing plone.app.testing
%py_requires zope.configuration

%description tests
This package provides a notification system for plone for sending
notifications when a content is changed.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires ftw

%description -n python-module-%mname
Core files of %mname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

install -p -m644 ftw/notification/__init__.py \
	%buildroot%python_sitelibdir/ftw/notification/

%check
python setup.py test

%files
%doc *.rst docs/*
%python_sitelibdir/ftw/notification/base
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/ftw/notification/base/test*

%files tests
%python_sitelibdir/ftw/notification/base/test*

%files -n python-module-%mname
%dir %python_sitelibdir/ftw/notification
%python_sitelibdir/ftw/notification/__init__.py*

%changelog
* Sat Feb 21 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.7-alt1.dev0.git20141107
- Initial build for Sisyphus

