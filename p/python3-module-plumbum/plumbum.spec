%define oname plumbum

Name: python3-module-%oname
Version: 1.6.3
Release: alt2
Summary: Plumbum: shell combinators library
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/plumbum/

# https://github.com/tomerfiliba/plumbum.git
Source: %name-%version.tar
Patch1: %oname-%version-alt-docs.patch
BuildArch: noarch

BuildRequires(pre): rpm-build-python3 rpm-macros-sphinx3
BuildRequires: python3-module-setuptools python3-module-sphinx /usr/bin/2to3

%py3_provides %oname

%description
Ever wished the compactness of shell scripts be put into a real
programming language? Say hello to Plumbum Shell Combinators. Plumbum
(Latin for lead, which was used to create pipes back in the day) is a
small yet feature-rich library for shell script-like programs in Python.
The motto of the library is "Never write shell scripts again", and thus
it attempts to mimic the shell syntax ("shell combinators") where it
makes sense, while keeping it all Pythonic and cross-platform.

Apart from shell-like syntax and handy shortcuts, the library provides
local and remote command execution (over SSH), local and remote
file-system paths, easy working-directory and environment manipulation,
and a programmatic Command-Line Interface (CLI) application toolkit. Now
let's see some code!

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
Ever wished the compactness of shell scripts be put into a real
programming language? Say hello to Plumbum Shell Combinators. Plumbum
(Latin for lead, which was used to create pipes back in the day) is a
small yet feature-rich library for shell script-like programs in Python.
The motto of the library is "Never write shell scripts again", and thus
it attempts to mimic the shell syntax ("shell combinators") where it
makes sense, while keeping it all Pythonic and cross-platform.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
Ever wished the compactness of shell scripts be put into a real
programming language? Say hello to Plumbum Shell Combinators. Plumbum
(Latin for lead, which was used to create pipes back in the day) is a
small yet feature-rich library for shell script-like programs in Python.
The motto of the library is "Never write shell scripts again", and thus
it attempts to mimic the shell syntax ("shell combinators") where it
makes sense, while keeping it all Pythonic and cross-platform.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Ever wished the compactness of shell scripts be put into a real
programming language? Say hello to Plumbum Shell Combinators. Plumbum
(Latin for lead, which was used to create pipes back in the day) is a
small yet feature-rich library for shell script-like programs in Python.
The motto of the library is "Never write shell scripts again", and thus
it attempts to mimic the shell syntax ("shell combinators") where it
makes sense, while keeping it all Pythonic and cross-platform.

This package contains documentation for %oname.

%prep
%setup
%patch1 -p1

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%python3_build_debug

%install
%python3_install
touch experiments/__init__.py
cp -fR experiments %buildroot%python3_sitelibdir/%oname/
find %buildroot%python3_sitelibdir/%oname/experiments \
	-type f -name '*.py' -exec 2to3 -w -n '{}' +

%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
python3 setup.py test ||:

%files
%doc examples *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle
%exclude %python3_sitelibdir/*/*/test*

%files tests
%python3_sitelibdir/*/*/test*

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Thu Sep 03 2020 Grigory Ustinov <grenka@altlinux.org> 1.6.3-alt2
- Drop python2 support.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.6.3-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Mon Aug 14 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 1.6.3-alt1
- Updated to upstream version 1.6.3.

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.4.3-alt1.git20141103.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 1.4.3-alt1.git20141103.1
- NMU: Use buildreq for BR.

* Fri Nov 07 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.4.3-alt1.git20141103
- Initial build for Sisyphus

