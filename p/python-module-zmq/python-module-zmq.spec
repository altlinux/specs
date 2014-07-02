Name: python-module-zmq
Version: 14.3.1
Release: alt1
Summary: Software library for fast, message-based applications

Group: Development/Python
License: LGPLv3+ and ASL 2.0
Packager: Valentin Rosavitskiy <valintinr@altlinux.org>
Url: http://www.zeromq.org/bindings:python
# http://github.com/zeromq/pyzmq.git
Source: %name-%version.tar

BuildRequires: gcc4.7-c++ python-devel libzeromq-devel python-module-nose python-modules-json python-module-Cython python-module-numpy

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

%prep
%setup
cp setup.cfg.template setup.cfg
subst "s|/usr/local/lib|%_libdir|" setup.cfg
subst "s|/usr/local/include|%_includedir|" setup.cfg

%build
%python_build

%install
%python_install

%check
rm zmq/__*
PYTHONPATH=%buildroot%python_sitelibdir %__python setup.py test

%files
%doc README.md COPYING.LESSER COPYING.BSD CONTRIBUTING.md AUTHORS.md examples/
%python_sitelibdir/*.egg-info
%python_sitelibdir/zmq
%exclude %python_sitelibdir/zmq/tests
%exclude %python_sitelibdir/zmq/*/*.h

%files devel
%python_sitelibdir/zmq/*/*.h

%files tests
%python_sitelibdir/zmq/tests

%changelog
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
