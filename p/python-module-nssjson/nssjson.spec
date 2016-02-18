%define oname nssjson

%def_with python3

Name: python-module-%oname
Version: 0.7
Release: alt1.git20150807.1
Summary: Not So Simple JSON encoder/decoder
License: MIT
Group: Development/Python
Url: https://pypi.python.org/pypi/nssjson
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lelit/nssjson.git
# branch: nssjson
Source: %name-%version.tar

#BuildPreReq: python-devel python-module-setuptools-tests
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

%py_provides %oname

# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: elfutils python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-devel python3-module-pytest rpm-build-python3

%description
nssjson is a (not so) simple, fast, complete, correct and extensible
JSON encoder and decoder for Python 2.5+ and Python 3.3+. It is pure
Python code with no dependencies, but includes an optional C extension
for a serious speed boost.

nssjson is a fork of simplejson that fulfills my need of having a good
performance JSON encoder/decoder able to handle also Python's datetime
and UUID, even if with an admittedly non-standard and faulty heuristic
that was not considered within the scope of the original product.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
nssjson is a (not so) simple, fast, complete, correct and extensible
JSON encoder and decoder for Python 2.5+ and Python 3.3+. It is pure
Python code with no dependencies, but includes an optional C extension
for a serious speed boost.

nssjson is a fork of simplejson that fulfills my need of having a good
performance JSON encoder/decoder able to handle also Python's datetime
and UUID, even if with an admittedly non-standard and faulty heuristic
that was not considered within the scope of the original product.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: Not So Simple JSON encoder/decoder
Group: Development/Python3
%py3_provides %oname
%add_python3_req_skip UserDict

%description -n python3-module-%oname
nssjson is a (not so) simple, fast, complete, correct and extensible
JSON encoder and decoder for Python 2.5+ and Python 3.3+. It is pure
Python code with no dependencies, but includes an optional C extension
for a serious speed boost.

nssjson is a fork of simplejson that fulfills my need of having a good
performance JSON encoder/decoder able to handle also Python's datetime
and UUID, even if with an admittedly non-standard and faulty heuristic
that was not considered within the scope of the original product.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
nssjson is a (not so) simple, fast, complete, correct and extensible
JSON encoder and decoder for Python 2.5+ and Python 3.3+. It is pure
Python code with no dependencies, but includes an optional C extension
for a serious speed boost.

nssjson is a fork of simplejson that fulfills my need of having a good
performance JSON encoder/decoder able to handle also Python's datetime
and UUID, even if with an admittedly non-standard and faulty heuristic
that was not considered within the scope of the original product.

This package contains tests for %oname.
%endif

%prep
%setup

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
python setup.py test -v
%if_with python3
pushd ../python3
python3 setup.py test -v
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
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.7-alt1.git20150807.1
- NMU: Use buildreq for BR.

* Sat Aug 08 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.7-alt1.git20150807
- Initial build for Sisyphus

