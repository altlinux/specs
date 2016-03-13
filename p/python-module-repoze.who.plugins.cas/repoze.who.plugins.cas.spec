%define oname repoze.who.plugins.cas

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt2.1
Summary: CAS plugin for repoze.who by Makina Corpus
License: BSD
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.who.plugins.cas/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires repoze.who.plugins repoze.who zope.interface

%description
repoze.who.plugins.cas is a plugin for the repoze.who framework enabling
straightforward "cassification" (i.e.: makings each of your applications
part of the SSO mecanism) of all applications that can be deployed
through Python Paste.

It currently supports CAS 3.0, although it mays be used with others
versions of CAS (yet, no compatiblity is ensured as it has only been
tested with CAS 3.0).

%package -n python3-module-%oname
Summary: CAS plugin for repoze.who by Makina Corpus
Group: Development/Python3
%py3_requires repoze.who.plugins repoze.who zope.interface

%description -n python3-module-%oname
repoze.who.plugins.cas is a plugin for the repoze.who framework enabling
straightforward "cassification" (i.e.: makings each of your applications
part of the SSO mecanism) of all applications that can be deployed
through Python Paste.

It currently supports CAS 3.0, although it mays be used with others
versions of CAS (yet, no compatiblity is ensured as it has only been
tested with CAS 3.0).

%package -n python3-module-%oname-tests
Summary: Tests for repoze.who.plugins.cas
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing paste.deploy

%description -n python3-module-%oname-tests
repoze.who.plugins.cas is a plugin for the repoze.who framework enabling
straightforward "cassification" (i.e.: makings each of your applications
part of the SSO mecanism) of all applications that can be deployed
through Python Paste.

It currently supports CAS 3.0, although it mays be used with others
versions of CAS (yet, no compatiblity is ensured as it has only been
tested with CAS 3.0).

This package contains tests for repoze.who.plugins.cas.

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
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.2-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jul 31 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt2
- Added module for Python 3

* Mon Sep 23 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1
- Version 0.2.2

* Thu Apr 04 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1
- Version 0.1.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt1.1
- Rebuild with Python-2.7

* Fri Jul 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

