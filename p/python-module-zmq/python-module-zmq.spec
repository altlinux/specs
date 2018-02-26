Name: python-module-zmq
Version: 2.1.11
Release: alt1.1
Summary: Software library for fast, message-based applications

Group: Development/Python
License: LGPLv3+ and ASL 2.0
Url: http://www.zeromq.org/bindings:python
# http://github.com/zeromq/pyzmq.git
Source: %name-%version.tar

BuildRequires: python-devel libzeromq-devel python-module-nose python-modules-json python-module-Cython python-module-numpy

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
%doc README.rst COPYING.LESSER examples/
%python_sitelibdir/*.egg-info
%python_sitelibdir/zmq
%exclude %python_sitelibdir/zmq/tests

%files tests
%python_sitelibdir/zmq/tests

%changelog
* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 2.1.11-alt1.1
- Rebuild to remove redundant libpython2.7 dependency

* Sat Jan 21 2012 Slava Dubrovskiy <dubrsl@altlinux.org> 2.1.11-alt1
- Build for ALT
