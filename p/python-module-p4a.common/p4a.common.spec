%define mname p4a
%define oname %mname.common
Name: python-module-%oname
Version: 1.1.1
Release: alt1.dev0.git20130827
Summary: Reusable code-bits for Zope 3 and Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/p4a.common/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/p4a.common.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-dateutil
BuildPreReq: python-module-zope.event
BuildPreReq: python-module-zope.schema
BuildPreReq: python-module-zope.formlib
BuildPreReq: python-module-zope.app.form
BuildPreReq: python-module-zope.app.annotation
BuildPreReq: python-module-zope.annotation
BuildPreReq: python-module-zope.location
BuildPreReq: python-module-zope.app.component
BuildPreReq: python-module-zope.testing

%py_provides %oname
Requires: python-module-Zope2
%py_requires %mname zope.interface zope.event zope.schema zope.formlib
%py_requires zope.app.form zope.app.annotation zope.annotation
%py_requires zope.location zope.app.component zope.component

%description
Reusable code-bits for Zope 3 and Plone.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires zope.testing

%description tests
Reusable code-bits for Zope 3 and Plone.

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
%doc *.txt docs/*
%python_sitelibdir/%mname/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/%mname/*/test*

%files tests
%python_sitelibdir/%mname/*/test*

%changelog
* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.1-alt1.dev0.git20130827
- Initial build for Sisyphus

