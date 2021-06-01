%define oname pymlconf

%def_without check

Name: python3-module-%oname
Version: 0.3.11
Release: alt2.git20140603
Summary: Python high level configuration library
License: Free
Group: Development/Python3
Url: https://pypi.python.org/pypi/pymlconf/

# https://github.com/pylover/pymlconf.git
Source: %name-%version.tar
BuildArch: noarch

BuildRequires(pre): rpm-build-python3

%py3_provides %oname

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-pytest python3-module-yaml rpm-build-python3
BuildRequires: python3-module-sphinx

%description
pymlconf (Python YAML Configuration Library) helps to easily manage and
access to your application configurations which was already Written in
YAML language.

It can merge two or more configuration files according their names and
automatically treat file-names as namespaces, or simply merge several
parts of configuration(YAML-string or Python-dict) on arbitrary config
node.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
pymlconf (Python YAML Configuration Library) helps to easily manage and
access to your application configurations which was already Written in
YAML language.

It can merge two or more configuration files according their names and
automatically treat file-names as namespaces, or simply merge several
parts of configuration(YAML-string or Python-dict) on arbitrary config
node.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
pymlconf (Python YAML Configuration Library) helps to easily manage and
access to your application configurations which was already Written in
YAML language.

It can merge two or more configuration files according their names and
automatically treat file-names as namespaces, or simply merge several
parts of configuration(YAML-string or Python-dict) on arbitrary config
node.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pymlconf (Python YAML Configuration Library) helps to easily manage and
access to your application configurations which was already Written in
YAML language.

It can merge two or more configuration files according their names and
automatically treat file-names as namespaces, or simply merge several
parts of configuration(YAML-string or Python-dict) on arbitrary config
node.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx3 .
ln -s ../objects.inv doc/

%build
%python3_build

%install
%python3_install

%make SPHINXBUILD="sphinx-build-3" -C doc pickle
%make SPHINXBUILD="sphinx-build-3" -C doc html

cp -fR doc/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
python3 setup.py test

%files
%doc README.html
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%changelog
* Tue Jun 01 2021 Grigory Ustinov <grenka@altlinux.org> 0.3.11-alt2.git20140603
- Drop python2 support.
- Build without check.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.3.11-alt1.git20140603.1.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.3.11-alt1.git20140603.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 0.3.11-alt1.git20140603.1
- NMU: Use buildreq for BR.

* Tue Nov 04 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.11-alt1.git20140603
- Initial build for Sisyphus

