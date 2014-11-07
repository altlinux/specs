%define oname PyRSS2Gen

%def_with python3

Name: python-module-%oname
Version: 1.1
Release: alt1
Summary: Generate RSS2 using a Python data structure
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/PyRSS2Gen/
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
A Python library for generating RSS 2.0 feeds.

%package -n python3-module-%oname
Summary: Generate RSS2 using a Python data structure
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
A Python library for generating RSS 2.0 feeds.

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
%doc README
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc README
%python3_sitelibdir/*
%endif

%changelog
* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1-alt1
- Initial build for Sisyphus

