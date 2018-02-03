%define oname cdecimal

%def_with python3
%def_disable check

Name: python-module-%oname
Version: 2.3
Release: alt1.git20140923.1.1
Summary: Fast drop-in replacement for decimal.py
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/cdecimal/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/midlgxdev/cdecimal-2.3.git
Source: %name-%version.tar

BuildPreReq: python-devel python-module-setuptools
BuildPreReq: libgmp-devel dejagnu python-test
BuildPreReq: python-module-coverage python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-coverage python3-module-nose
BuildPreReq: python3-test
%endif

%py_provides %oname
Requires: libmpdec = %EVR

%description
Please note: cdecimal has been integrated into CPython 3.3, where it
supersedes the pure Python version: import decimal will automatically
import the C version. Performance has been improved further, so the
cdecimal version shipped with CPython 3.3 is significantly faster for
numerical workload than cdecimal-2.3. If you need maximum decimal
computing performance, you should solely use that Python version.

cdecimal is a fast drop-in replacement for the decimal module in
Python's standard library for Python versions 2.5 up to 3.2. It provides
a complete implementation of Mike Cowlishaw/IBM's General Decimal
Arithmetic Specification.

%package -n libmpdec
Summary: Shared library for %oname
Group: System/Libraries

%description -n libmpdec
Please note: cdecimal has been integrated into CPython 3.3, where it
supersedes the pure Python version: import decimal will automatically
import the C version. Performance has been improved further, so the
cdecimal version shipped with CPython 3.3 is significantly faster for
numerical workload than cdecimal-2.3. If you need maximum decimal
computing performance, you should solely use that Python version.

This package contains shared library for %oname.

%package -n libmpdec-devel
Summary: Shared library for %oname
Group: Development/C
Requires: libmpdec = %EVR

%description -n libmpdec-devel
Please note: cdecimal has been integrated into CPython 3.3, where it
supersedes the pure Python version: import decimal will automatically
import the C version. Performance has been improved further, so the
cdecimal version shipped with CPython 3.3 is significantly faster for
numerical workload than cdecimal-2.3. If you need maximum decimal
computing performance, you should solely use that Python version.

This package contains documentation for for libmpdec.

%package -n python3-module-%oname
Summary: Fast drop-in replacement for decimal.py
Group: Development/Python3
%py3_provides %oname
Requires: libmpdec = %EVR

%description -n python3-module-%oname
Please note: cdecimal has been integrated into CPython 3.3, where it
supersedes the pure Python version: import decimal will automatically
import the C version. Performance has been improved further, so the
cdecimal version shipped with CPython 3.3 is significantly faster for
numerical workload than cdecimal-2.3. If you need maximum decimal
computing performance, you should solely use that Python version.

cdecimal is a fast drop-in replacement for the decimal module in
Python's standard library for Python versions 2.5 up to 3.2. It provides
a complete implementation of Mike Cowlishaw/IBM's General Decimal
Arithmetic Specification.

%prep
%setup

%autoreconf

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags %optflags_shared -DANSI=1
%configure
%make_build
%python_build_debug

%if_with python3
pushd ../python3
%configure
%make_build
%python3_build_debug
popd
%endif

%install
%makeinstall_std
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

ln -s libmpdec.so.%version %buildroot%_libdir/libmpdec.so

%check
python setup.py test
%make coverage
%if_with python3
pushd ../python3
python3 setup.py test
%make coverage
popd
%endif

%files
%doc *.txt
%python_sitelibdir/*

%files -n libmpdec
%_libdir/*.so.*

%files -n libmpdec-devel
%_includedir/*
%_libdir/*.so

%if_with python3
%files -n python3-module-%oname
%doc *.txt
%python3_sitelibdir/*
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 2.3-alt1.git20140923.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 2.3-alt1.git20140923.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Oct 20 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 2.3-alt1.git20140923
- Initial build for Sisyphus

