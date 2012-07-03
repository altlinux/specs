Name: installer-feature-setup-openldap
Version: 0.2
Release: alt3

Summary: Tunes openldap to be ready to alterator-openldap out of the box
License: GPL
Group: System/Configuration/Other
Url: http://www.altlinux.org/Installer/beans
BuildArch: noarch
Source: %name-%version.tar

%description
Disables unnesesary example.com base and enables samba.scheme if
alterator-openldap and samba are both installed

%prep
%setup

%install
%define hookdir %_datadir/install2/preinstall.d
mkdir -p %buildroot%hookdir
install -pm755 *.sh %buildroot%hookdir/

%files
%hookdir/*

%changelog
* Mon Mar 14 2011 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt3
- add samba scheme only if availible

* Wed Oct 06 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt2
- typo fixed

* Thu Sep 30 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- kerberos schema adding
- return code if not needed fixed

* Wed Sep 29 2010 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build
