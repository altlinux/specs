%define oname repoze.retry
Name: python-module-%oname
Version: 1.0
Release: alt1.git20110322.1.1
Summary: WSGI middleware: retries requests after optimistic concurrency conflict errors
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.retry
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.retry.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze

%description
This package implements a WSGI middleware filter which intercepts
"retryable" exceptions and retries the WSGI request a configurable
number of times.  If the request cannot be satisfied via retries, the
exception is reraised.

%package tests
Summary: Tests for repoze.retry
Group: Development/Python
Requires: %name = %version-%release
%py_requires wsgiref

%description tests
This package implements a WSGI middleware filter which intercepts
"retryable" exceptions and retries the WSGI request a configurable
number of times.  If the request cannot be satisfied via retries, the
exception is reraised.

This package contains tests for repoze.retry.

%prep
%setup

%build
%python_build

%install
%python_install

%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%files
%doc *.txt docs/index.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.git20110322.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20110322.1
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20110322
- Initial build for Sisyphus

