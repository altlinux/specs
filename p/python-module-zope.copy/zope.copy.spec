%define oname zope.copy

%def_with python3

Name: python-module-%oname
Version: 4.0.3
Release: alt1.1
Summary: Pluggable object copying mechanism
License: ZPLv2.1
Group: Development/Python
Url: http://pypi.python.org/pypi/zope.copy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_requires zope zope.interface

%description
This package provides a pluggable way to copy persistent objects. It was
once extracted from the zc.copy package to contain much less
dependencies. In fact, we only depend on zope.interface to provide
pluggability.

%package -n python3-module-%oname
Summary: Pluggable object copying mechanism
Group: Development/Python3
%py3_requires zope zope.interface

%description -n python3-module-%oname
This package provides a pluggable way to copy persistent objects. It was
once extracted from the zc.copy package to contain much less
dependencies. In fact, we only depend on zope.interface to provide
pluggability.

%package -n python3-module-%oname-tests
Summary: Tests for zope.copy
Group: Development/Python3
Requires: python3-module-%oname = %version-%release
%py3_requires zope.component zope.location zope.testing

%description -n python3-module-%oname-tests
This package provides a pluggable way to copy persistent objects. It was
once extracted from the zc.copy package to contain much less
dependencies. In fact, we only depend on zope.interface to provide
pluggability.

This package contains tests for zope.copy.

%package tests
Summary: Tests for zope.copy
Group: Development/Python
Requires: %name = %version-%release
%py_requires zope.component zope.location zope.testing

%description tests
This package provides a pluggable way to copy persistent objects. It was
once extracted from the zc.copy package to contain much less
dependencies. In fact, we only depend on zope.interface to provide
pluggability.

This package contains tests for zope.copy.

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
%exclude %python_sitelibdir/*/*/tests
%exclude %python_sitelibdir/*/*/examples.*

%files tests
%python_sitelibdir/*/*/tests
%python_sitelibdir/*/*/examples.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*.pth
%exclude %python3_sitelibdir/*/*/tests
%exclude %python3_sitelibdir/*/*/examples.*
%exclude %python3_sitelibdir/*/*/*/examples.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/tests
%python3_sitelibdir/*/*/examples.*
%python3_sitelibdir/*/*/*/examples.*
%endif

%changelog
* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 4.0.3-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Mon Dec 29 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.3-alt1
- Version 4.0.3

* Thu Jul 17 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt2
- Added module for Python 3

* Tue Apr 09 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0.2-alt1
- Version 4.0.2

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 3.5.0-alt2.1
- Rebuild with Python-2.7

* Tue Jun 28 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt2
- Added necesssary requirements
- Excluded *.pth

* Sat May 21 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5.0-alt1
- Initial build for Sisyphus

