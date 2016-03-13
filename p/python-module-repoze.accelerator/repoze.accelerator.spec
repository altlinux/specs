%define oname repoze.accelerator

%def_with python3

Name: python-module-%oname
Version: 0.1
Release: alt2.git20120330.1
Summary: WSGI middleware that acts as a caching accelerator
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.accelerator
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.accelerator.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires repoze paste zope.interface

%description
An caching accelerator for WSGI applications.  Intercepts responses
from downstream WSGI applications and caches responses based on
Cache-Control (and other) response header values.  Serves up cached
responses to clients thereafter based on the policy specified by the
headers.

%package -n python3-module-%oname
Summary: WSGI middleware that acts as a caching accelerator
Group: Development/Python3
%py3_requires repoze paste zope.interface

%description -n python3-module-%oname
An caching accelerator for WSGI applications.  Intercepts responses
from downstream WSGI applications and caches responses based on
Cache-Control (and other) response header values.  Serves up cached
responses to clients thereafter based on the policy specified by the
headers.

%package -n python3-module-%oname-tests
Summary: Tests for repoze.accelerator
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
An caching accelerator for WSGI applications.  Intercepts responses
from downstream WSGI applications and caches responses based on
Cache-Control (and other) response header values.  Serves up cached
responses to clients thereafter based on the policy specified by the
headers.

This package contains tests for repoze.accelerator.

%package tests
Summary: Tests for repoze.accelerator
Group: Development/Python
Requires: %name = %version-%release

%description tests
An caching accelerator for WSGI applications.  Intercepts responses
from downstream WSGI applications and caches responses based on
Cache-Control (and other) response header values.  Serves up cached
responses to clients thereafter based on the policy specified by the
headers.

This package contains tests for repoze.accelerator.

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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1-alt2.git20120330.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 28 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2.git20120330
- Added module for Python 3

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20120330
- New snapshot

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.git20110302.1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20110302.1
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20110302
- Initial build for Sisyphus

