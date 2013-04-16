Name: installer-feature-autofs-wait
Version: 0.1
Release: alt1

Summary: Setups MOUNT_WAIT paramater for autofs
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Setups MOUNT_WAIT paramater for autofs (see #28356)

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Tue Apr 16 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build


