%define oname ripozo-sqlalchemy

%def_with python3

Name: python-module-%oname
Version: 0.1.6
Release: alt1.dev0.git20150428.1.1
Summary: A python package for integrating sqlalchemy with ripozo
License: UNKNOWN
Group: Development/Python
Url: https://pypi.python.org/pypi/ripozo-sqlalchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vertical-knowledge/ripozo-sqlalchemy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-ripozo python-module-SQLAlchemy
BuildPreReq: python-module-tox python-module-ripozo-tests
BuildPreReq: python-module-coverage python-module-virtualenv
BuildPreReq: python-module-mock
BuildPreReq: python-modules-logging python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-ripozo python3-module-SQLAlchemy
BuildPreReq: python3-module-tox python3-module-ripozo-tests
BuildPreReq: python3-module-coverage python3-module-virtualenv
BuildPreReq: python3-module-mock
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides ripozo_sqlalchemy
%py_requires ripozo sqlalchemy logging

%description
This package is a ripozo extension that provides a Manager that
integrate SQLAlchemy with ripozo. It provides convience functions for
generating resources. In particular, it focuses on creating shortcuts
for CRUD type operations. It fully implements the BaseManager class that
is provided in the ripozo package.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This package is a ripozo extension that provides a Manager that
integrate SQLAlchemy with ripozo. It provides convience functions for
generating resources. In particular, it focuses on creating shortcuts
for CRUD type operations. It fully implements the BaseManager class that
is provided in the ripozo package.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: A python package for integrating sqlalchemy with ripozo
Group: Development/Python3
%py3_provides ripozo_sqlalchemy
%py3_requires ripozo sqlalchemy logging

%description -n python3-module-%oname
This package is a ripozo extension that provides a Manager that
integrate SQLAlchemy with ripozo. It provides convience functions for
generating resources. In particular, it focuses on creating shortcuts
for CRUD type operations. It fully implements the BaseManager class that
is provided in the ripozo package.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This package is a ripozo extension that provides a Manager that
integrate SQLAlchemy with ripozo. It provides convience functions for
generating resources. In particular, it focuses on creating shortcuts
for CRUD type operations. It fully implements the BaseManager class that
is provided in the ripozo package.

This package contains tests for %oname.
%endif

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.rst docs/source/*.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/ripozo_sqlalchemy_tests

%files tests
%python_sitelibdir/ripozo_sqlalchemy_tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/source/*.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/ripozo_sqlalchemy_tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/ripozo_sqlalchemy_tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.1.6-alt1.dev0.git20150428.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.1.6-alt1.dev0.git20150428.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Apr 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.6-alt1.dev0.git20150428
- Version 0.1.6.dev0

* Tue Mar 24 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.1.2-alt1.dev0.git20150319
- Initial build for Sisyphus

