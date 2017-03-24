%define pear_name Net_LDAP3

Name: pear-Net_LDAP3
Version: 1.0.5
Release: alt1

Summary: A successor of the PEAR:Net_LDAP2 module providing advanced functionality for accessing LDAP directories

License: GPL-3.0+
Group: Development/Other
URL: https://gitlab.com/roundcube/net_ldap3
Source: %name-%version.tar
BuildArch: noarch
BuildRequires: rpm-build-pear

%description
Net_LDAP3 is the successor of Net_LDAP2 which providing advanced functionality
for accessing LDAP directories

%prep
%setup

%build

%install
install -m 644 -D net_ldap3/lib/Net/LDAP3/Result.php %buildroot%pear_dir/Net/LDAP3/Result.php
install -m 644 net_ldap3/lib/Net/LDAP3.php %buildroot%pear_dir/Net/LDAP3.php

%post


%preun


%files
%pear_dir/Net/LDAP3/Result.php
%pear_dir/Net/LDAP3.php


%changelog
* Wed Mar 23 2017 Sergey Novikov <sotor@altlinux.org> 1.0.5-alt1
- initial packaging

