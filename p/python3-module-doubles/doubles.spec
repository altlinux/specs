%define oname doubles

%def_disable check

Name: python3-module-%oname
Version: 1.0.5
Release: alt2

Summary: Test doubles for Python
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/doubles/

BuildArch: noarch

# https://github.com/uber/doubles.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: python3-module-sphinx
BuildRequires: python3-module-sphinx_rtd_theme
BuildRequires: python3-module-pytest


%description
Doubles is a Python package that provides test doubles for use in
automated tests.

It provides functionality for stubbing, mocking, and verification of
test doubles against the real objects they double. In contrast to the
Mock package, it provides a clear, expressive syntax and better safety
guarantees to prevent API drift and to improve confidence in tests using
doubles. It comes with drop-in support for test suites run by Pytest,
Nose, or standard unittest.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Doubles is a Python package that provides test doubles for use in
automated tests.

It provides functionality for stubbing, mocking, and verification of
test doubles against the real objects they double. In contrast to the
Mock package, it provides a clear, expressive syntax and better safety
guarantees to prevent API drift and to improve confidence in tests using
doubles. It comes with drop-in support for test suites run by Pytest,
Nose, or standard unittest.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Doubles is a Python package that provides test doubles for use in
automated tests.

It provides functionality for stubbing, mocking, and verification of
test doubles against the real objects they double. In contrast to the
Mock package, it provides a clear, expressive syntax and better safety
guarantees to prevent API drift and to improve confidence in tests using
doubles. It comes with drop-in support for test suites run by Pytest,
Nose, or standard unittest.

This package contains documentation for %oname.

%prep
%setup

sed -i 's|sphinx-build|sphinx-build-3|' docs/Makefile

%build
%python3_build_debug

%install
%python3_install

export PYTHONPATH=$PWD
%make -C docs pickle
%make -C docs html

cp -fR docs/build/pickle %buildroot%python3_sitelibdir/%oname/

%check
%__python3 setup.py test

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/build/html/*


%changelog
* Thu Feb 20 2020 Andrey Bychkov <mrdrew@altlinux.org> 1.0.5-alt2
- Build for python2 disabled.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.0.5-alt1.git20150205.1.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon May 23 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.5-alt1.git20150205.1.1.1
- BR: sphinx_rtd_theme (the theme is optional since sphinx-1.4.1).

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.5-alt1.git20150205.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.0.5-alt1.git20150205.1
- NMU: Use buildreq for BR.

* Wed Feb 11 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.5-alt1.git20150205
- Initial build for Sisyphus

