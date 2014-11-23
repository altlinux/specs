%define oname lmfit

%def_without python3

Name: python-module-%oname
Version: 0.8.1
Release: alt1.git20141121
Summary: Least-Squares Minimization with Bounds and Constraints
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/lmfit/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/lmfit/lmfit-py.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools-tests
BuildPreReq: python-module-scipy libnumpy-devel
BuildPreReq: python-module-nose xvfb-run
BuildPreReq: python-module-sphinx-devel ipython
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools-tests
BuildPreReq: python3-module-scipy libnumpy-py3-devel
BuildPreReq: python3-module-nose python3-module-matplotlib
%endif

%py_provides %oname

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

%package -n python3-module-%oname
Summary: Least-Squares Minimization with Bounds and Constraints
Group: Development/Python3
%py3_provides %oname

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
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
python setup.py test
xvfb-run nosetests
%if_with python3
pushd ../python3
python3 setup.py test
#xvfb-run nosetests3
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
* Sun Nov 23 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.8.1-alt1.git20141121
- Initial build for Sisyphus

