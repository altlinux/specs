Name: apache2-mod_geoip2
Version: 1.2.7
Release: alt1

Summary: Apache2 module for finding the country and city that a web request originated from
License: Apache Software License v1.1
Group: System/Servers

# NB: do not put trailing slash in URL or you will end up at maxmind homepage! :)
Url: http://www.maxmind.com/app/mod_geoip
Source0: http://www.maxmind.com/download/geoip/api/mod_geoip2/mod_geoip2_%version.tar.gz
Source1: apache2-mod_geoip2-load.conf
Source2: apache2-mod_geoip2.conf

PreReq: apache2 >= %apache2_version

# Automatically added by buildreq on Mon Aug 11 2008
BuildRequires: apache2-devel libGeoIP-devel

%description
mod_geoip is an Apache module for finding the country that a web request
originated from. It uses the GeoIP library and database to perform the lookup.

%prep
%setup -n mod_geoip2_%version

%build
%apache2_apxs -lGeoIP -c mod_geoip.c

%install
install -pD -m 0644 %SOURCE1 %buildroot%apache2_confdir/modules.d/A.500_geoip2.conf
install -pD -m 0644 %SOURCE2 %buildroot%apache2_addonconfdir/A.mod_geoip2.conf
install -pD -m 0755 .libs/mod_geoip.so %buildroot%apache2_moduledir/mod_geoip.so

%files
%config(noreplace) %apache2_confdir/modules.d/A.500_geoip2.conf
%config(noreplace) %apache2_addonconfdir/A.mod_geoip2.conf
%apache2_moduledir/mod_geoip.so
%doc Changes INSTALL README README.php

%changelog
* Sat Nov 26 2011 Victor Forsiuk <force@altlinux.org> 1.2.7-alt1
- 1.2.7

* Tue Aug 26 2008 Victor Forsyuk <force@altlinux.org> 1.2.5-alt1
- 1.2.5

* Mon Aug 11 2008 Victor Forsyuk <force@altlinux.org> 1.2.4-alt1
- 1.2.4

* Thu May 15 2008 Victor Forsyuk <force@altlinux.org> 1.2.3-alt1
- 1.2.3

* Tue Apr 08 2008 Victor Forsyuk <force@altlinux.org> 1.2.2-alt1
- 1.2.2
- License is in fact Apache, not GPL.

* Sun Mar 04 2007 Ivan Fedorov <ns@altlinux.ru> 1.1.8-alt2
- Rebuild for apache 2.2 compatibility
- Rewrite configuration
- Fix URL

* Sat Feb 17 2007 Ivan Fedorov <ns@altlinux.ru> 1.1.8-alt1
- Initial build for ALT Linux.
