%define oname pytest-spec

%def_with python3

Name: python-module-%oname
Version: 0.2.24
Release: alt1.git20150202
Summary: pytest plugin to display test execution output like a SPECIFICATION
License: GPLv2+
Group: Development/Python
Url: https://pypi.python.org/pypi/pytest-spec/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/pchomik/pytest-spec.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-mock
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-mock
%endif

%py_provides pytest_spec
%py_requires pytest mock

%description
pytest plugin to display test execution output like a SPECIFICATION.

Available features:

* Format output to look like specification.
* Group tests by classes.
* Failed, passed and skipped are marked and colored.
* Remove test_ and underscores for every test.
* Method under test may be highlighted (method) like in example.

%package -n python3-module-%oname
Summary: pytest plugin to display test execution output like a SPECIFICATION
Group: Development/Python3
%py3_provides pytest_spec
%py3_requires pytest mock

%description -n python3-module-%oname
pytest plugin to display test execution output like a SPECIFICATION.

Available features:

* Format output to look like specification.
* Group tests by classes.
* Failed, passed and skipped are marked and colored.
* Remove test_ and underscores for every test.
* Method under test may be highlighted (method) like in example.

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
py.test -vv
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=$PWD
py.test-%_python3_version -vv
popd
%endif

%files
%doc *.txt *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt *.rst
%python3_sitelibdir/*
%endif

%changelog
* Tue Feb 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.24-alt1.git20150202
- Initial build for Sisyphus

