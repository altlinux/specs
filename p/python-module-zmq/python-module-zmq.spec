%define oname zmq

%def_with python3

Name: python-module-%oname
Version: 16.0.2
Release: alt1
Summary: Software library for fast, message-based applications

Group: Development/Python
License: LGPLv3+ and ASL 2.0
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
Url: http://www.zeromq.org/bindings:python
# http://github.com/zeromq/pyzmq.git
Source: %name-%version.tar

BuildRequires: gcc-c++ python-devel libzeromq-devel python-module-nose python-modules-json python-module-Cython python-module-numpy
%if_with python3
BuildRequires(pre): rpm-build-python3
BuildPreReq: python3-devel python3-module-nose python3-module-Cython
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
Group: Development/Python
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
Group: Development/Python
Requires: %name = %version-%release

%description devel
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the headers for the python bindings.

%package -n python3-module-%oname
Summary: Software library for fast, message-based applications
Group: Development/Python3

%description -n python3-module-%oname
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the python bindings.

%package -n python3-module-%oname-tests
Summary: Software library for fast, message-based applications
Group: Development/Python3
License: LGPLv3+

%description -n python3-module-%oname-tests
The 0MQ lightweight messaging kernel is a library which extends the
standard socket interfaces with features traditionally provided by
specialized messaging middle-ware products. 0MQ sockets provide an
abstraction of asynchronous message queues, multiple messaging
patterns, message filtering (subscriptions), seamless access to
multiple transport protocols and more.

This package contains the testsuite for the python bindings.

%package -n python3-module-%oname-devel
Summary: Software library for fast, message-based applications
Group: Development/Python3
Requires: python3-module-%oname = %version-%release

%description -n python3-module-%oname-devel
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

%if_with python3
cp -fR . ../python3
%endif

%build
%add_optflags -fno-strict-aliasing
%python_build

%if_with python3
pushd ../python3
%python3_build
popd
%endif

%install
%python_install

%if_with python3
pushd ../python3
%python3_install
popd
%endif

#check
#rm %oname/__*
#PYTHONPATH=%buildroot%python_sitelibdir python setup.py test
#rm -rf %python_sitelibdir/%oname/backend/cffi/__*
#rm -rf %buildroot%python_sitelibdir/%oname/backend/cffi/__*
#
#if_with python3
#pushd ../python3
#rm %oname/__*
#PYTHONPATH=%buildroot%python3_sitelibdir python3 setup.py test
#rm -rf %python3_sitelibdir/%oname/backend/cffi/__*
#rm -rf %buildroot%python3_sitelibdir/%oname/backend/cffi/__*
#popd
#endif

%files
%doc README.md COPYING.LESSER COPYING.BSD CONTRIBUTING.md AUTHORS.md examples/
%python_sitelibdir/*.egg-info
%python_sitelibdir/%oname
%exclude %python_sitelibdir/%oname/tests
%exclude %python_sitelibdir/%oname/*/*.h

%files devel
%python_sitelibdir/%oname/*/*.h

%files tests
%python_sitelibdir/%oname/tests

%if_with python3
%files -n python3-module-%oname
%doc README.md COPYING.LESSER COPYING.BSD CONTRIBUTING.md AUTHORS.md examples/
%python3_sitelibdir/*.egg-info
%python3_sitelibdir/%oname
%exclude %python3_sitelibdir/%oname/tests
%exclude %python3_sitelibdir/%oname/*/*.h

%files -n python3-module-%oname-devel
%python3_sitelibdir/%oname/*/*.h

%files -n python3-module-%oname-tests
%python3_sitelibdir/%oname/tests
%endif

%changelog
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
