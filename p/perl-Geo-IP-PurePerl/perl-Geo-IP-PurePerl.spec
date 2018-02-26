# no network :(
%def_disable test
%define module Geo-IP-PurePerl

Name: perl-%module
Version: 1.25
Release: alt2

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Geo::IP::PurePerl - Look up country by IP Address
License: GPLv2+
Group: Development/Perl

BuildArch: noarch

Url: %CPAN %module
Source: http://search.cpan.org/CPAN/authors/id/B/BO/BORISZ/%module-%version.tar.gz

# Automatically added by buildreq on Fri Jun 25 2010 (-bi)
BuildRequires: GeoIP-Lite-Country perl-Encode perl-Locale-Codes perl-devel

# automatically added during perl 5.8 -> 5.12 upgrade.
# perl-podlators is required for pod2man conversion.
BuildRequires: perl-podlators

%description
This module uses a file based database. This database simply contains IP blocks
as keys, and countries as values. This database should be more complete and
accurate than reverse DNS lookups.

%prep
%setup -n %module-%version

%build
find . -type f -print0 | xargs -r0 subst 's./usr/local/share/GeoIP./usr/share/GeoIP.'
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
%doc README Changes geoip-lookup-*
%_bindir/geoip-lookup
%_man1dir/*
%perl_vendor_privlib/Geo

%changelog
* Sun Oct 23 2011 Igor Vlasenko <viy@altlinux.ru> 1.25-alt2
- fixed build (disabled tests because network is disabled)

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Fri Jun 25 2010 Victor Forsiuk <force@altlinux.org> 1.25-alt1
- 1.25

* Wed Oct 07 2009 Victor Forsyuk <force@altlinux.org> 1.24-alt1
- 1.24

* Tue Aug 16 2005 LAKostis <lakostis at altlinux.ru> 1.17-alt1
- 1.17.
- remove man3 pages (use perldoc instead).
- add lookup examples.
- fix prefix.

* Mon Apr 11 2005 LAKostis <lakostis at altlinux.ru> 1.14-alt1.1
- change license to GPL;
- fix buildreq;
- add lost man pages.

* Sat Apr 09 2005 LAKostis <lakostis at altlinux.ru> 1.14-alt1
- first build for Sisyphus.

