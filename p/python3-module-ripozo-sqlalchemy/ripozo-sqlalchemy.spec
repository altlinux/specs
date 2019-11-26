%define oname ripozo-sqlalchemy

Name: python3-module-%oname
Version: 0.1.6
Release: alt2

Summary: A python package for integrating sqlalchemy with ripozo
License: UNKNOWN
Group: Development/Python3
Url: https://pypi.python.org/pypi/ripozo-sqlalchemy/
# https://github.com/vertical-knowledge/ripozo-sqlalchemy.git
BuildArch: noarch

Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-ripozo python3-module-SQLAlchemy
BuildPreReq: python3-module-tox python3-module-ripozo-tests
BuildPreReq: python3-module-coverage python3-module-virtualenv
BuildPreReq: python3-module-mock
BuildPreReq: python3-modules-sqlite3

%py3_provides ripozo_sqlalchemy
%py3_requires ripozo sqlalchemy logging


%description
This package is a ripozo extension that provides a Manager that
integrate SQLAlchemy with ripozo. It provides convience functions for
generating resources. In particular, it focuses on creating shortcuts
for CRUD type operations. It fully implements the BaseManager class that
is provided in the ripozo package.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This package is a ripozo extension that provides a Manager that
integrate SQLAlchemy with ripozo. It provides convience functions for
generating resources. In particular, it focuses on creating shortcuts
for CRUD type operations. It fully implements the BaseManager class that
is provided in the ripozo package.

This package contains tests for %oname.

%prep
%setup

%build
%python3_build_debug

%install
%python3_install

%check
%__python3 setup.py test

%files
%doc *.rst docs/source/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/ripozo_sqlalchemy_tests

%files tests
%python3_sitelibdir/ripozo_sqlalchemy_tests


%changelog
* Tue Nov 26 2019 Andrey Bychkov <mrdrew@altlinux.org> 0.1.6-alt2
- python2 disabled

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.6-alt1.dev0.git20150428.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.6-alt1.dev0.git20150428.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.dev0.git20150428
- Version 0.1.6.dev0

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.dev0.git20150319
- Initial build for Sisyphus

