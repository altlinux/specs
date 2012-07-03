%define oname z3c.pypimirror
Name: python-module-%oname
Version: 1.0.16
Release: alt2.1
Summary: A module for building a complete or a partial PyPI mirror
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.pypimirror/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc.lockfile BeautifulSoup

%description
This package provides a mirror for the PyPI simple interface,
http://cheeseshop.python.org/simple/.

%package tests
Summary: Tests for z3c.pypimirror
Group: Development/Python
Requires: %name = %version-%release
%py_requires zc.buildout zope.testing interlude

%description tests
This package provides a mirror for the PyPI simple interface,
http://cheeseshop.python.org/simple/.

This package contains tests for z3c.pypimirror.

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

install -p -m644 src/z3c/pypimirror/util.py \
	%buildroot%python_sitelibdir/z3c/pypimirror

%files
%doc *.txt
%_bindir/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.16-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.16-alt2
- Added necessary requirements
- Excluded *.pth

* Mon Jun 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.16-alt1
- Initial build for Sisyphus

