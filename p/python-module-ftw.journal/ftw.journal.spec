%define mname ftw
%define oname %mname.journal
Name: python-module-%oname
Version: 1.2.9
Release: alt1.dev0.git20141107
Summary: Journaling infrastructure for plone
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/ftw.journal/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/4teamwork/ftw.journal.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-mocker python-module-unittest2
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.i18nmessageid
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-Products.CMFCore
BuildPreReq: python-module-plone.app.contentrules
BuildPreReq: python-module-plone.contentrules
BuildPreReq: python-module-zope.configuration
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-plone.mocktestcase

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname zope.annotation zope.component zope.event ZODB3
%py_requires zope.formlib zope.i18nmessageid zope.interface zope.schema
%py_requires Products.CMFCore plone.app.contentrules plone.contentrules

%description
Currently ftw.journal provides two adapters to store infos.

* workflow_histoy
* annotations

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.configuration plone.app.testing plone.mocktestcase

%description tests
Currently ftw.journal provides two adapters to store infos.

* workflow_histoy
* annotations

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
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Wed Dec 24 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2.9-alt1.dev0.git20141107
- Initial build for Sisyphus

