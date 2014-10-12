%define oname repoze.zope2

%def_disable check

Name: python-module-%oname
Version: 1.0.3
Release: alt1
Summary: Zope2 via WSGI and Paste
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/repoze.zope2/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-module-setuptools-tests python-module-Zope2-tests
BuildPreReq: python-module-PasteScript python-module-WSGIUtils
BuildPreReq: python-module-repoze.obob python-module-PasteDeploy
BuildPreReq: python-module-repoze.tm
BuildPreReq: python-module-repoze.retry
BuildPreReq: python-module-repoze.vhm
BuildPreReq: python-module-repoze.errorlog
BuildPreReq: python-module-zope.app.testing
BuildPreReq: python-module-zope.component-tests
BuildPreReq: python-module-zope.password-tests
BuildPreReq: python-module-zope.traversing-tests
BuildPreReq: python-module-zope.security-tests
BuildPreReq: python-module-zope.server

%py_provides %oname
Requires: python-module-Zope2
%py_requires repoze paste.script repoze.obob repoze.tm repoze.retry
%py_requires repoze.vhm repoze.errorlog paste.deploy

%description
repoze.zope2 is a decomposition of the Zope 2 appserver publication
machinery (ZPublisher) into a WSGI application component. It relies on
separately-distributed middleware pieces to perform some of the features
previously handled by ZPublisher and other parts of Zope 2.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
repoze.zope2 is a decomposition of the Zope 2 appserver publication
machinery (ZPublisher) into a WSGI application component. It relies on
separately-distributed middleware pieces to perform some of the features
previously handled by ZPublisher and other parts of Zope 2.

This package contains tests for %oname.

%prep
%setup

%build
%python_build_debug

%install
%python_install

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

pushd %buildroot%_bindir
mv addzope2user addzope2user.repoze
popd

%check
python setup.py test

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/repoze/*
%python_sitelibdir/*.egg-info
%exclude %python_sitelibdir/repoze/*/tests
%exclude %python_sitelibdir/repoze/*/*/testrunner.*

%files tests
%python_sitelibdir/repoze/*/tests
%python_sitelibdir/repoze/*/*/testrunner.*

%changelog
* Sun Oct 12 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.3-alt1
- Initial build for Sisyphus

