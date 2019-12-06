%define oname Ming

Name: python3-module-%oname
Version: 0.5.0
Release: alt3

Summary: Bringing order to Mongo since 2009
License: MIT
Group: Development/Python3
Url: http://pypi.python.org/pypi/Ming/
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3


%description
Database mapping layer for MongoDB on Python. Includes schema
enforcement and some facilities for schema migration.

%package tests
Summary: Tests for Bringing order to Mongo since 2009
Group: Development/Python3
Requires: %name = %version-%release

%description tests
Database mapping layer for MongoDB on Python. Includes schema
enforcement and some facilities for schema migration.

This package contains tests for Ming.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%files
%doc PKG-INFO README
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Fri Dec 06 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.5.0-alt3
- build for python2 disabled

* Wed May 16 2018 Andrey Bychkov <mrdrew@altlinux.org> 0.5.0-alt2.2
- (NMU) rebuild with python3.6

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

