%define oname responses

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3.0
Release: alt3.1
Summary: A utility library for mocking out the requests Python library
License: ASLv2.0
Group: Development/Python
Url: https://pypi.python.org/pypi/responses/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: python-module-requests python-module-mock
BuildPreReq: python-module-six python-module-pytest-cov
BuildPreReq: python-module-flake8
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-requests python3-module-mock
BuildPreReq: python3-module-six python3-module-pytest-cov
BuildPreReq: python3-module-flake8
%endif

%py_provides %oname
%py_requires requests mock

%description
A utility library for mocking out the `requests` Python library.

%package -n python3-module-%oname
Summary: A utility library for mocking out the requests Python library
Group: Development/Python3
%py3_provides %oname
%py3_requires requests mock

%description -n python3-module-%oname
A utility library for mocking out the `requests` Python library.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.0-alt3.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 31 2016 Denis Medvedev <nbr@altlinux.org> 0.3.0-alt3
- Rebuild with changed site-packages in sisyphus

* Thu Feb 25 2016 Denis Medvedev <nbr@altlinux.org> 0.3.0-alt2
- Rebuild into sisyphus

* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.0-alt1
- Initial build for Sisyphus

