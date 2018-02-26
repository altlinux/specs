%define oname repoze.session
Name: python-module-%oname
Version: 0.2
Release: alt2.1
Summary: Sessioning for web applications
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.session/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze zope.component zope.event ZODB3

%description
An HTTP sessioning system for web applications, based on code from the
faster http://agendaless.com/Members/tseaver/software/faster/ Zope 2
product. repoze.session uses ZODB as its persistence mechanism.

%package tests
Summary: Tests for repoze.session
Group: Development/Python
Requires: %name = %version-%release

%description tests
An HTTP sessioning system for web applications, based on code from the
faster http://agendaless.com/Members/tseaver/software/faster/ Zope 2
product. repoze.session uses ZODB as its persistence mechanism.

This package contains tests for repoze.session.

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
%doc *.txt docs/*.rst docs/code
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 17 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

