%define oname z3c.testsummarizer
Name: python-module-%oname
Version: 2.0
Release: alt2.1
Summary: Checks a pipermail archive for recent messages and creates a summary
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.testsummarizer/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%description
Script that checks a pipermail archive for recent messages, parses them
according to a test result format and creates a summary.

%package tests
Summary: Tests for z3c.testsummarizer
Group: Development/Python
Requires: %name = %version-%release

%description tests
Script that checks a pipermail archive for recent messages, parses them
according to a test result format and creates a summary.

This package contains tests for z3c.testsummarizer.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt2
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0-alt1
- Initial build for Sisyphus

