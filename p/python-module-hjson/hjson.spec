%define oname hjson

%def_with python3

Name: python-module-%oname
Version: 1.4.1
Release: alt1.git20150116.1.1
Summary: JSON for Humans, allows comments and is less error prone
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/hjson/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/laktak/hjson-py.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

%description
Hjson, the Human JSON. A data format that caters to humans and helps
reduce the errors they make.

It supports #, // and /**/ style comments as well as avoiding
trailing/missing comma and other mistakes.
For details and syntax see hjson.org.

%package tests
Summary: tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Hjson, the Human JSON. A data format that caters to humans and helps
reduce the errors they make.

It supports #, // and /**/ style comments as well as avoiding
trailing/missing comma and other mistakes.
For details and syntax see hjson.org.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: JSON for Humans, allows comments and is less error prone
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip UserDict

%description -n python3-module-%oname
Hjson, the Human JSON. A data format that caters to humans and helps
reduce the errors they make.

It supports #, // and /**/ style comments as well as avoiding
trailing/missing comma and other mistakes.
For details and syntax see hjson.org.

%package -n python3-module-%oname-tests
Summary: tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
Hjson, the Human JSON. A data format that caters to humans and helps
reduce the errors they make.

It supports #, // and /**/ style comments as well as avoiding
trailing/missing comma and other mistakes.
For details and syntax see hjson.org.

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
cp -fR %oname/tests/assets %buildroot%python_sitelibdir/%oname/tests/

%if_with python3
pushd ../python3
%python3_install
cp -fR %oname/tests/assets %buildroot%python3_sitelibdir/%oname/tests/
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
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.1-alt1.git20150116.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.1-alt1.git20150116.1
- NMU: Use buildreq for BR.

* Sun Jan 18 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.1-alt1.git20150116
- Initial build for Sisyphus

