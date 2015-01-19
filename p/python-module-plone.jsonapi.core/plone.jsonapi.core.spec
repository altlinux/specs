%define mname plone.jsonapi
%define oname %mname.core
Name: python-module-%oname
Version: 0.4
Release: alt1.git20140304
Summary: An extensible Plone JSON API Framework
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/plone.jsonapi.core/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/plone.jsonapi.core.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-unittest2
BuildPreReq: python-module-werkzeug python-module-simplejson
BuildPreReq: python-module-plone.app.testing
BuildPreReq: python-module-zope.publisher
BuildPreReq: python-module-zope.configuration

%py_provides %oname
Requires: python-module-%mname = %EVR
Requires: python-module-Zope2
%py_requires werkzeug simplejson zope.publisher zope.interface
%py_requires zope.component

%description
This Package allows Users to expose content information via JSON.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR
%py_requires plone.app.testing unittest2 zope.configuration

%description tests
This Package allows Users to expose content information via JSON.

This package contains tests for %oname.

%package -n python-module-%mname
Summary: Core files of %mname
Group: Development/Python
%py_provides %mname
%py_requires plone

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

install -p -m644 src/plone/jsonapi/__init__.py \
	%buildroot%python_sitelibdir/plone/jsonapi/

%check
python setup.py test

%files
%doc *.rst
%python_sitelibdir/plone/jsonapi/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/plone/jsonapi/*/tests
%exclude %python_sitelibdir/plone/jsonapi/__init__.py*

%files tests
%python_sitelibdir/plone/jsonapi/*/tests

%files -n python-module-%mname
%dir %python_sitelibdir/plone/jsonapi
%python_sitelibdir/plone/jsonapi/__init__.py*

%changelog
* Mon Jan 19 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20140304
- Initial build for Sisyphus

