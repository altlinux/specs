%define oname zc.z3monitor

%def_with python3

Name: python-module-%oname
Version: 0.8.0
Release: alt2.1
Summary: A network-accessible command-line interface to monitor a Zope 3 process
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zc.z3monitor/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

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

%package -n python3-module-%oname
Summary: A network-accessible command-line interface to monitor a Zope 3 process
Group: Development/Python3
%py3_requires zc zc.monitor ZODB3 zope.component zope.publisher
%py3_requires zope.app.appsetup zope.testing

%description -n python3-module-%oname
The Zope 3 monitor server is a server that runs in a Zope 3 process and
that provides a command-line interface to request various bits of
information. It is based on zc.monitor, which is itself based on zc.ngi,
so we can use the zc.ngi testing infrastructure to demonstrate it.

This package provides several Zope 3 and ZODB monitoring and
introspection tools that work within the zc.monitor server. These are
demonstrated below.

This package also supports starting a monitor using ZConfig, and
provides a default configure.zcml for registering plugins.

%package -n python3-module-%oname-tests
Summary: Tests for zc.z3monitor
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
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

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install
%ifarch x86_64
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%ifarch x86_64
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/tests.*

%files tests
%python_sitelibdir/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests.*
%python3_sitelibdir/*/*/*/tests.*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt2
- Added module for Python 3

* Mon Apr 08 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.0-alt1
- Version 0.8.0

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.7.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 31 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1
- Initial build for Sisyphus

