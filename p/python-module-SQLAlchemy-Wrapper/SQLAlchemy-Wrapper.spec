%define oname SQLAlchemy-Wrapper

%def_with python3

Name: python-module-%oname
Version: 1.3.0
Release: alt1.git20150102
Summary: A framework-independent wrapper for SQLAlchemy that makes it really easy to use
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/SQLAlchemy-Wrapper/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lucuma/sqlalchemy-wrapper.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-inflection python-module-SQLAlchemy
BuildPreReq: python-module-pytest-cov python-module-tox
BuildPreReq: python-modules-sqlite3
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-inflection python3-module-SQLAlchemy
BuildPreReq: python3-module-pytest-cov python3-module-tox
BuildPreReq: python3-modules-sqlite3
%endif

%py_provides sqlalchemy_wrapper
%py_requires inflection sqlalchemy

%description
A framework-independent wrapper for SQLAlchemy that makes it really easy
to use.

%package -n python3-module-%oname
Summary: A framework-independent wrapper for SQLAlchemy that makes it really easy to use
Group: Development/Python3
%py3_provides sqlalchemy_wrapper
%py3_requires inflection sqlalchemy

%description -n python3-module-%oname
A framework-independent wrapper for SQLAlchemy that makes it really easy
to use.

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
export PYTHONPATH=$PWD
%make test
%if_with python3
pushd ../python3
python3 setup.py test
sed -i 's|py.test|py.test-%_python3_version|' Makefile
export PYTHONPATH=$PWD
%make test
popd
%endif

%files
%doc AUTHORS *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc AUTHORS *.rst
%python3_sitelibdir/*
%endif

%changelog
* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.3.0-alt1.git20150102
- Initial build for Sisyphus

