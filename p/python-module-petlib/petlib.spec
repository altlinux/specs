%define oname petlib

%def_with python3

Name: python-module-%oname
Version: 0.0.8
Release: alt1
Summary: A library implementing a number of Privacy Enhancing Technologies (PETs)
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/petlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools-tests libssl-devel
BuildPreReq: python-module-cffi
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-cffi
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
%py_requires cffi

%description
A library wrapping Open SSL low-level cryptographic libraries to build
Privacy Enhancing Technoloies (PETs).

%package -n python3-module-%oname
Summary: A library implementing a number of Privacy Enhancing Technologies (PETs)
Group: Development/Python3
%py3_provides %oname
%py3_requires cffi

%description -n python3-module-%oname
A library wrapping Open SSL low-level cryptographic libraries to build
Privacy Enhancing Technoloies (PETs).

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
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

%ifarch x86_64
mv %buildroot%_libexecdir %buildroot%_libdir
%endif

%check
py.test petlib/*.py
install -d %buildroot%python_sitelibdir/%oname/__pycache__
install -m644 %oname/__pycache__/*.so \
	%buildroot%python_sitelibdir/%oname/__pycache__/
%if_with python3
pushd ../python3
#py.test-%_python3_version petlib/*.py
python3 -c "from petlib import bindings"
install -m644 %oname/__pycache__/*.so \
	%buildroot%python3_sitelibdir/%oname/__pycache__/
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
* Tue Nov 25 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.0.8-alt1
- Initial build for Sisyphus

