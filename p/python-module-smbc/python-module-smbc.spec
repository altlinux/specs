%define mname smbc

Name: python-module-%mname
Version: 1.0.15.3
Release: alt1.1.1

Summary: Python interface for smbclient
Group: Development/Python
License: GPLv2+
URL: https://pypi.python.org/pypi/pysmbc/

%setup_python_module %mname

Source: https://pypi.python.org/packages/source/p/pysmbc//py%mname-%version.tar

BuildRequires: libsmbclient-devel
BuildRequires: rpm-build-python3 python3-devel

%description
The smbc module provides an interface to the Samba client API.

%package -n python3-module-%mname
Summary: Python3 interface for smbclient
Group: Development/Python3

%description -n python3-module-%mname
The smbc module provides an interface to the Samba client API.

%prep
%setup -n py%mname-%version -a0
mv py%mname-%version py3build

%build
CFLAGS=-I/usr/include/samba-4.0/ %python_build
pushd py3build
CFLAGS=-I/usr/include/samba-4.0/ %python3_build
popd

%install
%python_install
pushd py3build
%python3_install
popd

%files
%python_sitelibdir/*
%doc README NEWS PKG-INFO

%files -n python3-module-%mname
%python3_sitelibdir/*
%doc README NEWS PKG-INFO

%changelog
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

