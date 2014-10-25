%define mname collective.js
%define oname %mname.jqueryui
Name: python-module-%oname
Version: 1.10.5
Release: alt1.dev0.git20140404
Summary: JQueryUI ready for Plone
License: GPL
Group: Development/Python
Url: https://pypi.python.org/pypi/collective.js.jqueryui/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/collective/collective.js.jqueryui.git
Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-plone.app.jquery python-module-nose

%py_provides %oname
%py_requires %mname plone.app.jquery

%description
Integration of jQueryUI in Plone 4.3.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Integration of jQueryUI in Plone 4.3.

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
nosetests

%files
%doc *.rst docs/*
%python_sitelibdir/collective/js/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/collective/js/*/tests.*

%files tests
%python_sitelibdir/collective/js/*/tests.*

%changelog
* Sat Oct 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.10.5-alt1.dev0.git20140404
- Initial build for Sisyphus

