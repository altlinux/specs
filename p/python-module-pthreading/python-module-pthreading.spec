%define _name pthreading
%define orig_version 0.1.3-3

Name: python-module-%_name
Version: %(echo %orig_version|tr - .)
Release: alt1

Summary: Re-implement threading.Lock, RLock and Condition with libpthread
Group: Development/Python
License: GPLv2+
Url: http://pypi.python.org/pypi/%_name

Source: http://pypi.python.org/packages/source/p/%_name/%_name-%orig_version.tar.gz
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
%setup -n %_name-%orig_version
%patch

%install
%__python setup.py install --root %buildroot --install-lib %python_sitelibdir_noarch

%check
%__python setup.py test

%files
%python_sitelibdir_noarch/pthread.py*
%python_sitelibdir_noarch/%_name.py*
%python_sitelibdir_noarch/%_name-*.egg-info

%changelog
* Thu Jun 02 2016 Yuri N. Sedunov <aris@altlinux.org> 0.1.3.3-alt1
- 0.1.3.3

* Fri Jun 06 2014 Yuri N. Sedunov <aris@altlinux.org> 0.1.3-alt1
- 0.1.3

* Wed Oct 30 2013 Yuri N. Sedunov <aris@altlinux.org> 0.1.2-alt1
- first build for Sisyphus

