Name: installer-feature-weak-passwd
Version: 0.1
Release: alt1

Summary: Set more weak settings in /etc/passwdqc.conf
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
Source: %name-%version.tar

%description
Set more weak settings in /etc/passwdqc.conf

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Thu Sep 17 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first version

