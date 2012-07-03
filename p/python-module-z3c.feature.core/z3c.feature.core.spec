%define oname z3c.feature.core
Name: python-module-%oname
Version: 0.1.1
Release: alt2.1
Summary: Core Features to use with z3c.builder.core
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.feature.core/0.1.1
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires z3c.builder.core

%description
Core Features to use with z3c.builder.core

This package provides the ZBoiler Core Features.

%package tests
Summary: Tests for z3c.builder.core
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing z3c.coverage

%description tests
Core Features to use with z3c.builder.core

This package contains tests for z3c.builder.core.


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
%exclude %python_sitelibdir/*/*/*/test*

%files tests
%python_sitelibdir/*/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.1-alt2.1
- Rebuild with Python-2.7

* Fri Jul 08 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 20 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.1-alt1
- Initial build for Sisyphus

