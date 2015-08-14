%define oname SQLConstruct

%def_with python3

Name: python-module-%oname
Version: 0.2.2
Release: alt1.git20150523
Summary: Functional approach to query database using SQLAlchemy
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/SQLConstruct
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/vmagamedov/sqlconstruct.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-mock
BuildPreReq: python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-mock
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides sqlconstruct
Provides: python-module-sqlconstruct = %EVR
%py_requires sqlalchemy

%description
SQLConstruct is a functional approach to query database using SQLAlchemy
library. It was written to reach more speed without introducing
unmaintainable and verbose code. On the contrary, code becomes simpler,
so there are less chances of shooting yourself in the foot.

Main problems it aims to solve:
* ORM overhead in read-only SELECT queries;
* Network traffic when loading unnecessary columns;
* Code complexity;
* N+1 problem.

%if_with python3
%package -n python3-module-%oname
Summary: Functional approach to query database using SQLAlchemy
Group: Development/Python3
%py3_provides sqlconstruct
Provides: python3-module-sqlconstruct = %EVR
%py3_requires sqlalchemy

%description -n python3-module-%oname
SQLConstruct is a functional approach to query database using SQLAlchemy
library. It was written to reach more speed without introducing
unmaintainable and verbose code. On the contrary, code becomes simpler,
so there are less chances of shooting yourself in the foot.

Main problems it aims to solve:
* ORM overhead in read-only SELECT queries;
* Network traffic when loading unnecessary columns;
* Code complexity;
* N+1 problem.
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
python setup.py test -v
python -m unittest tests
%if_with python3
pushd ../python3
python3 setup.py test -v
python3 -m unittest tests
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Aug 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.2-alt1.git20150523
- Initial build for Sisyphus

