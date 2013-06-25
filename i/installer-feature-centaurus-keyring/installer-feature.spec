Name: installer-feature-centaurus-keyring
Version: 0.1
Release: alt2

Summary: disable redundant ssh keyrings
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
The only one ssh keyring should run. Gnome and Mate keyrings
doesn't support ecdsa keys, so it should be ssh-agent

%prep
%setup

%install
%define hookdir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Tue Jun 25 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt2
- typo fixed

* Tue Jun 25 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build


