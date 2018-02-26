%define oname z3c.csvvocabulary
Name: python-module-%oname
Version: 1.1.0
Release: alt2.1
Summary: A package to create vocabularies based on CSV files
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.csvvocabulary/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.i18nmessageid zope.schema

%description
This package provides a very simple vocabulary implementation using CSV
files. The advantage of CSV files is that they provide an external point
to specify data, which allows a non-developer to adjust the data
themselves.

%package tests
Summary: Tests for z3c.csvvocabulary
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
This package provides a very simple vocabulary implementation using CSV
files. The advantage of CSV files is that they provide an external point
to specify data, which allows a non-developer to adjust the data
themselves.

This package contains tests for z3c.csvvocabulary.

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
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.1.0-alt2.1
- Rebuild with Python-2.7

* Thu Jun 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Wed Jun 01 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1
- Initial build for Sisyphus

