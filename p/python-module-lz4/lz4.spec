%define _unpackaged_files_terminate_build 1
%define oname lz4

%def_with python3

Name: python-module-%oname
Version: 0.8.2
Release: alt1.1
Summary: LZ4 Bindings for Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/lz4/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/steeve/python-lz4.git
Source0: https://pypi.python.org/packages/b5/f0/e1de2bb7feb54011f3c4dcf35b7cca3536e19526764db051b50ea26b58e7/%{oname}-%{version}.tar.gz

#BuildPreReq: liblz4-devel
#BuildPreReq: python-devel python-module-setuptools
#BuildPreReq: python-module-nose python-module-snappy
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools
#BuildPreReq: python3-module-nose python3-module-snappy
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-pytest python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-logging python-modules-multiprocessing python-modules-unittest python-modules-xml python3 python3-base python3-module-pytest python3-module-setuptools
BuildRequires: python-module-nose python-module-setuptools python-module-snappy python3-devel python3-module-nose python3-module-setuptools python3-module-snappy rpm-build-python3

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
%setup -q -n %{oname}-%{version}

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
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.8.2-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Wed Jan 11 2017 Igor Vlasenko <viy@altlinux.ru> 0.8.2-alt1
- automated PyPI update

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.7.0-alt1.git20140728.1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7.0-alt1.git20140728.1
- NMU: Use buildreq for BR.

* Sun Nov 09 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7.0-alt1.git20140728
- Initial build for Sisyphus

