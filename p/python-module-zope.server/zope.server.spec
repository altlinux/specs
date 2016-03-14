%define oname zope.server

%def_with python3

Name: python-module-%oname
Version: 3.9.0
Release: alt2.1
Summary: Zope Server (Web and FTP)
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.server/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zope zope.interface zope.publisher zope.security

%description
This package contains generic base classes for channel-based servers,
the servers themselves and helper objects, such as tasks and requests.

%package -n python3-module-%oname
Summary: Zope Server (Web and FTP)
Group: Development/Python3
%py3_requires zope zope.interface zope.publisher zope.security

%description -n python3-module-%oname
This package contains generic base classes for channel-based servers,
the servers themselves and helper objects, such as tasks and requests.

%package -n python3-module-%oname-tests
Summary: Tests for zope.server
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.i18n zope.component

%description -n python3-module-%oname-tests
This package contains generic base classes for channel-based servers,
the servers themselves and helper objects, such as tasks and requests.

This package contains tests for zope.server.

%package tests
Summary: Tests for zope.server
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.i18n zope.component

%description tests
This package contains generic base classes for channel-based servers,
the servers themselves and helper objects, such as tasks and requests.

This package contains tests for zope.server.

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
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/*/tests

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/*/tests
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.9.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt2
- Added module for Python 3

* Wed Apr 10 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.9.0-alt1
- Version 3.9.0

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.5-alt1
- Version 3.8.5

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.8.3-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt2
- Added necessary requirements
- Excluded *.pth

* Fri May 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.8.3-alt1
- Initial build for Sisyphus

