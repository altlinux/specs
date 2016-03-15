%define oname repoze.retry

%def_with python3

Name: python-module-%oname
Version: 1.3
Release: alt2.git20131015.1
Summary: WSGI middleware: retries requests after optimistic concurrency conflict errors
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.retry
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.retry.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze

%description
This package implements a WSGI middleware filter which intercepts
"retryable" exceptions and retries the WSGI request a configurable
number of times.  If the request cannot be satisfied via retries, the
exception is reraised.

%package -n python3-module-%oname
Summary: WSGI middleware: retries requests after optimistic concurrency conflict errors
Group: Development/Python3
%py3_requires repoze

%description -n python3-module-%oname
This package implements a WSGI middleware filter which intercepts
"retryable" exceptions and retries the WSGI request a configurable
number of times.  If the request cannot be satisfied via retries, the
exception is reraised.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.retry
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires wsgiref

%description -n python3-module-%oname-tests
This package implements a WSGI middleware filter which intercepts
"retryable" exceptions and retries the WSGI request a configurable
number of times.  If the request cannot be satisfied via retries, the
exception is reraised.

This package contains tests for repoze.retry.

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
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt docs/index.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt docs/index.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.3-alt2.git20131015.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt2.git20131015
- Added module for Python 3

* Mon Dec 02 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20131015
- New snapshot

* Tue Sep 24 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3-alt1.git20130604
- Version 1.3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.2-alt1.git20120712
- Version 1.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt1.git20110322.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20110322.1
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1.git20110322
- Initial build for Sisyphus

