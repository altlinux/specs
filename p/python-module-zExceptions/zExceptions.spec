%define oname zExceptions
Name: python-module-%oname
Version: 2.13.0
Release: alt1.1
Summary: zExceptions contains common exceptions used in Zope2
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zExceptions/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%description
zExceptions contains common exceptions and helper functions related to
exceptions as used in Zope 2.

%package tests
Summary: Tests for zExceptions
Group: Development/Python
Requires: %name = %version-%release

%description tests
zExceptions contains common exceptions and helper functions related to
exceptions as used in Zope 2.

This package contains tests for zExceptions.

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
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.13.0-alt1.1
- Rebuild with Python-2.7

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.13.0-alt1
- Initial build for Sisyphus

