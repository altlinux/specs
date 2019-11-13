%define oname sqlalchemy-batteries

Name: python3-module-%oname
Version: 0.4.5
Release: alt2

Summary: Various batteries for SQLAlchemy models
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/sqlalchemy-batteries/
# https://github.com/jessedhillon/batteries.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3

%py3_provides batteries

BuildRequires: python3-module-geoalchemy2 python3-module-pytest
BuildRequires: python-tools-2to3


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
Group: Development/Python3
Requires: %name = %EVR

%description tests
This module contains Paste templates, SQLAlchemy mixins, utility
functions, and miscellany which experience has shown to be useful enough
to require reusable packaging.

This package contains tests for %oname.

%prep
%setup

find ./ -type f -name '*.py' -exec 2to3 -w -n '{}' +

%build
%python3_build_debug

%install
%python3_install

%check
%if 0
python3 setup.py test
%endif

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests


%changelog
* Wed Nov 13 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.4.5-alt2
- disable python2

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

