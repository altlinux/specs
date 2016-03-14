%define oname lmfit

%def_with python3

Name: python-module-%oname
Version: 0.8.3
Release: alt1.git20150302.1.1
Summary: Least-Squares Minimization with Bounds and Constraints
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/lmfit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lmfit/lmfit-py.git
Source: %name-%version.tar
BuildArch: noarch

#BuildPreReq: python-devel python-module-setuptools-tests
#BuildPreReq: python-module-scipy libnumpy-devel
#BuildPreReq: python-module-nose xvfb-run python-module-matplotlib
#BuildPreReq: python-module-lxml python-module-pygobject3
#BuildPreReq: python-module-pycairo
#BuildPreReq: python-modules-json
#BuildPreReq: python-module-sphinx-devel ipython
%if_with python3
BuildRequires(pre): rpm-build-python3
#BuildPreReq: python3-devel python3-module-setuptools-tests
#BuildPreReq: python3-module-scipy libnumpy-py3-devel
#BuildPreReq: python3-module-nose python3-module-matplotlib
#BuildPreReq: python3-module-lxml python3-module-pygobject3
#BuildPreReq: python3-module-pycairo
%endif

%py_provides %oname
%py_requires json numpy scipy matplotlib lxml gi cairo

BuildRequires(pre): rpm-macros-sphinx
# Automatically added by buildreq on Thu Jan 28 2016 (-bi)
# optimized out: at-spi2-atk at-spi2-core colord dbus dbus-tools-gui fakeroot fontconfig fonts-bitmap-misc glib-networking gobject-introspection gobject-introspection-x11 ipython libat-spi2-core libatk-gir libcairo-gobject libcap-ng libgdk-pixbuf libgdk-pixbuf-gir libgpg-error libgtk+3-gir libpango-gir libwayland-client libwayland-cursor libwayland-egl libwayland-server python-base python-devel python-module-Pillow python-module-PyStemmer python-module-Pygments python-module-babel python-module-cffi python-module-chardet python-module-cryptography python-module-cssselect python-module-cycler python-module-dateutil python-module-decorator python-module-docutils python-module-enum34 python-module-functools32 python-module-future python-module-genshi python-module-greenlet python-module-ipykernel python-module-ipyparallel python-module-ipython_genutils python-module-jinja2 python-module-jinja2-tests python-module-jsonschema python-module-jupyter_client python-module-jupyter_core python-module-markupsafe python-module-matplotlib python-module-matplotlib-gtk3 python-module-mpmath python-module-nbconvert python-module-nbformat python-module-ndg-httpsclient python-module-ntlm python-module-numpy python-module-path python-module-pexpect python-module-pickleshare python-module-ptyprocess python-module-pyasn1 python-module-pycairo python-module-pycares python-module-pycurl python-module-pygobject3 python-module-pyparsing python-module-pytest python-module-pytz python-module-setuptools python-module-simplegeneric python-module-six python-module-snowballstemmer python-module-sphinx python-module-sphinx_rtd_theme python-module-terminado python-module-tornado_xstatic python-module-traitlets python-module-wx3.0 python-module-xstatic python-module-xstatic-term.js python-module-zmq python-module-zope.interface python-modules python-modules-compiler python-modules-ctypes python-modules-email python-modules-encodings python-modules-hotshot python-modules-json python-modules-logging python-modules-multiprocessing python-modules-sqlite3 python-modules-unittest python-modules-wsgiref python-modules-xml python3 python3-base python3-module-cssselect python3-module-cycler python3-module-dateutil python3-module-genshi python3-module-matplotlib-gtk3 python3-module-numpy python3-module-pyparsing python3-module-pytest python3-module-setuptools python3-module-six xauth xkbcomp xkeyboard-config xorg-server-common xorg-xvfb xz
BuildRequires: python-module-alabaster python-module-html5lib python-module-nose python-module-notebook python-module-numpy-testing python-module-numpydoc python-module-objects.inv python-module-scipy python-module-setuptools-tests python3-module-html5lib python3-module-matplotlib python3-module-nose python3-module-numpy-testing python3-module-pycairo python3-module-pygobject3 python3-module-scipy python3-module-setuptools-tests rpm-build-python3 time xvfb-run

%description
A library for least-squares minimization and data fitting in Python.
Built on top of scipy.optimize, lmfit provides a Parameter object which
can be set as fixed or free, can have upper and/or lower bounds, or can
be written in terms of algebraic constraints of other Parameters. The
user writes a function to be minimized as a function of these
Parameters, and the scipy.optimize methods are used to find the optimal
values for the Parameters. The Levenberg-Marquardt (leastsq) is the
default minimization algorithm, and provides estimated standard errors
and correlations between varied Parameters. Other minimization methods,
including Nelder-Mead's downhill simplex, Powell's method, BFGS,
Sequential Least Squares, and others are also supported. Bounds and
contraints can be placed on Parameters for all of these methods.

In addition, methods for explicitly calculating confidence intervals are
provided for exploring minmization problems where the approximation of
estimating Parameter uncertainties from the covariance matrix is
questionable.

%if_with python3
%package -n python3-module-%oname
Summary: Least-Squares Minimization with Bounds and Constraints
Group: Development/Python3
%py3_provides %oname
%py3_requires json numpy scipy matplotlib lxml gi cairo
%add_python3_req_skip UserDict

%description -n python3-module-%oname
A library for least-squares minimization and data fitting in Python.
Built on top of scipy.optimize, lmfit provides a Parameter object which
can be set as fixed or free, can have upper and/or lower bounds, or can
be written in terms of algebraic constraints of other Parameters. The
user writes a function to be minimized as a function of these
Parameters, and the scipy.optimize methods are used to find the optimal
values for the Parameters. The Levenberg-Marquardt (leastsq) is the
default minimization algorithm, and provides estimated standard errors
and correlations between varied Parameters. Other minimization methods,
including Nelder-Mead's downhill simplex, Powell's method, BFGS,
Sequential Least Squares, and others are also supported. Bounds and
contraints can be placed on Parameters for all of these methods.

In addition, methods for explicitly calculating confidence intervals are
provided for exploring minmization problems where the approximation of
estimating Parameter uncertainties from the covariance matrix is
questionable.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
A library for least-squares minimization and data fitting in Python.
Built on top of scipy.optimize, lmfit provides a Parameter object which
can be set as fixed or free, can have upper and/or lower bounds, or can
be written in terms of algebraic constraints of other Parameters. The
user writes a function to be minimized as a function of these
Parameters, and the scipy.optimize methods are used to find the optimal
values for the Parameters. The Levenberg-Marquardt (leastsq) is the
default minimization algorithm, and provides estimated standard errors
and correlations between varied Parameters. Other minimization methods,
including Nelder-Mead's downhill simplex, Powell's method, BFGS,
Sequential Least Squares, and others are also supported. Bounds and
contraints can be placed on Parameters for all of these methods.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
A library for least-squares minimization and data fitting in Python.
Built on top of scipy.optimize, lmfit provides a Parameter object which
can be set as fixed or free, can have upper and/or lower bounds, or can
be written in terms of algebraic constraints of other Parameters. The
user writes a function to be minimized as a function of these
Parameters, and the scipy.optimize methods are used to find the optimal
values for the Parameters. The Levenberg-Marquardt (leastsq) is the
default minimization algorithm, and provides estimated standard errors
and correlations between varied Parameters. Other minimization methods,
including Nelder-Mead's downhill simplex, Powell's method, BFGS,
Sequential Least Squares, and others are also supported. Bounds and
contraints can be placed on Parameters for all of these methods.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|@VERSION@|%version|' %oname/_version.py

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx .
ln -s ../objects.inv doc/

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

export PYTHONPATH=%buildroot%python_sitelibdir
xvfb-run make -C doc pickle
xvfb-run make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
xvfb-run nosetests -v
%if_with python3
pushd ../python3
python3 setup.py test
xvfb-run nosetests3 -v
popd
%endif

%files
%doc *.rst THANKS.txt examples
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst THANKS.txt examples
%python3_sitelibdir/*
%endif

%changelog
* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.8.3-alt1.git20150302.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.8.3-alt1.git20150302.1
- NMU: Use buildreq for BR.

* Tue Mar 03 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.3-alt1.git20150302
- Version 0.8.3
- Added module for Python 3

* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20141121
- Initial build for Sisyphus

