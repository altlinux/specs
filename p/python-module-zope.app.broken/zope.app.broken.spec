%define oname zope.app.broken

%def_with python3

Name: python-module-%oname
Version: 3.6.0
Release: alt3.1
Summary: Zope Broken (ZODB) Object Support
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.app.broken/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope.app zope.interface zope.location zope.security
%py_requires zope.annotation zope.broken zope.processlifetime ZODB3

%description
When an object cannot be correctly loaded from the ZODB, this package
allows this object still to be instantiated, but as a "Broken" object.
This allows for gracefully updating the database without interuption.

%package -n python3-module-%oname
Summary: Zope Broken (ZODB) Object Support
Group: Development/Python3
%py3_requires zope.app zope.interface zope.location zope.security
%py3_requires zope.annotation zope.broken zope.processlifetime ZODB3

%description -n python3-module-%oname
When an object cannot be correctly loaded from the ZODB, this package
allows this object still to be instantiated, but as a "Broken" object.
This allows for gracefully updating the database without interuption.

%package -n python3-module-%oname-tests
Summary: Tests for Zope Broken (ZODB) Object Support
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.testing

%description -n python3-module-%oname-tests
When an object cannot be correctly loaded from the ZODB, this package
allows this object still to be instantiated, but as a "Broken" object.
This allows for gracefully updating the database without interuption.

This package contains tests for Zope Broken (ZODB) Object Support.

%package tests
Summary: Tests for Zope Broken (ZODB) Object Support
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.testing

%description tests
When an object cannot be correctly loaded from the ZODB, this package
allows this object still to be instantiated, but as a "Broken" object.
This allows for gracefully updating the database without interuption.

This package contains tests for Zope Broken (ZODB) Object Support.

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
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 3.6.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jul 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.6.0-alt2.1
- Rebuild with Python-2.7

* Mon Jun 27 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt2
- Added necessary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.6.0-alt1
- Initial build for Sisyphus

