%define oname repoze.accelerator
Name: python-module-%oname
Version: 0.1
Release: alt1.git20110302.1.1
Summary: WSGI middleware that acts as a caching accelerator
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.accelerator
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.accelerator.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze paste zope.interface

%description
An caching accelerator for WSGI applications.  Intercepts responses
from downstream WSGI applications and caches responses based on
Cache-Control (and other) response header values.  Serves up cached
responses to clients thereafter based on the policy specified by the
headers.

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
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt1.git20110302.1.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20110302.1
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1.git20110302
- Initial build for Sisyphus

