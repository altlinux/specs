Name: python-module-smbc
Version: 1.0.8
Release: alt1

Summary: Python interface for smbclient
Group: Development/Python
License: GPLv2+
URL: http://cyberelk.net/tim/data/pysmbc/

%define mname smbc

%setup_python_module %mname

Source: py%mname-%version.tar

BuildRequires: libsmbclient-devel

%description
The smbc module provides an interface to the Samba client API.

%prep
%setup -n py%mname-%version

%build
CFLAGS=-I/usr/include/samba-4.0/ %python_build

%install
%python_install

%files
%python_sitelibdir/*
%doc README

%changelog
* Wed Apr 10 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.8-alt1
- updated to 1.0.8
- build fixed

* Thu Apr 12 2012 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.6-alt1.1.1
- Rebuild to remove redundant libpython2.7 dependency

* Thu Oct 20 2011 Vitaly Kuznetsov <vitty@altlinux.ru> 1.0.6-alt1.1
- Rebuild with Python-2.7

* Tue Jan 19 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0.6-alt1
- first build for Sisyphus

