%define oname repoze.mailin
Name: python-module-%oname
Version: 0.4
Release: alt1.git20110225.1.1
Summary: Map inbound e-mail onto application-defined handlers
License: BSD
Group: Development/Python
Url: https://github.com/repoze/repoze.mailin
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/repoze/repoze.mailin.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_provides %oname
%py_requires repoze zope.interface

%description
This package provides a framework for mapping inbound e-mail onto
application-defined handlers.

%package tests
Summary: Tests for repoze.mailin
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a framework for mapping inbound e-mail onto
application-defined handlers.

This package contains tests for repoze.mailin.

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
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4-alt1.git20110225.1.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20110225.1
- Added necessary requirements
- Excluded *.pth

* Fri Jun 10 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20110225
- Initial build for Sisyphus

