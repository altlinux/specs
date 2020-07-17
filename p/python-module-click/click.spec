%define oname click

Name: python-module-%oname
Version: 7.0
Release: alt2

Summary: A simple wrapper around optparse for powerful command line utilities
License: BSD
Group: Development/Python

Url: https://pypi.python.org/pypi/click/
# Source-git: https://github.com/mitsuhiko/click.git
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-macros-sphinx
BuildRequires: python-module-pallets-sphinx-themes

%py_provides %oname


%description
Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary.  It's the "Command
Line Interface Creation Kit".  It's highly configurable but comes with
sensible defaults out of the box.

It aims to make the process of writing command line tools quick and fun
while also preventing any frustration caused by the inability to
implement an intended CLI API.

%package tests
Summary: Tests for %oname
Group: Development/Python
Requires: %name = %EVR

%description tests
Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary.  It's the "Command
Line Interface Creation Kit".  It's highly configurable but comes with
sensible defaults out of the box.

It aims to make the process of writing command line tools quick and fun
while also preventing any frustration caused by the inability to
implement an intended CLI API.

This package contains tests for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
Click is a Python package for creating beautiful command line interfaces
in a composable way with as little code as necessary.  It's the "Command
Line Interface Creation Kit".  It's highly configurable but comes with
sensible defaults out of the box.

It aims to make the process of writing command line tools quick and fun
while also preventing any frustration caused by the inability to
implement an intended CLI API.

This package contains documentation for %oname.

%prep
%setup
rm -fv click/_winconsole.py

%build
%python_build_debug

export PYTHONPATH=$PWD
%make -C docs/ man

%install
%python_install

%check
python setup.py test

%files
%doc README.* LICENSE.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/test*

%files tests
%python_sitelibdir/*/test*

%files docs
%doc docs/*/man/*

%changelog
* Fri Jul 17 2020 Sergey Bolshakov <sbolshakov@altlinux.ru> 7.0-alt2
- rebuilt without python3

* Mon Jul 01 2019 Andrey Bychkov <mrdrew@altlinux.org> 7.0-alt1
- Version updated to 7.0

* Tue Apr 23 2019 Michael Shigorin <mike@altlinux.org> 6.7-alt1.1.1
- introduce doc knob (on by default)

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 6.7-alt1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Sun Dec 24 2017 Vitaly Lipatov <lav@altlinux.ru> 6.7-alt1
- new version 6.7 (with rpmrb script)

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 5.0-alt1.dev.git20150808.1.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Thu Jan 28 2016 Mikhail Efremov <sem@altlinux.org> 5.0-alt1.dev.git20150808.1
- NMU: Use buildreq for BR.

* Wed Aug 12 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt1.dev.git20150808
- New snapshot

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 5.0-alt1.dev.git20150725
- Version 5.0-dev

* Thu Oct 16 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 4.0-alt1.dev.git20141014
- Initial build for Sisyphus

