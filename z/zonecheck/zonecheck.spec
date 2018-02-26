Summary: Perform consistency checks on DNS zones
Name: zonecheck
Version: 2.0.4
Release: alt2
License: GPL
Group: Networking/Other
URL: http://www.zonecheck.fr/
Packager: Mikhail Pokidko <pma@altlinux.org>

Source: http://www.zonecheck.fr/download/src/zonecheck-%{version}.tgz

# Automatically added by buildreq on Fri Dec 22 2006
BuildRequires: samba-common

#BuildRequires: samba-common

BuildRequires: ruby >= 1.8, libruby, samba-common, ruby-module-fileutils
#Requires: ruby >= 1.8, libruby-libs

%description
ZoneCheck is intended to help solve DNS misconfigurations or
inconsistencies that are usually revealed by an increase in
the latency of the application. The DNS is a critical resource
for every network application, so it is quite important to
ensure that a zone or domain name is correctly configured in
the DNS.

%prep
%setup -n %name

%build

%install
#makeinstall
ruby ./installer.rb common cli cgi \
	-DPREFIX="%_prefix" \
	-DETCDIR="%_sysconfdir" \
	-DLIBEXEC="%_libdir" \
	-DMANDIR="%_mandir" \
        -DETCDIST="" \
	-DCHROOT="%buildroot" \
	-DRUBY="%_bindir/ruby" \
	-DHTML_PATH="/var/www/html/%name" \
	-DLIBEXEC="%_libdir" \
	-DPROGNAME="%name"
#mkdir -p %buildroot/var/www/html/%name \
#	%buildroot/var/www/cgi-bin
#mv %buildroot%_libdir/%name/www/* %buildroot/var/www/html/%name/
#mv %buildroot%_libdir/%name/cgi-bin %buildroot/var/www/


%files
%doc BUGS ChangeLog COPYING CREDITS doc/html GPL HISTORY README TODO
%doc %_mandir/man?/*
%dir %_sysconfdir/%name/
%config %_sysconfdir/%name/rootservers
%config %_sysconfdir/%name/*.profile
%config(noreplace) %_sysconfdir/%name/zc.conf
%_bindir/*
%_libdir/%name/
#/var/www/cgi-bin
#/var/www/html/%name

%changelog
* Fri Dec 22 2006 Mikhail Pokidko <pma@altlinux.ru> 2.0.4-alt2
- Builreq changes. Web-interface disabled.

* Tue Sep 12 2006 Mikhail Pokidko <pma@altlinux.ru> 2.0.4-alt1
- Initial build.
