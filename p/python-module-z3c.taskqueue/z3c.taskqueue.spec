%define oname z3c.taskqueue
Name: python-module-%oname
Version: 0.1.alpha4
Release: alt2.1
Summary: Task queue service
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.taskqueue/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope.interface zope.component zope.schema
%py_requires zope.configuration zope.container zc.queue
%py_requires zope.app.publication

%description
Task queue service.

%package tests
Summary: Tests for z3c.taskqueue
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
Task queue service.

This package contains tests for z3c.taskqueue.

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
%doc *.txt docs/*
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.1.alpha4-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.alpha4-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.alpha4-alt1
- Initial build for Sisyphus

