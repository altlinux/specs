Name: installer-feature-local-clock
Version: 0.1
Release: alt1

Summary: Sets UTC=false in sysconfig/clock
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Sets UTC=false in sysconfig/clock for desktop distributions

%prep
%setup

%install
%define hookdir %_datadir/install2/initinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Sat Oct 23 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initital build


