%define oname pyarmor

%def_with python3

Name: python-module-%oname
Version: 2.1.1
Release: alt1
Summary: A python package could import/run encrypted python scripts
License: Shareware
Group: Development/Python
Url: https://pypi.python.org/pypi/pyarmor/
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
A python package could import/run encrypted python scripts.

%package -n python3-module-%oname
Summary: A python package could import/run encrypted python scripts
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A python package could import/run encrypted python scripts.

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
py.test
%if_with python3
pushd ../python3
py.test-%_python3_version
popd
%endif

%files
%doc README *.lic *.key *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README *.lic *.key *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 01 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.1.1-alt1
- Initial build for Sisyphus

