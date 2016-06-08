Name: 	  igestis
Version:  2.3.18
Release:  alt1

Summary:  Web administration for LDAP users and groups
License:  GPL3
Group:    System/Configuration/Networking
Url: 	  http://open.iabsis.com/subversion/igestis

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildPreReq: rpm-build-php-version rpm-build-php5 rpm-build-apache2

BuildArch: noarch

%description
Web administration tool for managing  users and groups, stored in LDAP.
Taken from igestis ERP.

%prep
%setup

%install
install  -dm 0644 . %buildroot/%_datadir/igestis

%files
%_datadir/igestis

%changelog
* Fri Jun 03 2016 Denis Medvedev <nbr@altlinux.org> 2.3.18-alt1
Initial release
