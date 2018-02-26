%define module Geo-IPfree

Name: perl-%module
Version: 1.120460
Release: alt1

Summary: Geo::IPfree - Look up country by IP Address
License: Perl
Group: Development/Perl

BuildArch: noarch

Url: %CPAN %module
Source: http://www.cpan.org/authors/id/B/BR/BRICAS/Geo-IPfree-%version.tar.gz

# Automatically added by buildreq on Tue Nov 16 2010
BuildRequires: perl-Memoize perl-Test-Pod perl-Test-Pod-Coverage

%description
Look up country of IP Address. This module make this off-line and the DB of IPs
is free and small.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes benchmark
%perl_vendor_privlib/Geo

%changelog
* Fri Mar 23 2012 Victor Forsiuk <force@altlinux.org> 1.120460-alt1
- 1.120460

* Sun Jan 15 2012 Victor Forsiuk <force@altlinux.org> 1.112870-alt1
- 1.112870

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.112490-alt1
- automated CPAN update

* Sun Apr 10 2011 Victor Forsiuk <force@altlinux.org> 1.110450-alt1
- 1.110450

* Tue Nov 16 2010 Victor Forsiuk <force@altlinux.org> 1.102870-alt1
- 1.102870
- License is now Artistic 2.0.

* Wed Oct 07 2009 Victor Forsyuk <force@altlinux.org> 0.7-alt1
- 0.7
- Remove unneeded conflict with alternative packages.

* Mon Apr 11 2005 LAKostis <lakostis at altlinux.ru> 0.2-alt1.1
- spec cleanup.

* Sat Apr 09 2005 LAKostis <lakostis at altlinux.ru> 0.2-alt1
- first build for Sisyphus.
