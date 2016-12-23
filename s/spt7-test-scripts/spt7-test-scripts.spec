Name: spt7-test-scripts 
Version: 1.4
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
make -C src test_clearmem

%install
mkdir -p %buildroot%_bindir
mkdir -p %buildroot%_libexecdir/%name/
install -pm755 scripts/* %buildroot%_bindir/
install -pm755 src/test_access %buildroot%_bindir/
install -pm755 src/test_clearmem %buildroot%_bindir/
cp -a setup-tests/ %buildroot%_libexecdir/%name/
cp -a tests/ %buildroot%_libexecdir/%name/

%files
%_bindir/*
%_libexecdir/%name/

%changelog
* Fri Dec 23 2016 Anton V. Boyarshinov <boyarsh@altlinux.org> 1.4-alt1
- test_clearmem programm added

* Thu Apr 02 2015 Mikhail Efremov <sem@altlinux.org> 1.3-alt1
- Fix p4_6_2_3 test (by azol@).

* Fri Mar 20 2015 Mikhail Efremov <sem@altlinux.org> 1.2-alt1
- Add tests.

* Fri Feb 27 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.1-alt1
- test_access programm added

* Tue Feb 24 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt1
- first build

