%define oname metalchemy

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.git20141006
Summary: SQLAlchemy hierarchical key/value helper
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/metalchemy/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/paylogic/metalchemy.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-SQLAlchemy python-module-detox
BuildPreReq: python-module-pytest-cache python-module-pytest-cov
BuildPreReq: python-module-pytest-pep8 python-module-mock
BuildPreReq: python-module-virtualenv python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-SQLAlchemy python3-module-detox
BuildPreReq: python3-module-pytest-cache python3-module-pytest-cov
BuildPreReq: python3-module-pytest-pep8 python3-module-mock
BuildPreReq: python3-module-virtualenv python3-modules-sqlite3
%endif

%py_provides %oname

%description
The metalchemy package provides helpers for your SQLAlchemy models to
add dynamic properties.

%package -n python3-module-%oname
Summary: SQLAlchemy hierarchical key/value helper
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The metalchemy package provides helpers for your SQLAlchemy models to
add dynamic properties.

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
py.test
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version
popd
%endif

%files
%doc *.rst docs/*.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst docs/*.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Jan 02 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1.git20141006
- Initial build for Sisyphus

