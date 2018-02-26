%define oname z3c.quickentry
Name: python-module-%oname
Version: 0.1
Release: alt2.1
Summary: Allows a user to efficiently specify multiple values in one larger text block
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.quickentry/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%description
The quick entry processor allows a user to efficiently specify multiple
values in one larger text block. The processor uses plugins to
dynamically define the commands to handle.

This type of input is not aimed at the average user, but at power users
and users that can be trained. The syntax is purposefully minimized to
maximize the input speed. This method of entry has been verified in a
real life setting.

%package tests
Summary: Tests for z3c.quickentry
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.app.testing

%description tests
The quick entry processor allows a user to efficiently specify multiple
values in one larger text block. The processor uses plugins to
dynamically define the commands to handle.

This type of input is not aimed at the average user, but at power users
and users that can be trained. The syntax is purposefully minimized to
maximize the input speed. This method of entry has been verified in a
real life setting.

This package contains tests for z3c.quickentry.

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
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt2
- Added necessary requirements
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1-alt1
- Initial build for Sisyphus

