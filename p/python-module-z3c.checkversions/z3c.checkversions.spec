%define oname z3c.checkversions
Name: python-module-%oname
Version: 0.4.1
Release: alt2.1
Summary: Find newer package versions on PyPI
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.checkversions/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%description
Find newer versions of your installed Python packages, or newer versions
of packages in a buildout file.

This package provides a console script named checkversions.

%package tests
Summary: Tests for z3c.checkversions
Group: Development/Python
Requires: %name = %version-%release
%py_requires zc.buildout

%description tests
Find newer versions of your installed Python packages, or newer versions
of packages in a buildout file.

This package contains tests for z3c.checkversions.

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
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.4.1-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri Jun 03 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Initial build for Sisyphus

