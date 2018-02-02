%define oname sqlalchemy-batteries

%def_with python3

Name: python-module-%oname
Version: 0.4.5
Release: alt1.git20150204.1.1.1
Summary: Various batteries for SQLAlchemy models
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlalchemy-batteries/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/jessedhillon/batteries.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-SQLAlchemy python-module-dateutil
#BuildPreReq: python-module-geoalchemy2 python-module-shapely
#BuildPreReq: python-modules-json python-module-pysqlite2
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-SQLAlchemy python3-module-dateutil
#BuildPreReq: python3-module-geoalchemy2 python3-module-shapely
#BuildPreReq: python-tools-2to3 python3-modules-sqlite3
%endif

%py_provides batteries

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-SQLAlchemy python-module-pytest python-module-setuptools python-module-shapely python-module-six python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-logging python-modules-unittest python-tools-2to3 python3 python3-base python3-module-setuptools
BuildRequires: python-module-dateutil python-module-geoalchemy2 python-module-pysqlite2 python-module-setuptools python-modules-json python3-module-geoalchemy2 python3-module-pytest rpm-build-python3 time

%description
This module contains Paste templates, SQLAlchemy mixins, utility
functions, and miscellany which experience has shown to be useful enough
to require reusable packaging.

This package may one day aspire to be useful to a wide audience, and so
useful examples and comprehensive documentation might be found in this
file. But for today, if you need it you know how to use it already. And
if you really want to take a look at what it does, check out the tests.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This module contains Paste templates, SQLAlchemy mixins, utility
functions, and miscellany which experience has shown to be useful enough
to require reusable packaging.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Various batteries for SQLAlchemy models
Group: Development/Python3
%py3_provides batteries

%description -n python3-module-%oname
This module contains Paste templates, SQLAlchemy mixins, utility
functions, and miscellany which experience has shown to be useful enough
to require reusable packaging.

This package may one day aspire to be useful to a wide audience, and so
useful examples and comprehensive documentation might be found in this
file. But for today, if you need it you know how to use it already. And
if you really want to take a look at what it does, check out the tests.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This module contains Paste templates, SQLAlchemy mixins, utility
functions, and miscellany which experience has shown to be useful enough
to require reusable packaging.

This package contains tests for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
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

%check
python setup.py test
#if_with python3
%if 0
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.5-alt1.git20150204.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.5-alt1.git20150204.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.4.5-alt1.git20150204.1
- NMU: Use buildreq for BR.

* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.5-alt1.git20150204
- Version 0.4.5

* Thu Dec 11 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.4-alt1.git20141210
- Version 0.4.4
- Added module for Python 3

* Thu Nov 13 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20141112
- New snapshot

* Sun Nov 02 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.2-alt1.git20141101
- Initial build for Sisyphus

