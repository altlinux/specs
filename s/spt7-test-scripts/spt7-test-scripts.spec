Name: spt7-test-scripts 
Version: 1.2
Release: alt1

Summary: Test scripts for SPT7 distro
License: GPL
Group: System/Configuration/Other
Source: %name-%version.tar

%description
Test scripts for SPT7 distro

%prep
%setup

%build
make -C src test_access

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libexecdir/%name/
install -pm755 scripts/* %buildroot%_bindir/
install -pm755 src/test_access %buildroot%_bindir/
cp -a setup-tests/ %buildroot%_libexecdir/%name/
cp -a tests/ %buildroot%_libexecdir/%name/

%files
%_bindir/*
%_libexecdir/%name/

%changelog
* Fri Mar 20 2015 Mikhail Efremov <sem@altlinux.org> 1.2-alt1
- Add tests.

* Fri Feb 27 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1-alt1
- test_access programm added

* Tue Feb 24 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt1
- first build

