%define pname bitcoin
%define oname %{pname}lib

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 0.3.1
Release: alt1.git20150110.1.1
Summary: Provides an easy interface to the Bitcoin data structures and protocol
License: LGPLv3+
Group: Development/Python
Url: https://pypi.python.org/pypi/python-bitcoinlib/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/petertodd/python-bitcoinlib.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: libssl-devel
#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-modules-json
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
%endif

Provides: python-module-%pname = %EVR
%py_provides %pname
%py_requires json

# Automatically added by buildreq on Wed Jan 27 2016 (-bi)
# optimized out: python-base python-devel python-module-setuptools python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-unittest python3 python3-base python3-module-setuptools
BuildRequires: python-module-pytest python3-module-pytest rpm-build-python3

%description
This Python2/3 library provides an easy interface to the bitcoin data
structures and protocol. The approach is low-level and "ground up", with
a focus on providing tools to manipulate the internals of how Bitcoin
works.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
This Python2/3 library provides an easy interface to the bitcoin data
structures and protocol. The approach is low-level and "ground up", with
a focus on providing tools to manipulate the internals of how Bitcoin
works.

This package contains tests for %oname.

%package -n python3-module-%oname
Summary: Provides an easy interface to the Bitcoin data structures and protocol
Group: Development/Python3
Provides: python3-module-%pname = %EVR
%py3_provides %pname
%py3_requires json

%description -n python3-module-%oname
This Python2/3 library provides an easy interface to the bitcoin data
structures and protocol. The approach is low-level and "ground up", with
a focus on providing tools to manipulate the internals of how Bitcoin
works.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This Python2/3 library provides an easy interface to the bitcoin data
structures and protocol. The approach is low-level and "ground up", with
a focus on providing tools to manipulate the internals of how Bitcoin
works.

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
python setup.py test
%if_with python3
pushd ../python3
python3 setup.py test
popd
%endif

%files
%doc README *.md examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%if_with python3
%files -n python3-module-%oname
%doc README *.md examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.1-alt1.git20150110.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.1-alt1.git20150110.1
- NMU: Use buildreq for BR.

* Sat Jan 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20150110
- Initial build for Sisyphus

