%define _unpackaged_files_terminate_build 1
%define module Geo-IP

Name: perl-%module
Version: 1.51
Release: alt1.1

Packager: Victor Forsyuk <force@altlinux.org>

Summary: Look up country by IP Address 
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/M/MA/MAXMIND/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libGeoIP-devel perl-devel

%description
This module uses a file-based database. This database simply contains IP blocks
as keys, and countries as values. This database should be more complete and
accurate than reverse DNS lookups.

%prep
%setup -q -n %{module}-%{version}

find lib/ example/ -type f -print0 | xargs -r0 %__subst -p 's./usr/local/share/GeoIP./usr/share/GeoIP.'

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README* Changes example CONTRIBUTING.md
%perl_vendor_archlib/Geo
%perl_vendor_autolib/Geo

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1.1
- rebuild with new perl 5.26.1

* Thu Oct 12 2017 Igor Vlasenko <viy@altlinux.ru> 1.51-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.50-alt1.1
- rebuild with new perl 5.24.1

* Mon Jul 25 2016 Igor Vlasenko <viy@altlinux.ru> 1.50-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.45-alt1.1
- rebuild with new perl 5.22.0

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.45-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.43-alt1.1
- rebuild with new perl 5.20.1

* Tue Jun 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.43-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.42-alt1
- 1.41 -> 1.42

* Wed Apr 17 2013 Andrey Cherepanov <cas@altlinux.org> 1.41-alt1
- New version 1.41 with correct test for libGeoIP-1.5.0

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.40-alt2
- rebuilt for perl-5.16

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
