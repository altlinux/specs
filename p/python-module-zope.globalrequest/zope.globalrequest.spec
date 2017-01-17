%define _unpackaged_files_terminate_build 1
# REMOVE ME (I was set for NMU) and uncomment real Release tags:
Release: alt1
%define oname zope.globalrequest

%def_with python3

Name: python-module-%oname
Version: 1.3
#Release: alt3.1
Summary: Global way of retrieving the currently active request
License: ZPL
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.globalrequest/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source0: https://pypi.python.org/packages/b4/20/672bf145ad76cad96cb237323f9bf25b4baebc61f283d2b34f3fb27a910a/%{oname}-%{version}.tar.gz

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope zope.interface

%description
This package provides a global way to retrieve the currently active
request object in a zope-based web framework.

%package -n python3-module-%oname
Summary: Global way of retrieving the currently active request
Group: Development/Python3
%py3_requires zope zope.interface

%description -n python3-module-%oname
This package provides a global way to retrieve the currently active
request object in a zope-based web framework.

%package -n python3-module-%oname-tests
Summary: Tests for zope.globalrequest
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing zope.configuration zope.app.publisher
%py3_requires zope.app.securitypolicy zope.app.testing
%py3_requires zope.app.zcmlfiles zope.testbrowser

%description -n python3-module-%oname-tests
This package provides a global way to retrieve the currently active
request object in a zope-based web framework.

This package contains tests for zope.globalrequest.

%package tests
Summary: Tests for zope.globalrequest
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing zope.configuration zope.app.publisher
%py_requires zope.app.securitypolicy zope.app.testing
%py_requires zope.app.zcmlfiles zope.testbrowser

%description tests
This package provides a global way to retrieve the currently active
request object in a zope-based web framework.

This package contains tests for zope.globalrequest.

%prep
%setup -q -n %{oname}-%{version}

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
%if "%python_sitelibdir_noarch" != "%python_sitelibdir"
install -d %buildroot%python_sitelibdir
mv %buildroot%python_sitelibdir_noarch/* \
	%buildroot%python_sitelibdir/
%endif

%if_with python3
pushd ../python3
%python3_install
popd
%if "%python3_sitelibdir_noarch" != "%python3_sitelibdir"
install -d %buildroot%python3_sitelibdir
mv %buildroot%python3_sitelibdir_noarch/* \
	%buildroot%python3_sitelibdir/
%endif
%endif

%files
%doc PKG-INFO README.rst CHANGES.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/*test*

%files tests
%python_sitelibdir/*/*/*test*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO README.rst CHANGES.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*test*
%exclude %python3_sitelibdir/*/*/*/*test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*test*
%python3_sitelibdir/*/*/*/*test*
%endif

%changelog
* Tue Jan 17 2017 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1
- automated PyPI update

* Mon Jun 06 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt3.1.1
- (AUTO) subst_x86_64.

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Jul 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0-alt1
- Initial build for Sisyphus

