Name: installer-feature-auto-domain
Version: 0.2
Release: alt1

Summary: Sets auth to krb5 if 'krb5' kernel option specified
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Sets auth to krb5 if 'krb5' kernel option specified

%prep
%setup

%install
%define hookdir %_datadir/install2/postinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Wed Sep 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- use install2 resolver
- move to postinstall

* Wed Sep 28 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- initial build



