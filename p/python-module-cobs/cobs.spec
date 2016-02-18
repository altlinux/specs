%define oname cobs

%def_with python3

Name: python-module-%oname
Version: 1.0.0
Release: alt1.1
Summary: Consistent Overhead Byte Stuffing (COBS)
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/cobs/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: elfutils python-base python-modules python-modules-compiler python-modules-email python3 python3-base
BuildRequires: python-devel python-modules-unittest python3-devel rpm-build-python3

%description
The cobs package is provided, which contains modules containing
functions for encoding and decoding according to COBS methods.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
The cobs package is provided, which contains modules containing
functions for encoding and decoding according to COBS methods.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Consistent Overhead Byte Stuffing (COBS)
Group: Development/Python3
%py3_provides %oname

%description -n python3-module-%oname
The cobs package is provided, which contains modules containing
functions for encoding and decoding according to COBS methods.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
The cobs package is provided, which contains modules containing
functions for encoding and decoding according to COBS methods.

This package contains tests for %oname.

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
python setup.py build_ext -i
pushd python2
python -m cobs.cobs.test -v
python -m cobs.cobsr.test -v
popd
%if_with python3
pushd ../python3
python3 setup.py build_ext -i
pushd python3
python3 -m cobs.cobs.test -v
python3 -m cobs.cobsr.test -v
popd
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*
%exclude %python_sitelibdir/*/*/test.*

%files tests
%python_sitelibdir/*/*/test.*

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/*/test.*
%exclude %python3_sitelibdir/*/*/*/test.*

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/*/test.*
%python3_sitelibdir/*/*/*/test.*
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.0-alt1.1
- NMU: Use buildreq for BR.

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.0-alt1
- Initial build for Sisyphus

