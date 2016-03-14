%define oname zope.app.localpermission

%def_with python3

Name: python-module-%oname
Version: 3.7.2
Release: alt4.1
Summary: Local Persistent Permissions for zope.security
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.localpermission/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.app ZODB3 zope.component zope.i18nmessageid
%py_requires zope.interface zope.location zope.security

%description
This package implements local persistent permissions for zope.security
that can be added and registered per site.

This is a part of "Through The Web" development pattern that is not used
much by zope community and not really supported in zope framework
anymore nowadays, so it can be considered as deprecated.

%package -n python3-module-%oname
Summary: Local Persistent Permissions for zope.security
Group: Development/Python3
%py3_requires zope.app ZODB3 zope.component zope.i18nmessageid
%py3_requires zope.interface zope.location zope.security

%description -n python3-module-%oname
This package implements local persistent permissions for zope.security
that can be added and registered per site.

This is a part of "Through The Web" development pattern that is not used
much by zope community and not really supported in zope framework
anymore nowadays, so it can be considered as deprecated.

%package -n python3-module-%oname-tests
Summary: Tests for zope.app.localpermission
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
This package implements local persistent permissions for zope.security
that can be added and registered per site.

This is a part of "Through The Web" development pattern that is not used
much by zope community and not really supported in zope framework
anymore nowadays, so it can be considered as deprecated.

This package contains tests for zope.app.localpermission.

%package tests
Summary: Tests for zope.app.localpermission
Group: Development/Python
Requires: %name = %version-%release

%description tests
This package implements local persistent permissions for zope.security
that can be added and registered per site.

This is a part of "Through The Web" development pattern that is not used
much by zope community and not really supported in zope framework
anymore nowadays, so it can be considered as deprecated.

This package contains tests for zope.app.localpermission.

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
%exclude %python_sitelibdir/*/*/*/tests.*

%files tests
%python_sitelibdir/*/*/*/tests.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/*/tests.*
%exclude %python3_sitelibdir/*/*/*/*/tests.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/*/tests.*
%python3_sitelibdir/*/*/*/*/tests.*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.7.2-alt4.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt4
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.7.2-alt3.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt3
- Really added necessary requirements

* Sun Jun 19 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 23 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.7.2-alt1
- Initial build for Sisyphus

