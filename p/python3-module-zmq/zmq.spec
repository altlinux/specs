%define oname zmq

%def_with bootstrap
# included patch totally destroys tests=(
%def_with check

Name: python3-module-%oname
Version: 24.0.1
Release: alt1

Summary: Software library for fast, message-based applications

Group: Development/Python3
License: LGPLv3+ and BSD-3-Clause
Url: http://www.zeromq.org/bindings:python
# http://github.com/zeromq/pyzmq.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libzeromq-devel
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel
BuildRequires: python3-module-Cython
%if_without bootstrap
BuildRequires: python3-module-cffi
BuildRequires: python3-module-numpy
%endif
%if_with check
BuildRequires: python3-module-pytest
%endif

%description
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the python bindings.

%package tests
Summary: Software library for fast, message-based applications
Group: Development/Python3
License: LGPLv3+

%description tests
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the testsuite for the python bindings.

%package devel
Summary: Software library for fast, message-based applications
Group: Development/Python3
Requires: %name = %version-%release

%description devel
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the headers for the python bindings.

%prep
%setup
cp setup.cfg.template setup.cfg
subst "s|/usr/local/lib|%_libdir|" setup.cfg
subst "s|/usr/local/include|%_includedir|" setup.cfg

%build
%add_optflags -fno-strict-aliasing
%pyproject_build

%install
%pyproject_install

%check
# This test wants to build a custom cython extension, but does
# not have the source files installed into the buildroot
# That's why test_cython disabled, according to opensuse
# Note also that it should be build with build_ext --inplace
# to pass the tests, according to setup.py
# Tests are not passing in %%buildroot%%python3_sitelibdir
# because zmq's asyncio conflicts with python3-base's asyncio
# Maybe it somehow tied with paths
export PYTHONPATH=%buildroot%python3_sitelibdir
cd ..
py.test3 --pyargs zmq -v -k "not test_cython"

%files
%doc README.md COPYING.LESSER COPYING.BSD CONTRIBUTING.md AUTHORS.md examples/
%python3_sitelibdir/*.dist-info
%python3_sitelibdir/%oname
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/*.h

%files devel
%python3_sitelibdir/%oname/*/*.h

%files tests
%python3_sitelibdir/%oname/tests

%changelog
* Thu Nov 24 2022 Grigory Ustinov <grenka@altlinux.org> 24.0.1-alt1
- Automatically updated to 24.0.1.
- Bootstrap for python3.11.

* Thu Mar 24 2022 Grigory Ustinov <grenka@altlinux.org> 22.3.0-alt4
- Force use cffi backend (Closes: #42033).
- Build without check.

* Mon Feb 14 2022 Grigory Ustinov <grenka@altlinux.org> 22.3.0-alt3
- Build without bootstrap.
- Build with cffi.
- Enabled check.

* Sun Dec 05 2021 Grigory Ustinov <grenka@altlinux.org> 22.3.0-alt2
- Bootstrap for python3.10.

* Wed Oct 06 2021 Grigory Ustinov <grenka@altlinux.org> 22.3.0-alt1
- Automatically updated to 22.3.0.

* Mon May 31 2021 Grigory Ustinov <grenka@altlinux.org> 22.1.0-alt1
- Automatically updated to 22.1.0.
- Build without bootstrap.
- Fix license.

* Thu Dec 03 2020 Grigory Ustinov <grenka@altlinux.org> 20.0.0-alt1
- Automatically updated to 20.0.0.
- Transfer to python3.
- Add bootstrap knob.

* Thu Jun 07 2018 Grigory Ustinov <grenka@altlinux.org> 17.0.0-alt1
- Build new version.

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 16.0.2-alt2.1
- (NMU) Rebuilt with python-3.6.4.

* Mon Jan 30 2017 Valentin Rosavitskiy <valintinr@altlinux.org> 16.0.2-alt2
- Rebuild with new zeromq library

* Wed Nov 30 2016 Valentin Rosavitskiy <valintinr@altlinux.org> 16.0.2-alt1
- New version

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 14.7.0-alt2.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Fri Oct 02 2015 Gleb F-Malinovskiy <glebfm@altlinux.org> 14.7.0-alt2
- Switched to build with default g++.

* Mon Aug 31 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 14.7.0-alt1
- New version

* Tue Apr 28 2015 Valentin Rosavitskiy <valintinr@altlinux.org> 14.6.0-alt1
- New version

* Mon Jan 05 2015 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.4.1-alt3.1
- Rebuilt with new zeromq

* Tue Dec 30 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 14.4.1-alt3
- Another try to fix repocop fail buildroot (__pycache__)

* Tue Dec 09 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 14.4.1-alt2
- Fixed repocop fail buildroot (__pycache__)

* Fri Nov 21 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 14.4.1-alt1
- New version

* Wed Sep 03 2014 Eugeny A. Rostovtsev (REAL) <real at altlinux.org> 14.3.1-alt1.1
- Added module for Python 3

* Tue Jul 01 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 14.3.1-alt1
- New version

* Tue Jun 10 2014 Valentin Rosavitskiy <valintinr@altlinux.org> 14.3.0-alt1
- New version

* Fri Dec 07 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.0.1-alt2
- Add subpackage devel

* Thu Dec 06 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.2.0.1-alt1
- New version

* Sat Jan 21 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1.11-alt1
- Build for ALT
