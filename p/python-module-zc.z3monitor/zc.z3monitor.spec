%define oname zc.z3monitor
Name: python-module-%oname
Version: 0.7.0
Release: alt2.1
Summary: A network-accessible command-line interface to monitor a Zope 3 process
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.z3monitor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-distribute

%py_requires zc zc.monitor ZODB3 zope.component zope.publisher
%py_requires zope.app.appsetup zope.testing

%description
The Zope 3 monitor server is a server that runs in a Zope 3 process and
that provides a command-line interface to request various bits of
information. It is based on zc.monitor, which is itself based on zc.ngi,
so we can use the zc.ngi testing infrastructure to demonstrate it.

This package provides several Zope 3 and ZODB monitoring and
introspection tools that work within the zc.monitor server. These are
demonstrated below.

This package also supports starting a monitor using ZConfig, and
provides a default configure.zcml for registering plugins.

%package tests
Summary: Tests for zc.z3monitor
Group: Development/Python
Requires: %name = %version-%release

%description tests
The Zope 3 monitor server is a server that runs in a Zope 3 process and
that provides a command-line interface to request various bits of
information. It is based on zc.monitor, which is itself based on zc.ngi,
so we can use the zc.ngi testing infrastructure to demonstrate it.

This package provides several Zope 3 and ZODB monitoring and
introspection tools that work within the zc.monitor server. These are
demonstrated below.

This package also supports starting a monitor using ZConfig, and
provides a default configure.zcml for registering plugins.

This package contains tests for zc.z3monitor.

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
* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

