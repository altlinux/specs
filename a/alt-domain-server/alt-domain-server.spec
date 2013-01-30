Name: alt-domain-server 
Version: 0.1
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

%description
Install this package if you need alt-domain server

%prep
%setup -q

%install
mkdir -p %buildroot/etc/
cp -a hooks %buildroot/etc/

%files
/etc/hooks/hostname.d/*

%changelog
* Tue Aug 07 2012 Anton V. Boyarshinov <boyarsh@altlinux.ru> 0.1-alt1
- first build



