%define oname zmq

%def_with bootstrap

Name: python3-module-%oname
Version: 22.3.0
Release: alt2
Summary: Software library for fast, message-based applications

Group: Development/Python3
License: LGPLv3+ and BSD-3-Clause
Url: http://www.zeromq.org/bindings:python
# http://github.com/zeromq/pyzmq.git
Source: %name-%version.tar

BuildRequires(pre): rpm-build-python3
BuildRequires: libzeromq-devel
BuildRequires: python3-module-Cython
%if_without bootstrap
BuildPreReq: python3-module-numpy
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
%python3_build

%install
%python3_install

#check
#rm %oname/__*
#PYTHONPATH=%buildroot%python3_sitelibdir python3 setup.py test
#rm -rf %python3_sitelibdir/%oname/backend/cffi/__*
#rm -rf %buildroot%python3_sitelibdir/%oname/backend/cffi/__*

%files
%doc README.md COPYING.LESSER COPYING.BSD CONTRIBUTING.md AUTHORS.md examples/
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/%oname
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/*.h

%files devel
%python3_sitelibdir/%oname/*/*.h

%files tests
%python3_sitelibdir/%oname/tests

%changelog
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
