%define oname terminado

%def_without check

Name: python3-module-%oname
Version: 0.9.5
Release: alt1

Summary: Terminals served by tornado websockets

License: BSD
Group: Development/Python3
Url: https://pypi.python.org/pypi/terminado/

Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# Source-url: %__pypi_url %oname
Source: %name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-intro
BuildRequires(pre): rpm-build-python3

BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx-sphinx-build-symlink

%if_with check
BuildRequires: /dev/pts
BuildRequires: python3-module-nose
BuildRequires: python3-module-ptyprocess
BuildRequires: python3-module-tornado_xstatic
%endif

%py3_requires xstatic.pkg.termjs ptyprocess tornado_xstatic

%description
This is a Tornado websocket backend for the term.js Javascript terminal
emulator library.

Modules:

* terminado.management: controls launching virtual terminals, connecting
  them to Tornado's event loop, and closing them down.
* terminado.websocket: Provides a websocket handler for communicating
  with a terminal.
* terminado.uimodule: Provides a Terminal Tornado UI Module.

JS:

* terminado/_static/terminado.js: A lightweight wrapper to set up a
  term.js terminal with a websocket.

%package tests
Summary: Tests for %oname
Group: Development/Python3
Requires: %name = %EVR

%description tests
This is a Tornado websocket backend for the term.js Javascript terminal
emulator library.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
This is a Tornado websocket backend for the term.js Javascript terminal
emulator library.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
This is a Tornado websocket backend for the term.js Javascript terminal
emulator library.

This package contains documentation for %oname.

%prep
%setup

%prepare_sphinx3 .
#ln -s ../objects.inv doc/

%build
%python3_build_debug

%install
%python3_install

#export PYTHONPATH=$PWD
#make -C doc pickle
#make -C doc html

#cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
rm -fR build
nosetests3 -v

%files
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files tests
%python3_sitelibdir/*/tests

#%files docs
#%doc doc/_build/html/*

%changelog
* Sun Aug 15 2021 Vitaly Lipatov <lav@altlinux.ru> 0.9.5-alt1
- new version 0.9.5 (with rpmrb script)

* Thu Aug 05 2021 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt2
- use python3-module-sphinx

* Wed Oct 21 2020 Vitaly Lipatov <lav@altlinux.ru> 0.9.1-alt1
- separated build python3 module, cleanup spec
- new version 0.9.1 (with rpmrb script)
- temp. disable check due its network nature
- switch to build from tarball

* Mon Jan 28 2019 Stanislav Levin <slev@altlinux.org> 0.5-alt2.git20150717
- Fixed build (closes: #35984).

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 0.5-alt1.git20150717.2.1
- (NMU) Fix Requires and BuildRequires to python-setuptools
- Fix tests

* Thu Jul 13 2017 Aleksei Nikiforov <darktemplar@altlinux.org> 0.5-alt1.git20150717.2
- Fixed build spec with py.test3

* Sun Mar 13 2016 Ivan Zakharyaschev <imz@altlinux.org> 0.5-alt1.git20150717.1
- (NMU) rebuild with rpm-build-python3-0.1.9
  (for common python3/site-packages/ and auto python3.3-ABI dep when needed)

* Sat Aug 22 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.5-alt1.git20150717
- Version 0.5

* Wed Feb 04 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.4-alt1.git20150203
- Version 0.4

* Tue Nov 18 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 0.3.1-alt1.git20141117
- Initial build for Sisyphus

