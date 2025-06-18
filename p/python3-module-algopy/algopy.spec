%define oname algopy

%def_with check
%def_with docs

Name: python3-module-%oname
Version: 0.7.2
Release: alt1

Summary: ALGOPY: Taylor Arithmetic Computation and Algorithmic Differentiation
License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/algopy
Vcs: https://github.com/b45ch1/algopy.git

Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
%if_with check
BuildRequires: python3-module-pytest
BuildRequires: python3-module-numpy-testing
BuildRequires: python3-module-scipy
%endif
%if_with docs
BuildRequires: python3-module-sphinx
%endif

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

rm -rf pyproject.toml

%if_with docs
sed -i 's|sphinx-build|&-3|' documentation/sphinx/Makefile
%endif

%build
%if_with docs
export PYTHONPATH=$PWD
%make -C documentation/sphinx pickle
%endif

%pyproject_build

%install
%pyproject_install

%if_with docs
cp -fR documentation/sphinx/_build/pickle \
	%buildroot%python3_sitelibdir/%oname/
%endif

%check
export PYTHONPATH=%buildroot%python3_sitelibdir
%__python3 run_tests.py

%files
%doc *.rst documentation/examples documentation/getting_started.py
%python3_sitelibdir/%oname
%python3_sitelibdir/%{pyproject_distinfo %oname}
%exclude %python3_sitelibdir/*/tests
%exclude %python3_sitelibdir/*/*/tests
%if_with docs
%exclude %python3_sitelibdir/*/pickle
%endif

%files tests
%python3_sitelibdir/*/tests
%python3_sitelibdir/*/*/tests

%if_with docs
%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc documentation/AD_tutorial_TU_Berlin
%doc documentation/ICCS2010
%doc documentation/*.pdf
%endif

%changelog
* Wed Jun 18 2025 Anton Vyatkin <toni@altlinux.org> 0.7.2-alt1
- New version 0.7.2.

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

