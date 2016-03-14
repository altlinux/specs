%define oname zope.keyreference

%def_with python3

Name: python-module-%oname
Version: 4.1.0
Release: alt1.1
Summary: Zope Key References
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.keyreference/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope zope.component zope.i18nmessageid
%py_requires zope.interface zope.schema ZODB3

%description
Object references that support stable comparison and hashes.

%package -n python3-module-%oname
Summary: Zope Key References
Group: Development/Python3
%py3_requires zope zope.component zope.i18nmessageid
%py3_requires zope.interface zope.schema ZODB3

%description -n python3-module-%oname
Object references that support stable comparison and hashes.

%package -n python3-module-%oname-tests
Summary: Tests for zope.keyreference
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
Object references that support stable comparison and hashes.

This package contains tests for zope.keyreference.

%package tests
Summary: Tests for zope.keyreference
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
Object references that support stable comparison and hashes.

This package contains tests for zope.keyreference.

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
%doc *.txt *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*.pth
%exclude %python_sitelibdir/*/*/test*

%files tests
%python_sitelibdir/*/*/test*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/test*
%exclude %python3_sitelibdir/*/*/*/test*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test*
%python3_sitelibdir/*/*/*/test*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.1.0-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.1.0-alt1
- Version 4.1.0

* Mon Dec 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt4
- Version 4.0.0

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt3.a2
- Added module for Python 3

* Wed Jul 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt2.a2
- Avoid requirement on ZODB3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.0-alt1.a2
- Version 4.0.0a2

* Wed Dec 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.4-alt1
- Version 3.6.4

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.2-alt2.1
- Rebuild with Python-2.7

* Wed Jun 29 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.2-alt1
- Initial build for Sisyphus

