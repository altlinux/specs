%define oname zope.app.server

%def_with python3

Name: python-module-%oname
Version: 3.6.0
Release: alt3.1
Summary: ZServer integration for Zope 3 Applications
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.server/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope.app zope.app.applicationcontrol zope.app.appsetup
%py_requires zope.app.publication zope.app.wsgi zope.configuration
%py_requires zope.deprecation zope.event zope.interface zope.publisher
%py_requires zope.server zope.password zope.processlifetime zdaemon
%py_requires ZConfig ZODB3

%description
This package integrates ZServer -- Zope's HTTP and FTP server -- into a
Zope 3 application setup. It also defines the script skeleton for a
classic Zope 3 application.

%package -n python3-module-%oname
Summary: ZServer integration for Zope 3 Applications
Group: Development/Python3
%py3_requires zope.app zope.app.applicationcontrol zope.app.appsetup
%py3_requires zope.app.publication zope.app.wsgi zope.configuration
%py3_requires zope.deprecation zope.event zope.interface zope.publisher
%py3_requires zope.server zope.password zope.processlifetime zdaemon
%py3_requires ZConfig ZODB3

%description -n python3-module-%oname
This package integrates ZServer -- Zope's HTTP and FTP server -- into a
Zope 3 application setup. It also defines the script skeleton for a
classic Zope 3 application.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.server
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.app.testing

%description -n python3-module-%oname-tests
This package integrates ZServer -- Zope's HTTP and FTP server -- into a
Zope 3 application setup. It also defines the script skeleton for a
classic Zope 3 application.

This package contains tests for zope.app.server.

%package tests
Summary: Tests for zope.app.server
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.app.testing

%description tests
This package integrates ZServer -- Zope's HTTP and FTP server -- into a
Zope 3 application setup. It also defines the script skeleton for a
classic Zope 3 application.

This package contains tests for zope.app.server.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build

%if_with python3
pushd ../python3
find -type f -name '*.py' -exec 2to3 -w -n '{}' +
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
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Tue May 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

