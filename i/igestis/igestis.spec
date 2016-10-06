Name: 	  igestis
Version:  3.1.0
Release:  alt1

Summary:  Web administration for LDAP users and groups
License:  GPL3
Group:    System/Configuration/Networking
Url: 	  http://open.iabsis.com/subversion/igestis

Packager: Denis Medvedev <nbr@altlinux.org>

Source:   %name-%version.tar

BuildPreReq: rpm-build-php-version rpm-build-php5 rpm-build-apache2

BuildArch: noarch
Requires: apache2-mod_php5
Requires: php5-mysql

%description
Web administration tool for managing  users and groups, stored in LDAP.
Taken from igestis ERP.

%prep
%setup

%install
mkdir -p  %buildroot/%webserver_webappsdir/igestis/
mkdir -p  %buildroot/%_docdir/igestis/debian_packing
cp README.md %buildroot/%_docdir/igestis/
rm igestis.spec
cp -ar  ./debian/* %buildroot/%_docdir/igestis/debian_packing/
rm -rf ./debian
cp -ar ./* %buildroot/%webserver_webappsdir/igestis/

%files
%webserver_webappsdir/igestis/*
%_docdir/igestis/*

%changelog
* Thu Oct 06 2016 Denis Medvedev <nbr@altlinux.org> 3.1.0-alt1
- new version

* Thu Oct 06 2016 Denis Medvedev <nbr@altlinux.org> 2.3.18-alt4
- Moved app to webappsdir

* Thu Jun 09 2016 Denis Medvedev <nbr@altlinux.org> 2.3.18-alt3
- moved debian packaging instructions to doc

* Thu Jun 09 2016 Denis Medvedev <nbr@altlinux.org> 2.3.18-alt2
- fix packaging

* Fri Jun 03 2016 Denis Medvedev <nbr@altlinux.org> 2.3.18-alt1
Initial release
