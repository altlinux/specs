%define oname sqlquery

%def_with python3

Name: python-module-%oname
Version: 0.0.4
Release: alt1.git20150122.1
Summary: SQL query translation
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/sqlquery/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/coldeasy/py-sql-query.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock python-module-six
BuildPreReq: python-module-wheel
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock python3-module-six
BuildPreReq: python3-module-wheel
%endif

%py_provides %oname
%py_requires six

%description
py-sql-query is a basic and pre-alpha SQL translation layer in python.
You construct queries using mainly python constructs which later can be
serialized to a SQL query.

%package -n python3-module-%oname
Summary: SQL query translation
Group: Development/Python3
%py3_provides %oname
%py3_requires six

%description -n python3-module-%oname
py-sql-query is a basic and pre-alpha SQL translation layer in python.
You construct queries using mainly python constructs which later can be
serialized to a SQL query.

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
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
py.test-%_python3_version -vv
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
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.0.4-alt1.git20150122.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.4-alt1.git20150122
- Initial build for Sisyphus

