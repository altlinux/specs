Name: spt7-test-scripts 
Version: 1.0
Release: alt1

Summary: Test scripts for SPT7 distro
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Source: %name-%version.tar

%description
Test scripts for SPT7 distro

%prep
%setup

%install
mkdir -p %buildroot%_bindir
install -pm755 scripts/* %buildroot%_bindir/

%files
%_bindir/*

%changelog
* Tue Feb 24 2015 Anton V. Boyarshinov <boyarsh@altlinux.ru> 1.0-alt1
- first build

