%define oname random_Json_generator

%def_with python3

Name: python-module-%oname
Version: 0.00
Release: alt1
Summary: Create a random JSON data for testing
License: LGPL
Group: Development/Python
Url: https://pypi.python.org/pypi/random_Json_generator/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

%description
Create a random JSON data for testing.

%package -n python3-module-%oname
Summary: Create a random JSON data for testing
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Create a random JSON data for testing.

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
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.00-alt1
- Initial build for Sisyphus

