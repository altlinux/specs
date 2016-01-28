%define oname lz4

%def_with python3

Name: python-module-%oname
Version: 0.7.0
Release: alt1.git20140728.1
Summary: LZ4 Bindings for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/lz4/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/steeve/python-lz4.git
Source: %name-%version.tar

#BuildPreReq: liblz4-devel
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-nose python-module-snappy
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-nose python3-module-snappy
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-nose python-module-setuptools-tests python-module-snappy python3-devel python3-module-nose python3-module-setuptools-tests python3-module-snappy rpm-build-python3

%description
This package provides bindings for the lz4 compression library by Yann
Collet.

%package -n python3-module-%oname
Summary: LZ4 Bindings for Python
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
This package provides bindings for the lz4 compression library by Yann
Collet.

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
%doc *.rst
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.git20140728.1
- NMU: Use buildreq for BR.

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20140728
- Initial build for Sisyphus

