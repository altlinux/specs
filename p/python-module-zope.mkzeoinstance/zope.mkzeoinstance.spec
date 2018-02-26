%define oname zope.mkzeoinstance
Name: python-module-%oname
Version: 3.9.5
Release: alt1
Summary: Make standalone ZEO database server instances
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.mkzeoinstance/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope ZODB3

%description
This package provides a single script, mkzeoinstance, which creates a
standalone ZEO server instance.

%package tests
Summary: Tests for mkzeoinstance
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package provides a single script, mkzeoinstance, which creates a
standalone ZEO server instance.

This package contains tests for mkzeoinstance.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.5-alt1
- Version 3.9.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.9.4-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.4-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.4-alt1
- Initial build for Sisyphus

