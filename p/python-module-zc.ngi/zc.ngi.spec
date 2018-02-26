%define oname zc.ngi
Name: python-module-%oname
Version: 2.0.0rel
Release: alt1
Summary: Network Gateway Interface
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.ngi/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc

%description
The Network Gateway Interface provides:

* the ability to test application networking code without use of
  sockets, threads or subprocesses
* clean separation of application code and low-level networking code
* a fairly simple inheritence free set of networking APIs
* an event-based framework that makes it easy to handle many
  simultaneous connections while still supporting an imperative
  programming style.

%package tests
Summary: Tests for Network Gateway Interface
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing manuel

%description tests
The Network Gateway Interface provides:

* the ability to test application networking code without use of
  sockets, threads or subprocesses
* clean separation of application code and low-level networking code
* a fairly simple inheritence free set of networking APIs
* an event-based framework that makes it easy to handle many
  simultaneous connections while still supporting an imperative
  programming style.

This package contains tests for Network Gateway Interface.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0rel-alt1
- Version 2.0.0 (released)

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 2.0.0a6-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0a6-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.0.0a6-alt1
- Initial build for Sisyphus

