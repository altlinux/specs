%define oname algopy

Name: python3-module-%oname
Version: 0.5.7
Release: alt1

Summary: ALGOPY: Taylor Arithmetic Computation and Algorithmic Differentiation
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/algopy

# https://github.com/b45ch1/algopy.git
Source: %name-%version.tar
Patch1: fix_test_import_of_deprecated_decorators_module.patch

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-scipy
BuildRequires: python3-module-sphinx

%py3_provides %oname
%py3_requires numpy scipy

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
Group: Development/Python3
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
%patch1 -p1

sed -i 's|sphinx-build|&-3|' documentation/sphinx/Makefile

%build
export PYTHONPATH=$PWD
%make -C documentation/sphinx pickle

%python3_build_debug

%install
%python3_install

cp -fR documentation/sphinx/_build/pickle \
	%buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test -v ||:
%__python3 run_tests.py -v ||:

%files
%doc *.rst documentation/examples documentation/getting_started.py
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc documentation/AD_tutorial_TU_Berlin
%doc documentation/ICCS2010
%doc documentation/*.pdf

%changelog
* Tue Feb 14 2023 Grigory Ustinov <grenka@altlinux.org> 0.5.7-alt1
- Build new version.

* Wed Aug 26 2020 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5.3-alt3
- Fixed build with new numpy.

* Thu Apr 02 2020 Andrey Bychkov <mrdrew@altlinux.org> 0.5.3-alt2
- Build for python2 disabled.

* Wed Jan 09 2019 Mikhail Gordeev <obirvalger@altlinux.org> 0.5.3-alt1.git20150630.3
- Fix tests passing. Tests use deprecated module numpy.testing.decorators, very
  likely tests will not pass with next numpy upgrade and tests must be disabled.

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

