%define oname chameleon

%def_with python3

Name: python-module-%oname.html
Version: 1.0.b4
Release: alt2.bzr20090520.1
Summary: Dynamic HTML template compiler with XSS language support
License: BSD
Group: Development/Python
Url: http://chameleon.repoze.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# bzr branch lp:chameleon.html
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires chameleon repoze.cssutils zope.interface
%py_requires zope.component

%description
This package implements a template compiler for dynamic HTML
documents. In particular, it supports the XSS rule language which is
used to associate elements with dynamic content.

%package -n python3-module-%oname.html
Summary: Dynamic HTML template compiler with XSS language support
Group: Development/Python3
%py3_requires chameleon repoze.cssutils zope.interface
%py3_requires zope.component

%description -n python3-module-%oname.html
This package implements a template compiler for dynamic HTML
documents. In particular, it supports the XSS rule language which is
used to associate elements with dynamic content.

%package -n python3-module-%oname.html-tests
Summary: Tests for Dynamic HTML template compiler
Group: Development/Python3
Requires: python3-module-%oname.html = %version-%release
%py3_requires zope.testing zope.component.testing zope.configuration

%description -n python3-module-%oname.html-tests
This package implements a template compiler for dynamic HTML
documents. In particular, it supports the XSS rule language which is
used to associate elements with dynamic content.

This package contains tests for Dynamic HTML template compiler.

%package tests
Summary: Tests for Dynamic HTML template compiler
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.component.testing zope.configuration

%description tests
This package implements a template compiler for dynamic HTML
documents. In particular, it supports the XSS rule language which is
used to associate elements with dynamic content.

This package contains tests for Dynamic HTML template compiler.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/*/tests

%files tests
%python_sitelibdir/%oname/*/tests

%if_with python3
%files -n python3-module-%oname.html
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/*/tests

%files -n python3-module-%oname.html-tests
%python3_sitelibdir/%oname/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.b4-alt2.bzr20090520.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.b4-alt2.bzr20090520
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.b4-alt1.bzr20090520.1
- Rebuild with Python-2.7

* Mon May 16 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.b4-alt1.bzr20090520
- Initial build for Sisyphus

