%define module Geo-IP

Name: perl-%module
Version: 1.40
Release: alt1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Look up country by IP Address 
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Geo/%module-%version.tar.gz

# from Fedora
Patch: Geo-IP-1.28-yahoo-namelookuptest.diff

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libGeoIP-devel perl-devel

%description
This module uses a file-based database. This database simply contains IP blocks
as keys, and countries as values. This database should be more complete and
accurate than reverse DNS lookups.

%prep
%setup -n %module-%version
%patch

find lib/ example/ -type f -print0 | xargs -r0 %__subst -p 's./usr/local/share/GeoIP./usr/share/GeoIP.'

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes example
%perl_vendor_archlib/Geo
%perl_vendor_autolib/Geo

%changelog
* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.40-alt1
- 1.38 -> 1.40
- built for perl-5.14
- disabled online test (patch from Fedora)

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 1.38-alt1.1
- rebuilt with perl 5.12

* Wed Oct 07 2009 Victor Forsyuk <force@altlinux.org> 1.38-alt1
- 1.38
- Fix default path to GeoIP database.

* Mon Apr 11 2005 LAKostis <lakostis at altlinux.ru> 1.25-alt1.1
- spec cleanup.

* Sat Apr 09 2005 LAKostis <lakostis at altlinux.ru> 1.25-alt1
- first build for Sisyphus.
