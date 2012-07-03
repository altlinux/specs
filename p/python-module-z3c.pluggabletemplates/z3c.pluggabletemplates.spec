%define oname z3c.pluggabletemplates
Name: python-module-%oname
Version: 0.2
Release: alt2.1
Summary: Seperation of view code from skin templates like z3c.viewtemplate
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.pluggabletemplates/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%description
This package does two things. First, it does everything z3c.viewtemplate
does -- seperate the view code layer from the template skin layer.
Second, it allows an unlimited number of templates to be plugged into
any view class.

%package tests
Summary: Tests for z3c.pluggabletemplates
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package does two things. First, it does everything z3c.viewtemplate
does -- seperate the view code layer from the template skin layer.
Second, it allows an unlimited number of templates to be plugged into
any view class.

This package contains tests for z3c.pluggabletemplates.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt2
- Excluded *.pth

* Sat Jun 04 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2-alt1
- Initial build for Sisyphus

