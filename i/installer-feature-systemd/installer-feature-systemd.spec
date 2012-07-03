Name: installer-feature-systemd
Version: 0.3
Release: alt3

Summary: Set up systemd support
License: GPL
Group: System/Configuration/Other

Url: http://www.altlinux.org/Installer/beans
Source: %name-%version.tar
BuildArch: noarch
Requires: installer-stage2

%description
%summary

%prep
%setup -q

%install
%define hookdir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed May 30 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt3
- really fix chkconfig deceiveing (mount --bind isn't recursive)

* Tue May 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt2
- chkconfig deceiveing fixed

* Tue May 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.3-alt1
- deceive chkconfig about running systemd

* Tue May 29 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- removed not needed now 90-systemd.sh

* Fri Nov 11 2011 Alexey Shabalin <shaba@altlinux.ru> 0.1-alt1
- init with installer-sdk

