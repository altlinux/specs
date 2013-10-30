%define _name pthreading

Name: python-module-%_name
Version: 0.1.2
Release: alt1

Summary: Re-implement threading.Lock, RLock and Condition with libpthread
Group: Development/Python
License: GPLv2+
Url: http://pypi.python.org/pypi/%_name

Source: http://pypi.python.org/packages/source/p/%_name/%_name-%version.tar.gz
# fc
Patch: python-pthreading-01-COPYING-and-tests.patch

BuildArch: noarch

BuildRequires: python-devel python-modules-unittest

%description
The pthreading module provides Lock and Condition synchronization
objects compatible with Python native threading module.
The implementation, however, is based on POSIX thread library as delivered
by the libpthread and has considerable performance benefits over Python 2.x's
implementation.

%prep
%setup -n %_name-%version
%patch

%install
%__python setup.py install --root %buildroot --install-lib %python_sitelibdir_noarch

%check
%__python setup.py test

%files
%python_sitelibdir_noarch/pthread.py*
%python_sitelibdir_noarch/%_name.py*
%python_sitelibdir_noarch/%_name-%version-py*.egg-info

%changelog
* Wed Oct 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- first build for Sisyphus

