Name: mod_geoip
Version: 1.3.5
Release: alt1

Summary: GeoIP database access module for Apache
License: Apache Software License v1.1
Group: System/Servers

URL: http://www.maxmind.com/app/mod_geoip
Source: http://www.maxmind.com/download/geoip/api/mod_geoip/mod_geoip_%version.tar.gz
Source2: mod_geoip.conf

# Automatically added by buildreq on Fri Sep 19 2008
BuildRequires: apache-devel apache-suexec libGeoIP-devel

%description
mod_geoip is an Apache module for finding the country that a web request
originated from. It uses the GeoIP library and database to perform the
lookup.

%prep
%setup -n mod_geoip_%version

%build
%apache_apxs -c -I/usr/include/GeoIP -lGeoIP mod_geoip.c

%install
install -pD -m755 mod_geoip.so %buildroot%apache_moduledir/mod_geoip.so
install -pD -m644 %_sourcedir/mod_geoip.conf %buildroot%apache_modconfdir/mod_geoip.conf

%post
%post_apacheconf

%postun
%postun_apacheconf

%files
%doc README README.php
%apache_moduledir/*
%config(noreplace) %apache_modconfdir/*

%changelog
* Sat Nov 26 2011 Victor Forsiuk <force@altlinux.org> 1.3.5-alt1
- 1.3.5

* Fri Sep 19 2008 Victor Forsyuk <force@altlinux.org> 1.3.4-alt1
- 1.3.4

* Tue Aug 26 2008 Victor Forsyuk <force@altlinux.org> 1.3.3-alt1
- 1.3.3

* Tue May 27 2008 Victor Forsyuk <force@altlinux.org> 1.3.2-alt1
- 1.3.2

* Thu Mar 27 2008 Victor Forsyuk <force@altlinux.org> 1.3.1-alt1
- 1.3.1

* Mon Apr 16 2007 ALT QA Team Robot <qa-robot@altlinux.org> 1.2.9-alt1.0
- Automated rebuild.

* Tue May 23 2006 Victor Forsyuk <force@altlinux.ru> 1.2.9-alt1
- 1.2.9

* Tue Sep 27 2005 Victor Forsyuk <force@altlinux.ru> 1.2.8-alt1
- Initial build.
