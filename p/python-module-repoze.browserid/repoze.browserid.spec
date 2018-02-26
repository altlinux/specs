%define oname repoze.browserid
Name: python-module-%oname
Version: 0.3
Release: alt1.git20110222.1.1
Summary: Browser id middleware for WSGI
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.browserid
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.browserid.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze paste

%description
Browser id middleware for WSGI, loosely based on the Zope 2 concept of
browser ids, which are cookies which represent a browser, for use by
sessioning libraries.

%package tests
Summary: Tests for repoze.browserid
Group: Development/Python
Requires: %name = %version

%description tests
Browser id middleware for WSGI, loosely based on the Zope 2 concept of
browser ids, which are cookies which represent a browser, for use by
sessioning libraries.

This package contains tests for repoze.browserid.

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
%doc *.txt docs/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.3-alt1.git20110222.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110222.1
- Added necessary requirements
- Excluded *.pth

* Tue Jun 14 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3-alt1.git20110222
- Initial build for Sisyphus

