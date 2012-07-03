%define oname zc.monitor
Name: python-module-%oname
Version: 0.3.0
Release: alt1
Summary: A network-accessible command-line monitoring interface
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.monitor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc.ngi zope.component zope.testing

%description
The monitor server is a server that provides a command-line interface to
request various bits of information.

The server supports an extensible set of commands. It looks up commands
as named zc.monitor.interfaces.IMonitorPlugin "utilities", as defined by
the zope.component package.

%package tests
Summary: Tests for zc.monitor
Group: Development/Python
Requires: %name = %version-%release

%description tests
The monitor server is a server that provides a command-line interface to
request various bits of information.

The server supports an extensible set of commands. It looks up commands
as named zc.monitor.interfaces.IMonitorPlugin "utilities", as defined by
the zope.component package.

This package contains tests for zc.monitor.

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
* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Version 0.3.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.2.0-alt2.1
- Rebuild with Python-2.7

* Sun Jun 26 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sun Jun 05 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.0-alt1
- Initial build for Sisyphus

