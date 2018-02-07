%define oname amqpy
Name: python3-module-%oname
Version: 0.12.4
Release: alt1.git20160226.1.1
Summary: Pure-Python 3 AMQP client library
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/amqpy/

# https://github.com/veegee/amqpy.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python-module-sphinx-devel python3-module-sphinx

%py_provides %oname

%description
amqpy is a pure-Python AMQP 0.9.1 client library for Python >= 3.2.0
(including PyPy3) with a focus on:

* stability and reliability
* well-tested and thoroughly documented code
* clean, correct design
* 100%% compliance with the AMQP 0.9.1 protocol specification

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
amqpy is a pure-Python AMQP 0.9.1 client library for Python >= 3.2.0
(including PyPy3) with a focus on:

* stability and reliability
* well-tested and thoroughly documented code
* clean, correct design
* 100%% compliance with the AMQP 0.9.1 protocol specification

This package contains tests for %oname.

%prep
%setup

%prepare_sphinx docs
ln -s ../objects.inv docs/source/

%build
%python3_build_debug

%install
%python3_install

%make -C docs html
mv docs/build/html docs_html

%check
python3 setup.py test

%files
%doc AUTHORS *.rst docs_html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%changelog
* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.12.4-alt1.git20160226.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Mar 14 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.12.4-alt1.git20160226.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Fri Feb 26 2016 Denis Medvedev <nbr@altlinux.org> 0.12.4-alt1.git20160226
- New version.

* Mon Feb 16 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.4-alt1.git20150215
- Version 0.9.4

* Wed Jan 14 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.9.3-alt1.git20150113
- Initial build for Sisyphus

