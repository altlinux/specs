%define oname kungfu

%def_with python3

Name: python-module-%oname
Version: 1.5.1
Release: alt1
Summary: A Pandas Enhancement
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/kungfu/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-pandas python-module-openpyxl
BuildPreReq: python-module-xlrd python-module-numpy
BuildPreReq: python-module-xlwt
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-pandas python3-module-openpyxl
BuildPreReq: python3-module-xlrd python3-module-numpy
BuildPreReq: python3-module-xlwt-future
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires pandas openpyxl xlrd numpy xlwt

%description
An enhancement to pandas module. This is kungfu, with monkey-patched
common methods to (Data)Frame and Series in pandas.

%package -n python3-module-%oname
Summary: A Pandas Enhancement
Group: Development/Python3
%py3_provides %oname
%py3_requires pandas openpyxl xlrd numpy xlwt

%description -n python3-module-%oname
An enhancement to pandas module. This is kungfu, with monkey-patched
common methods to (Data)Frame and Series in pandas.

%prep
%setup

%if_with python3
cp -fR . ../python3
find ../python3 -type f -name '*.py' -exec 2to3 -w -n '{}' +
%endif

%build
%python_build_debug

%if_with python3
pushd ../python3
%python3_build_debug
popd
%endif

%install
export LC_ALL=en_US.UTF-8
%python_install

%if_with python3
pushd ../python3
%python3_install
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
* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.5.1-alt1
- Initial build for Sisyphus

