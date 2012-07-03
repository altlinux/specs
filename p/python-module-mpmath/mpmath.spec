%define oname mpmath

%def_with python3

Name: python-module-%oname
Version: 0.17
Release: alt2
Summary: Python library for arbitrary-precision floating-point arithmetic
License: New BSD License
Group: Development/Python
Url: http://code.google.com/p/mpmath/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

Source: %oname-all-%version.tar

BuildRequires(pre): rpm-build-python
BuildPreReq: python-devel python-module-gmpy python-module-matplotlib
BuildPreReq: python-module-sphinx-devel python-module-Pygments
BuildPreReq: texlive-latex-recommended
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-devel python3-module-gmpy python-tools-2to3
%endif

BuildArch: noarch

%description
Mpmath is a pure-Python library for multiprecision floating-point
arithmetic. It provides an extensive set of transcendental functions,
unlimited exponent sizes, complex numbers, interval arithmetic,
numerical integration and differentiation, root-finding, linear algebra,
and much more. Almost any calculation can be performed just as well at
10-digit or 1000-digit precision, and in many cases mpmath implements
asymptotically fast algorithms that scale well for extremely high
precision work. Mpmath internally uses Python's builtin long integers by
default, but automatically switches to GMP/MPIR for much faster
high-precision arithmetic if gmpy is installed.

If matplotlib is available, mpmath also provides a convenient plotting
interface.

%if_with python3
%package -n python3-module-%oname
Summary: Python 3 library for arbitrary-precision floating-point arithmetic
Group: Development/Python3

%description -n python3-module-%oname
Mpmath is a pure-Python library for multiprecision floating-point
arithmetic. It provides an extensive set of transcendental functions,
unlimited exponent sizes, complex numbers, interval arithmetic,
numerical integration and differentiation, root-finding, linear algebra,
and much more. Almost any calculation can be performed just as well at
10-digit or 1000-digit precision, and in many cases mpmath implements
asymptotically fast algorithms that scale well for extremely high
precision work. Mpmath internally uses Python's builtin long integers by
default, but automatically switches to GMP/MPIR for much faster
high-precision arithmetic if gmpy is installed.

If matplotlib is available, mpmath also provides a convenient plotting
interface.
%endif

%package doc
Summary: Documentation and demos for Mpmath
Group: Development/Documentation

%description doc
Mpmath is a pure-Python library for multiprecision floating-point
arithmetic. It provides an extensive set of transcendental functions,
unlimited exponent sizes, complex numbers, interval arithmetic,
numerical integration and differentiation, root-finding, linear algebra,
and much more. Almost any calculation can be performed just as well at
10-digit or 1000-digit precision, and in many cases mpmath implements
asymptotically fast algorithms that scale well for extremely high
precision work. Mpmath internally uses Python's builtin long integers by
default, but automatically switches to GMP/MPIR for much faster
high-precision arithmetic if gmpy is installed.

This package contains documentation and demos for Mpmath.

%package pickles
Summary: Pickles for Mpmath
Group: Development/Python

%description pickles
Mpmath is a pure-Python library for multiprecision floating-point
arithmetic. It provides an extensive set of transcendental functions,
unlimited exponent sizes, complex numbers, interval arithmetic,
numerical integration and differentiation, root-finding, linear algebra,
and much more. Almost any calculation can be performed just as well at
10-digit or 1000-digit precision, and in many cases mpmath implements
asymptotically fast algorithms that scale well for extremely high
precision work. Mpmath internally uses Python's builtin long integers by
default, but automatically switches to GMP/MPIR for much faster
high-precision arithmetic if gmpy is installed.

This package contains pickles for Mpmath.

%prep
%setup
%if_with python3
rm -rf ../python3
cp -a . ../python3
%endif

%build
%python_build
%if_with python3
pushd ../python3
#for i in $(find ./ -name '*.py'); do
#	2to3 -w -n $i
#done
%python3_build
popd
%endif

pushd doc
python build.py
sphinx-build -b pickle -E source pickle
popd

%install
%python_install
%if_with python3
pushd ../python3
%python3_install
popd
%endif

cp -fR doc/pickle %buildroot%python_sitelibdir/%oname/

%check
export PYTHONPATH=%buildroot%python_sitelibdir
python mpmath/tests/runtests.py

%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
python mpmath/tests/runtests.py
popd
%endif

%files
%doc CHANGES LICENSE README
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/libmp/exec_py3.py*

%files doc
%doc doc/build/* demo

%files pickles
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/libmp/exec_py2.py*
%endif

%changelog
* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.17-alt1.1
- Rebuild with Python-2.7

* Wed Apr 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1
- Initial build for Sisyphus

