%define oname zope.sequencesort
Name: python-module-%oname
Version: 3.4.0
Release: alt2.1
Summary: Sequence Sorting
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.sequencesort/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope

%description
This package provides a very advanced sequence sorting feature.

%package tests
Summary: Tests for zope.sequencesort
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package provides a very advanced sequence sorting feature.

This package contains tests for zope.sequencesort.

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
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.4.0-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.4.0-alt1
- Initial build for Sisyphus

