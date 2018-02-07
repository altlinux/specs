%define oname terminado

%def_with python3

Name: python-module-%oname
Version: 0.5
Release: alt1.git20150717.2.1
Summary: Terminals served by tornado websockets
License: BSD
Group: Development/Python
Url: https://pypi.python.org/pypi/terminado/
Packager: Eugeny A. Rostovtsev (REAL) <real at altlinux.org>

# https://github.com/takluyver/terminado.git
Source: %name-%version.tar
BuildArch: noarch

BuildPreReq: python-devel python-module-setuptools /dev/pts
BuildPreReq: python-module-tornado_xstatic python-module-ptyprocess
BuildPreReq: python-module-xstatic-term.js
BuildPreReq: python-module-sphinx-devel
BuildRequires: python-module-nose
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-setuptools
BuildPreReq: python3-module-tornado_xstatic python3-module-ptyprocess
BuildPreReq: python3-module-xstatic-term.js
BuildRequires: python3-module-nose
%endif

%py_provides %oname
%py_requires xstatic.pkg.termjs ptyprocess tornado_xstatic

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
Group: Development/Python
Requires: %name = %EVR

%description tests
This is a Tornado websocket backend for the term.js Javascript terminal
emulator library.

This package contains tests for %oname.

%package pickles
Summary: Pickles for %oname
Group: Development/Python

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

%package -n python3-module-%oname
Summary: Terminals served by tornado websockets
Group: Development/Python3
%py3_provides %oname
%py3_requires xstatic.pkg.termjs ptyprocess tornado_xstatic

%description -n python3-module-%oname
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

%package -n python3-module-%oname-tests
Summary: Tests for %oname
Group: Development/Python3
Requires: python3-module-%oname = %EVR

%description -n python3-module-%oname-tests
This is a Tornado websocket backend for the term.js Javascript terminal
emulator library.

This package contains tests for %oname.

%prep
%setup

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

export PYTHONPATH=$PWD
%make -C doc pickle
%make -C doc html

cp -fR doc/_build/pickle %buildroot%python_sitelibdir/%oname/

%check
rm -fR build
nosetests -v
%if_with python3
pushd ../python3
rm -fR build
nosetests3 -v
popd
%endif

%files
%doc *.rst
%python_sitelibdir/*
%exclude %python_sitelibdir/*/pickle
%exclude %python_sitelibdir/*/tests

%files tests
%python_sitelibdir/*/tests

%files pickles
%python_sitelibdir/*/pickle

%files docs
%doc doc/_build/html/*

%if_with python3
%files -n python3-module-%oname
%doc *.rst
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/tests

%files -n python3-module-%oname-tests
%python3_sitelibdir/*/tests
%endif

%changelog
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

