%define oname Ming

%def_with python3

Name: python-module-%oname
Version: 0.5.0
Release: alt2.1
Summary: Bringing order to Mongo since 2009
License: MIT
Group: Development/Python
Url: http://pypi.python.org/pypi/Ming/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%description
Database mapping layer for MongoDB on Python. Includes schema
enforcement and some facilities for schema migration.

%package -n python3-module-%oname
Summary: Bringing order to Mongo since 2009
Group: Development/Python3

%description -n python3-module-%oname
Database mapping layer for MongoDB on Python. Includes schema
enforcement and some facilities for schema migration.

%package -n python3-module-%oname-tests
Summary: Tests for Bringing order to Mongo since 2009
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-tests
Database mapping layer for MongoDB on Python. Includes schema
enforcement and some facilities for schema migration.

This package contains tests for Ming.

%package tests
Summary: Tests for Bringing order to Mongo since 2009
Group: Development/Python
Requires: %name = %version-%release

%description tests
Database mapping layer for MongoDB on Python. Includes schema
enforcement and some facilities for schema migration.

This package contains tests for Ming.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%files
%doc PKG-INFO README
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.0-alt2.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Tue Jul 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt2
- Added module for Python 3

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.0-alt1
- Version 0.5.0

* Fri Nov 29 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1
- Version 0.4.2

* Mon Sep 16 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.1-alt1
- Version 0.4.1

* Tue Feb 12 2013 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.dev.20121219
- Version 0.3.2dev-20121219

* Wed Sep 26 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.2-alt1.dev.20120912
- Initial build for Sisyphus

