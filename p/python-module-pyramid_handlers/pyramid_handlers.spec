%define oname pyramid_handlers
Name: python-module-%oname
Version: 0.4
Release: alt1
Summary: Pyramid handlers emulate Pylons 1 controllers
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_handlers/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-distribute

%py_requires pyramid pyramid_zcml

%description
pyramid_handlers is a package which allows Pyramid to largely emulate
the functionality of Pylons 1 "controllers". Handlers are a synthesis of
Pyramid url dispatch and method introspection of a view class that makes
it easier to create bundles of view logic which reacts to particular
route patterns.

%package tests
Summary: Tests for pyramid_handlers
Group: Development/Python
Requires: %name = %version-%release
%py_requires sphinx docutils repoze.sphinx.autointerface

%description tests
pyramid_handlers is a package which allows Pyramid to largely emulate
the functionality of Pylons 1 "controllers". Handlers are a synthesis of
Pyramid url dispatch and method introspection of a view class that makes
it easier to create bundles of view logic which reacts to particular
route patterns.

This package contains tests for pyramid_handlers.

%prep
%setup

%build
%python_build

%install
%python_install

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%changelog
* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Version 0.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

