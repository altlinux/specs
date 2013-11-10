%define modulename python-libevent

Name: python-module-libevent
Version: 0.9.2
Release: alt2

Summary: Python bindings for libevent

Group: Development/Python
License: LGPLv2+
Url: http://pypi.python.org/pypi/%modulename/

Packager: Denis Baranov <baraka@altlinux.ru>

Source: http://pypi.python.org/packages/source/p/%modulename/%modulename-%version.tar

%setup_python_module %modulename

BuildRequires: python-devel libevent-devel python-module-setuptools


%description
python-libevent is a CPython extension module that wraps the lightweight C
library 'libevent', available at http://www.monkey.org/~provos/libevent/.

libevent provides a unified interface to a variety of IO multiplexing
mechanisms (select, poll, kqueue, epoll) and an event loop that supports
timed events and signal handlers.

%prep
%setup -n %modulename-%version

%build
%python_build

%install
%python_install

%files
#%python_sitelibdir/%modulename/
#%python_sitelibdir/%modulename-%version-*.egg-info
%python_sitelibdir/_libevent.so
%python_sitelibdir/libevent.py
%python_sitelibdir/libevent.pyc
%python_sitelibdir/libevent.pyo
%python_sitelibdir/python_libevent-%version-*.egg-info/*

%changelog
* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 0.9.2-alt2
- Fix requires

* Sun Nov 10 2013 Denis Baranov <baraka@altlinux.ru> 0.9.2-alt1
- Initial build for ALTLinux

