%define oname aiodns

%def_with python3

Name: python-module-%oname
Version: 0.3.1
Release: alt1.git20141207.1
Summary: Simple DNS resolver for asyncio
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/aiodns/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/saghul/aiodns.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-pycares python-module-trollius
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-pycares python3-module-asyncio
%endif

%py_provides %oname
%py_requires pycares trollius

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-pycares python-module-setuptools-tests python-module-trollius python3-module-pycares python3-module-setuptools-tests rpm-build-python3

%description
aiodns provides a simple way for doing asynchronous DNS resolutions with
a synchronous looking interface by using pycares.

%package -n python3-module-%oname
Summary: Simple DNS resolver for asyncio
Group: Development/Python3
%py3_provides %oname
%py3_requires pycares asyncio

%description -n python3-module-%oname
aiodns provides a simple way for doing asynchronous DNS resolutions with
a synchronous looking interface by using pycares.

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
#python tests.py
%if_with python3
pushd ../python3
python3 setup.py test
#python3 tests.py
popd
%endif

%files
%doc ChangeLog *.rst tests.py
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc ChangeLog *.rst tests.py
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1.git20141207.1
- NMU: Use buildreq for BR.

* Fri Jan 09 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20141207
- Initial build for Sisyphus

