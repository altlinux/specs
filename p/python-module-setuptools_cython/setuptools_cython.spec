%define oname setuptools_cython

%def_with python3

Name: python-module-%oname
Version: 0.2.1
Release: alt1.1
Summary: Cython setuptools integration
License: GPLv2
Group: Development/Python
Url: https://pypi.python.org/pypi/setuptools_cython/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-module-setuptools python-module-Cython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-module-setuptools python3-module-Cython
%endif

%py_provides %oname
%py_requires setuptools Cython

%description
Allows compiling Cython extensions in setuptools by putting
setuptools_cython in your setup_requires.

%package -n python3-module-%oname
Summary: Cython setuptools integration
Group: Development/Python3
%py3_provides %oname
%py3_requires setuptools Cython

%description -n python3-module-%oname
Allows compiling Cython extensions in setuptools by putting
setuptools_cython in your setup_requires.

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

%files
%doc PKG-INFO
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc PKG-INFO
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.2.1-alt1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Wed Feb 25 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.2.1-alt1
- Initial build for Sisyphus

