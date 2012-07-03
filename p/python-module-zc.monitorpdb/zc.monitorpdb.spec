%define oname zc.monitorpdb
Name: python-module-%oname
Version: 1.0.0
Release: alt2.1
Summary: zc.monitor plugin to debug running processes
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.monitorpdb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc zc.monitor

%description
zc.montorpdb is a small plugin for the (very) lightweight zc.monitor
system. It allows a user to telnet to a monitor port and invoke a Python
debugger (PDB) prompt.

%package tests
Summary: Tests for zc.monitorpdb
Group: Development/Python
Requires: %name = %version-%release

%description tests
zc.montorpdb is a small plugin for the (very) lightweight zc.monitor
system. It allows a user to telnet to a monitor port and invoke a Python
debugger (PDB) prompt.

This package contains tests for zc.monitorpdb.

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
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%changelog
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue Jun 07 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

