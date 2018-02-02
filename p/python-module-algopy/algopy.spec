%define oname algopy

%def_with python3

Name: python-module-%oname
Version: 0.5.3
Release: alt1.git20150630.2.1
Summary: ALGOPY: Taylor Arithmetic Computation and Algorithmic Differentiation
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/algopy

# https://github.com/b45ch1/algopy.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: time python-module-alabaster python-module-docutils python-module-html5lib python-module-matplotlib
BuildRequires: python-module-nose python-module-numpy-testing python-module-objects.inv python-module-scipy
BuildRequires: python-module-setuptools
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-nose python3-module-numpy-testing python3-module-scipy python3-module-setuptools
%endif

%py_provides %oname
%py_requires numpy scipy

%description
ALGOPY is a tool for Algorithmic Differentiation (AD) and Taylor
polynomial approximations. ALGOPY makes it possible to perform
computations on scalar and polynomial matrices. It is designed to be as
compatible to numpy as possible. I.e. views, broadcasting and most
functions of numpy can be performed on polynomial matrices. Exampels are
dot,trace,qr,solve, inv,eigh. The reverse mode of AD is also supported
by a simple code evaluation tracer.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
ALGOPY is a tool for Algorithmic Differentiation (AD) and Taylor
polynomial approximations. ALGOPY makes it possible to perform
computations on scalar and polynomial matrices. It is designed to be as
compatible to numpy as possible. I.e. views, broadcasting and most
functions of numpy can be performed on polynomial matrices. Exampels are
dot,trace,qr,solve, inv,eigh. The reverse mode of AD is also supported
by a simple code evaluation tracer.

This package contains tests for %oname.

%if_with python3
%package -n python3-module-%oname
Summary: ALGOPY: Taylor Arithmetic Computation and Algorithmic Differentiation
Group: Development/Python3
%py3_provides %oname
%py3_requires numpy scipy

%description -n python3-module-%oname
ALGOPY is a tool for Algorithmic Differentiation (AD) and Taylor
polynomial approximations. ALGOPY makes it possible to perform
computations on scalar and polynomial matrices. It is designed to be as
compatible to numpy as possible. I.e. views, broadcasting and most
functions of numpy can be performed on polynomial matrices. Exampels are
dot,trace,qr,solve, inv,eigh. The reverse mode of AD is also supported
by a simple code evaluation tracer.

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
ALGOPY is a tool for Algorithmic Differentiation (AD) and Taylor
polynomial approximations. ALGOPY makes it possible to perform
computations on scalar and polynomial matrices. It is designed to be as
compatible to numpy as possible. I.e. views, broadcasting and most
functions of numpy can be performed on polynomial matrices. Exampels are
dot,trace,qr,solve, inv,eigh. The reverse mode of AD is also supported
by a simple code evaluation tracer.

This package contains tests for %oname.
%endif

%package pickles
Summary: Pickles for %oname
Group: Development/Python

%description pickles
ALGOPY is a tool for Algorithmic Differentiation (AD) and Taylor
polynomial approximations. ALGOPY makes it possible to perform
computations on scalar and polynomial matrices. It is designed to be as
compatible to numpy as possible. I.e. views, broadcasting and most
functions of numpy can be performed on polynomial matrices. Exampels are
dot,trace,qr,solve, inv,eigh. The reverse mode of AD is also supported
by a simple code evaluation tracer.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
ALGOPY is a tool for Algorithmic Differentiation (AD) and Taylor
polynomial approximations. ALGOPY makes it possible to perform
computations on scalar and polynomial matrices. It is designed to be as
compatible to numpy as possible. I.e. views, broadcasting and most
functions of numpy can be performed on polynomial matrices. Exampels are
dot,trace,qr,solve, inv,eigh. The reverse mode of AD is also supported
by a simple code evaluation tracer.

This package contains documentation for %oname.

%prep
%setup

%if_with python3
cp -fR . ../python3
%endif

%prepare_sphinx documentation
ln -s ../objects.inv documentation/sphinx/

%build
%python_build_debug

export PYTHONPATH=$PWD
python setup.py build_sphinx
%make -C documentation/sphinx pickle

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

cp -fR documentation/sphinx/_build/pickle \
	%buildroot%python_sitelibdir/%oname/

%check
python setup.py test -v
python run_tests.py -v
%if_with python3
pushd ../python3
python3 setup.py test -v ||:
python3 run_tests.py -v ||:
popd
%endif

%files
%doc *.rst documentation/examples documentation/getting_started.py
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests
%exclude %python_sitelibdir/*/*/tests

%files tests
%python_sitelibdir/*/tests
%python_sitelibdir/*/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc documentation/AD_tutorial_TU_Berlin
%doc documentation/ICCS2010
%doc documentation/*.pdf
%doc documentation/sphinx/_build/html

%if_with python3
%files -n python3-module-%oname
%doc *.rst documentation/examples documentation/getting_started.py
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests
%endif

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5.3-alt1.git20150630.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Aug 03 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.3-alt1.git20150630.2
- Fixed build.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5.3-alt1.git20150630.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.5.3-alt1.git20150630.1
- NMU: Use buildreq for BR.

* Sun Aug 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5.3-alt1.git20150630
- Initial build for Sisyphus

