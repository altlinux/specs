%define oname z3c.iplocation

%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt3.1
Summary: Geo location utility for Zope3
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/z3c.iplocation/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-tools-2to3
%endif

%py_requires zc.catalog zope.app.container zope.app.intid
%py_requires zope.app.keyreference zope.component zope.schema z3c.schema

%description
This package provides a solution which allows geolocation of IP blocks,
country and continent of the visitor connection. The dataset, which must
be downloaded form www.ipligence.com, contains IP location at a
worldwide level. There are different commercial and free version
available at the homepage of ipligence.

%package -n python3-module-%oname
Summary: Geo location utility for Zope3
Group: Development/Python3
%py3_requires zc.catalog zope.app.container zope.app.intid
%py3_requires zope.app.keyreference zope.component zope.schema z3c.schema

%description -n python3-module-%oname
This package provides a solution which allows geolocation of IP blocks,
country and continent of the visitor connection. The dataset, which must
be downloaded form www.ipligence.com, contains IP location at a
worldwide level. There are different commercial and free version
available at the homepage of ipligence.

%package -n python3-module-%oname-tests
Summary: Tests for Geo location utility for Zope3
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires z3c.coverage zope.annotation zope.app.testing zope.testing

%description -n python3-module-%oname-tests
This package provides a solution which allows geolocation of IP blocks,
country and continent of the visitor connection. The dataset, which must
be downloaded form www.ipligence.com, contains IP location at a
worldwide level. There are different commercial and free version
available at the homepage of ipligence.

This package contains tests for Geo location utility for Zope3.

%package tests
Summary: Tests for Geo location utility for Zope3
Group: Development/Python
Requires: %name = %version-%release
%py_requires z3c.coverage zope.annotation zope.app.testing zope.testing

%description tests
This package provides a solution which allows geolocation of IP blocks,
country and continent of the visitor connection. The dataset, which must
be downloaded form www.ipligence.com, contains IP location at a
worldwide level. There are different commercial and free version
available at the homepage of ipligence.

This package contains tests for Geo location utility for Zope3.

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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt3.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Jul 21 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt3
- Added module for Python 3

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.5.0-alt2.1
- Rebuild with Python-2.7

* Fri Jun 24 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2
- Added necessary requirements
- Excluded *.pth

* Mon May 30 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Initial build for Sisyphus

