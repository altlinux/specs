%define oname leveldb

%def_with python3

Name: python-module-%oname
Version: 0.193
Release: alt2
Summary: Python bindings for leveldb database library
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/leveldb/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: libleveldb-devel
#BuildPreReq: python-devel python-module-setuptools gcc-c++
#BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-nose
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils libstdc++-devel python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-pytest python3-module-setuptools xz
BuildRequires: gcc-c++ python-module-nose python-module-setuptools python3-devel python3-module-nose python3-module-setuptools rpm-build-python3 time

%description
Python bindings for leveldb database library.

%package -n python3-module-%oname
Summary: Python bindings for leveldb database library
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
Python bindings for leveldb database library.

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
export PYTHONPATH=%buildroot%python_sitelibdir
nosetests
%if_with python3
pushd ../python3
python3 setup.py test
export PYTHONPATH=%buildroot%python3_sitelibdir
nosetests3
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
* Mon Feb 05 2018 Sergey Bolshakov <sbolshakov@altlinux.ru> 0.193-alt2
- fix build on aarch64

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.193-alt1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.193-alt1.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.193-alt1.1
- NMU: Use buildreq for BR.

* Sat Nov 22 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.193-alt1
- Initial build for Sisyphus

