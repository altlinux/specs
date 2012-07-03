%define oname zope.applicationcontrol
Name: python-module-%oname
Version: 3.5.5
Release: alt2.1
Summary: Zope applicationcontrol
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.applicationcontrol/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zope zope.interface zope.component zope.location
%py_requires zope.security zope.traversing

%description
The application control instance can be generated upon startup of an
application built with the Zope Toolkit.

This package provides an API to retrieve runtime information. It also
provides a utility with methods for shutting down and restarting the
server.

%package tests
Summary: Tests for zope.applicationcontrol
Group: Development/Python
Requires: %name = %version-%release

%description tests
The application control instance can be generated upon startup of an
application built with the Zope Toolkit.

This package provides an API to retrieve runtime information. It also
provides a utility with methods for shutting down and restarting the
server.

This package contains tests for zope.applicationcontrol.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.5-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.5-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.5-alt1
- Initial build for Sisyphus

