%define oname pyramid_handlers

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt2
Summary: Pyramid handlers emulate Pylons 1 controllers
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/pyramid_handlers/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires pyramid pyramid_zcml

%description
pyramid_handlers is a package which allows Pyramid to largely emulate
the functionality of Pylons 1 "controllers". Handlers are a synthesis of
Pyramid url dispatch and method introspection of a view class that makes
it easier to create bundles of view logic which reacts to particular
route patterns.

%package -n python3-module-%oname
Summary: Pyramid handlers emulate Pylons 1 controllers
Group: Development/Python3
%py3_requires pyramid pyramid_zcml

%description -n python3-module-%oname
pyramid_handlers is a package which allows Pyramid to largely emulate
the functionality of Pylons 1 "controllers". Handlers are a synthesis of
Pyramid url dispatch and method introspection of a view class that makes
it easier to create bundles of view logic which reacts to particular
route patterns.

%package -n python3-module-%oname-tests
Summary: Tests for pyramid_handlers
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires sphinx docutils repoze.sphinx.autointerface

%description -n python3-module-%oname-tests
pyramid_handlers is a package which allows Pyramid to largely emulate
the functionality of Pylons 1 "controllers". Handlers are a synthesis of
Pyramid url dispatch and method introspection of a view class that makes
it easier to create bundles of view logic which reacts to particular
route patterns.

This package contains tests for pyramid_handlers.

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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests.*

%files tests
%python_sitelibdir/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests.*
%exclude %python3_sitelibdir/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests.*
%python3_sitelibdir/*/*/tests.*
%endif

%changelog
* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt2
- Added module for Python 3

* Tue Apr 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1
- Version 0.5

* Mon Dec 12 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1
- Version 0.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.1
- Rebuild with Python-2.7

* Tue Jul 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

