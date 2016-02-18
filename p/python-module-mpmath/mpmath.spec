%define oname mpmath

%def_with python3

Name: python-module-%oname
Version: 0.19
Release: alt1.git20150621.1
Summary: Python library for arbitrary-precision floating-point arithmetic
License: New BSD License
Group: Development/Python
Url: http://mpmath.org/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/fredrik-johansson/mpmath.git
Source: %oname-all-%version.tar

BuildRequires(pre): rpm-build-python
#BuildPreReq: python-devel python-module-gmpy python-module-matplotlib
#BuildPreReq: python-module-sphinx-devel python-module-Pygments
#BuildPreReq: python-module-pygobject3 python-module-pycairo
#BuildPreReq: texlive-latex-recommended xvfb-run
%if_with python3
BuildRequires(pre): rpm-build-python3
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: at-spi2-atk at-spi2-core colord dbus dbus-tools-gui fakeroot fontconfig fonts-bitmap-misc glib-networking gobject-introspection gobject-introspection-x11 libat-spi2-core libatk-gir libcairo-gobject libcap-ng libgdk-pixbuf libgdk-pixbuf-gir libgpg-error libgtk+3-gir libpango-gir libwayland-client libwayland-cursor libwayland-egl libwayland-server python-base python-devel python-module-PyStemmer python-module-Pygments python-module-babel python-module-cssselect python-module-cycler python-module-dateutil python-module-jinja2 python-module-jinja2-tests python-module-markupsafe python-module-matplotlib-gtk3 python-module-numpy python-module-pyparsing python-module-pytz python-module-setuptools python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-json python-modules-logging python-modules-multiprocessing python-modules-unittest python3 python3-base shared-mime-info xauth xkbcomp xkeyboard-config xorg-server-common xorg-xvfb
BuildRequires: fonts-type1-urw python-module-alabaster python-module-docutils python-module-gmpy python-module-html5lib python-module-matplotlib python-module-numpy-testing python-module-pycairo python-module-pygobject3 rpm-build-python3 time xvfb-run

#BuildRequires: python3-devel python3-module-gmpy python-tools-2to3
#BuildPreReq: python3-module-matplotlib python3-module-pycairo
#BuildPreReq: python3-module-pygobject3
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

%package tests
Summary: Tests for Mpmath
Group: Development/Python
Requires: %name = %EVR

%description tests
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

This package contains tests for Mpmath.

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

%package -n python3-module-%oname-tests
Summary: Tests for Mpmath
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
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

This package contains tests for Mpmath.
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
xvfb-run python mpmath/tests/runtests.py

%if_with python3
pushd ../python3
export PYTHONPATH=%buildroot%python3_sitelibdir
xvfb-run python mpmath/tests/runtests.py
popd
%endif

%files
%doc CHANGES LICENSE README*
%python_sitelibdir/*
%exclude %python_sitelibdir/%oname/pickle
%exclude %python_sitelibdir/%oname/tests
#exclude %python_sitelibdir/%oname/libmp/exec_py3.py*

%files tests
%python_sitelibdir/%oname/tests

%files doc
%doc doc/build/* demo

%files pickles
%python_sitelibdir/%oname/pickle

%if_with python3
%files -n python3-module-%oname
%doc CHANGES LICENSE README*
%python3_sitelibdir/*
%exclude %python3_sitelibdir/%oname/tests
#exclude %python3_sitelibdir/%oname/libmp/exec_py2.py*

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.19-alt1.git20150621.1
- NMU: Use buildreq for BR.

* Mon Aug 31 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.19-alt1.git20150621
- Version 0.19

* Mon Jul 14 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.18-alt1
- Version 0.18

* Fri Mar 22 2013 Aleksey Avdeev <solo@altlinux.ru> 0.17-alt2.1
- Rebuild with Python-3.3

* Sat May 12 2012 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt2
- Added module for Python 3

* Mon Oct 24 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 0.17-alt1.1
- Rebuild with Python-2.7

* Wed Apr 06 2011 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.17-alt1
- Initial build for Sisyphus

