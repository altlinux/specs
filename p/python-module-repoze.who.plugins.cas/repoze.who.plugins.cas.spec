%define oname repoze.who.plugins.cas
Name: python-module-%oname
Version: 0.1.1
Release: alt1.1
Summary: CAS plugin for repoze.who by Makina Corpus
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.who.plugins.cas/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.who.plugins

%description
repoze.who.plugins.cas is a plugin for the repoze.who framework enabling
straightforward "cassification" (i.e.: makings each of your applications
part of the SSO mecanism) of all applications that can be deployed
through Python Paste.

It currently supports CAS 3.0, although it mays be used with others
versions of CAS (yet, no compatiblity is ensured as it has only been
tested with CAS 3.0).

%package tests
Summary: Tests for repoze.who.plugins.cas
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing paste.deploy

%description tests
repoze.who.plugins.cas is a plugin for the repoze.who framework enabling
straightforward "cassification" (i.e.: makings each of your applications
part of the SSO mecanism) of all applications that can be deployed
through Python Paste.

It currently supports CAS 3.0, although it mays be used with others
versions of CAS (yet, no compatiblity is ensured as it has only been
tested with CAS 3.0).

This package contains tests for repoze.who.plugins.cas.

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
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

