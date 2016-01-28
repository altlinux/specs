%define oname clang

%def_with python3

Name: python-module-%oname
Version: 3.5
Release: alt1.1
Summary: libclang python bindings
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/clang/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests clang
#BuildPreReq: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose
#BuildPreReq: python-tools-2to3
%endif

%py_provides %oname
Requires: clang

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python-tools-2to3 python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-nose python-module-setuptools-tests python3-module-nose python3-module-setuptools-tests rpm-build-python3 time

%description
This is the python bindings subdir of llvm clang repository.
https://github.com/llvm-mirror/clang/tree/master/bindings/python

This is a fork. Mainly for Pypi packaging purposes.

%package -n python3-module-%oname
Summary: libclang python bindings
Group: Development/Python3
%py3_provides %oname
Requires: clang

%description -n python3-module-%oname
This is the python bindings subdir of llvm clang repository.
https://github.com/llvm-mirror/clang/tree/master/bindings/python

This is a fork. Mainly for Pypi packaging purposes.

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

%check
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 3.5-alt1.1
- NMU: Use buildreq for BR.

* Fri Jan 23 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 3.5-alt1
- Initial build for Sisyphus

