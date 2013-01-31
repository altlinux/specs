Name: alt-domain-server 
Version: 0.2
Release: alt1

Summary: All needed for alt-domain server
License: GPL
Group: System/Configuration/Other
BuildArch: noarch
Source: %name-%version.tar
Requires: bind alterator-bind
Requires: openldap-servers krb5-kdc krb5-kadmin krb5-kinit ldap-user-tools
Requires: dhcp-server alterator-dhcp
Requires: alterator-net-domain alterator-ldap-users ldap-user-tools
Requires: samba4
Requires: alterator-kdc alterator-ldap-groups alterator-net-eth

Provides: installer-feature-setup-openldap
Obsoletes: installer-feature-setup-openldap

%description
Install this package if you need alt-domain server

%prep
%setup -q

%install
mkdir -p %buildroot/etc/
cp -a hooks %buildroot/etc/
mkdir -p %buildroot/usr/share/install2/preinstall.d
cp preinstall.d/* %buildroot/usr/share/install2/preinstall.d/

%files
/etc/hooks/hostname.d/*
/usr/share/install2/preinstall.d/*

%changelog
* Thu Jan 31 2013 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.2-alt1
- i-f-setup-openldap moved here

* Tue Aug 07 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build



