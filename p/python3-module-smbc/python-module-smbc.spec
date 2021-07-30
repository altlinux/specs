%define mname smbc

Name: python3-module-%mname
Version: 1.0.23
Release: alt3

Summary: Python interface for smbclient
Group: Development/Python3
License: GPLv2+
URL: https://pypi.python.org/pypi/pysmbc/

Source: https://pypi.python.org/packages/source/p/pysmbc//py%mname-%version.tar
Patch0: use_kerberos.patch

BuildRequires: libsmbclient-devel
BuildRequires: rpm-build-python3

%description
The smbc module provides an interface to the Samba client API.

%prep
%setup -n py%mname-%version -a0
%patch0 -p2

%build
CFLAGS=-I/usr/include/samba-4.0/ %python3_build

%install
%python3_install

%files
%python3_sitelibdir/*
%doc README.md NEWS PKG-INFO

%changelog
* Fri Jul 30 2021 Igor Chudov <nir@altlinux.org> 1.0.23-alt3
- Added support for Kerberos authentication via use_kerberos.patch

* Fri Jul 23 2021 Grigory Ustinov <grenka@altlinux.org> 1.0.23-alt2
- Drop python2 support.

* Mon Jul 05 2021 Evgeny Sinelnikov <sin@altlinux.org> 1.0.23-alt1
- updated to 1.0.23

* Thu Mar 22 2018 Aleksei Nikiforov <darktemplar@altlinux.org> 1.0.15.3-alt1.1.1
- (NMU) Rebuilt with python-3.6.4.

* Thu Mar 17 2016 Ivan Zakharyaschev <imz@altlinux.org> 1.0.15.3-alt1.1
- (NMU) rebuild with python3-3.5 & rpm-build-python3-0.1.10
  (for ABI dependence and new python3(*) reqs)

* Mon Dec 22 2014 Yuri N. Sedunov <aris@altlinux.org> 1.0.15.3-alt1
- updated to 1.0.15.3, new url
- new python3 subpackage

* Wed Apr 10 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.8-alt1
- updated to 1.0.8
- build fixed

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.6-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.6-alt1.1
- Rebuild with Python-2.7

* Tue Jan 19 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.6-alt1
- first build for Sisyphus

