Name: installer-feature-rm-slideshow
Version: 0.1
Release: alt1

Summary: turn off slideshow in small memory conditions 
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Packager: Anton V. Boyarshinov <boyarsh@altlinux.org>
Source: %name-%version.tar

%description
turn off slideshow in small memory conditions

%prep
%setup

%install
%define hookdir %_datadir/install2/initinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Thu Jul 30 2009 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build

