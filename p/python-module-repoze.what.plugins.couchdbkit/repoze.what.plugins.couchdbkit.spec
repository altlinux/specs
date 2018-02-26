%define oname repoze.what.plugins.couchdbkit
Name: python-module-%oname
Version: 0.2
Release: alt2.1
Summary: repoze.what plugin for couchdbkit
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/repoze.what.plugins.couchdbkit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires repoze.what.plugins couchdbkit repoze.what simplejson

%description
repoze.what plugin for couchdbkit.

%package tests
Summary: Tests for repoze.what.plugins.couchdbkit
Group: Development/Python
Requires: %name = %version-%release

%description tests
repoze.what plugin for couchdbkit.

This package contains tests for repoze.what.plugins.couchdbkit.

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
%exclude %python_sitelibdir/*/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Thu Jun 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 15 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

