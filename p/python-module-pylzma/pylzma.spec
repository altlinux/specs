%define oname pylzma

%def_with python3

Name: python-module-%oname
Version: 0.4.6.2
Release: alt1.git20141116.1.1
Summary: Python bindings for the LZMA library by Igor Pavlov
License: LGPLv2.1+
Group: Development/Python
Url: https://pypi.python.org/pypi/pylzma/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/fancycode/pylzma.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
%endif

%py_provides %oname

%description
PyLZMA provides a platform independent way to read and write data that
has been compressed or can be decompressed by the LZMA library by Igor
Pavlov.

%package -n python3-module-%oname
Summary: Python bindings for the LZMA library by Igor Pavlov
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
PyLZMA provides a platform independent way to read and write data that
has been compressed or can be decompressed by the LZMA library by Igor
Pavlov.

%prep
%setup

sed -i 's|@VERSION@|%version|' version.py

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
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
%doc *.md doc/*
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc *.md doc/*
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.4.6.2-alt1.git20141116.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.4.6.2-alt1.git20141116.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Wed Nov 26 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4.6.2-alt1.git20141116
- Initial build for Sisyphus

