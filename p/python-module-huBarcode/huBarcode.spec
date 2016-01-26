%define oname huBarcode

%def_without python3
%def_disable check

Name: python-module-%oname
Version: 1.0.1
Release: alt3.git20140102
Summary: Generation of barcodes in Python
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/huBarcode/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/hudora/huBarcode.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires: python-devel
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-Pillow python-module-coverage
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-Pillow python3-module-coverage
BuildRequires: python3
BuildPreReq: python-tools-2to3
%endif

%py_provides %oname hubarcode
#%py_requires PIL

%description
huBarcode is a Python Library to generate 1D and 2D Barcodes.

%if_with python3
%package -n python3-module-%oname
Summary: Generation of barcodes in Python
Group: Development/Python3
%py3_provides %oname hubarcode
#%py3_requires PIL

%description -n python3-module-%oname
huBarcode is a Python Library to generate 1D and 2D Barcodes.
%endif

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
%make test
%if_with python3
pushd ../python3
sed -i 's|python|python3|g' Makefile
%make test
popd
%endif

%files
%doc CHANGES examples *.textile sample_barcodes
%python_sitelibdir/*

%if_with python3
%files -n python3-module-%oname
%doc CHANGES examples *.textile sample_barcodes
%python3_sitelibdir/*
%endif

%changelog
* Tue Jan 26 2016 Sergey Alembekov <rt@altlinux.ru> 1.0.1-alt3.git20140102
- Rebuild with "def_disable check"
- Cleanup buildreq

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt2.git20140102
- Fixed build

* Sat Feb 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.1-alt1.git20140102
- Initial build for Sisyphus

