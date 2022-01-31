%define oname pyuv

Name: python3-module-%oname
Version: 1.4.0
Release: alt3
Summary: Python interface for libuv
License: MIT
Group: Development/Python3
Url: https://pypi.python.org/pypi/pyuv/

# https://github.com/saghul/pyuv.git
# branch: v1.x
Source: %name-%version.tar

Patch: pyuv-python3.10.patch

BuildRequires(pre): /dev/pts /proc
BuildRequires(pre): rpm-build-python3
BuildRequires(pre): rpm-macros-sphinx3
BuildRequires: python3-module-sphinx

%py3_provides %oname

%description
pyuv is a Python module which provides an interface to libuv. libuv is a
high performance asynchronous networking and platform abstraction
library.

%package pickles
Summary: Pickles for %oname
Group: Development/Python3

%description pickles
pyuv is a Python module which provides an interface to libuv. libuv is a
high performance asynchronous networking and platform abstraction
library.

This package contains pickles for %oname.

%package docs
Summary: Documentation for %oname
Group: Development/Documentation
BuildArch: noarch

%description docs
pyuv is a Python module which provides an interface to libuv. libuv is a
high performance asynchronous networking and platform abstraction
library.

This package contains documentation for %oname.

%prep
%setup
%patch -p1

%prepare_sphinx3 .
ln -s ../objects.inv docs/

%build
%add_optflags -fno-strict-aliasing
%python3_build_debug

%install
%python3_install

%make SPHINXBUILD="sphinx-build-3" -C docs pickle
%make SPHINXBUILD="sphinx-build-3" -C docs html

cp -fR docs/_build/pickle %buildroot%python3_sitelibdir/%oname/

%check
python3 setup.py test

%files
%doc AUTHORS ChangeLog *.rst TODO examples
%python3_sitelibdir/*
%exclude %python3_sitelibdir/*/pickle

%files pickles
%python3_sitelibdir/*/pickle

%files docs
%doc docs/_build/html/*

%changelog
* Thu Jan 13 2022 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt3
- Fixed build with python3.10.

* Mon May 24 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt2
- Drop python2 support.

* Tue Feb 16 2021 Grigory Ustinov <grenka@altlinux.org> 1.4.0-alt1
- Build new version for python3.9.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.1.0-alt1.git20150619.1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Fri Feb 02 2018 Stanislav Levin <slev@altlinux.org> 1.1.0-alt1.git20150619.1.1
- (NMU) Fix Requires and BuildRequires to python-setuptools

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.1.0-alt1.git20150619.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Thu Jul 30 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.1.0-alt1.git20150619
- Version 1.1.0

* Tue Feb 17 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20150116
- New snapshot

* Thu Jan 15 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 1.0.2-alt1.git20150115
- Initial build for Sisyphus

