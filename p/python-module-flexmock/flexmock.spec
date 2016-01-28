%define oname flexmock

%def_with python3

Name: python-module-%oname
Version: 0.9.7
Release: alt1.git20140924.1
Summary: Mock/Stub/Spy library for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/flexmock/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/has207/flexmock.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose python-module-twisted-core-test
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose python3-module-twisted-core-test
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-OpenSSL python-module-cffi python-module-cryptography python-module-enum34 python-module-pluggy python-module-py python-module-pyasn1 python-module-serial python-module-setuptools python-module-six python-module-twisted-core python-module-zope python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-OpenSSL python3-module-cffi python3-module-cryptography python3-module-enum34 python3-module-pluggy python3-module-py python3-module-pycparser python3-module-pygobject3 python3-module-serial python3-module-setuptools python3-module-six python3-module-twisted-core python3-module-zope python3-module-zope.interface xz
BuildRequires: python-module-nose python-module-pytest python-module-twisted-core-test python-module-twisted-logger python3-module-nose python3-module-pytest python3-module-twisted-core-test rpm-build-python3 time

%description
flexmock is a testing library for Python that makes it easy to create
mocks, stubs and fakes.

%package -n python3-module-%oname
Summary: Mock/Stub/Spy library for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
flexmock is a testing library for Python that makes it easy to create
mocks, stubs and fakes.

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
tests/run_tests.sh
%if_with python3
pushd ../python3
tests/run_tests.sh
popd
%endif

%files
%doc CHANGELOG *.md
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGELOG *.md
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.9.7-alt1.git20140924.1
- NMU: Use buildreq for BR.

* Sat Nov 01 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.7-alt1.git20140924
- Initial build for Sisyphus

