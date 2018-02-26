Name: installer-feature-tune-logindefs
Version: 0.2
Release: alt1

Summary: Set UID_MIN and GID_MIN to 10000
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
Source: %name-%version.tar

%description
LDAP users should not cross with local users. This install-time package
tunes /etc/login.defs to aviod this crossing.

%prep
%setup

%install
%define hookdir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Apr 20 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- GID_MIN downgraded to 5000 to avoid conflict with Samba mappings 

* Fri Apr 17 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build 

