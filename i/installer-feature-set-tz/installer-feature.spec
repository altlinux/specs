Name: installer-feature-set-tz
Version: 0.2
Release: alt1

Summary: Set TZ in stage2 from kernel command line
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
Source: %name-%version.tar

%description
This package sets TZ from kernel command line

%prep
%setup

%install
%define hookdir %_datadir/install2/initinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Fri May 22 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- fixed work when no tz specified in /proc/cmdline 

* Wed Apr 29 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial version 

