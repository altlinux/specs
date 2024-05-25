%define mname smbc

Name: python3-module-%mname
Version: 1.0.25.1
Release: alt1

Summary: Python interface for smbclient

Group: Development/Python3
License: GPLv2+
URL: https://pypi.org/project/pysmbc
VCS: https://github.com/hamano/pysmbc

Source: %name-%version.tar

BuildRequires: libsmbclient-devel
BuildRequires: rpm-build-python3
BuildRequires: python3-module-setuptools
BuildRequires: python3-module-wheel

%description
The smbc module provides an interface to the Samba client API.

%prep
%setup

%build
CFLAGS=-I/usr/include/samba-4.0/ %pyproject_build

%install
%pyproject_install

%files
%doc README.md NEWS
%python3_sitelibdir/_smbc.cpython*.so
%python3_sitelibdir/%mname
%python3_sitelibdir/pysmbc-%version.dist-info

%changelog
* Sat May 25 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.25.1-alt1
- Build new version.

* Tue Jan 09 2024 Grigory Ustinov <grenka@altlinux.org> 1.0.23-alt4
- Fixed build with python3.12.

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

