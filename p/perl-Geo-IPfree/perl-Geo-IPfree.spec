%define _unpackaged_files_terminate_build 1
Epoch: 1
%define module Geo-IPfree

Name: perl-%module
Version: 1.16
Release: alt1.1

Summary: Geo::IPfree - Look up country by IP Address
License: Perl
Group: Development/Perl

BuildArch: noarch

Url: %CPAN %module
Source0: http://www.cpan.org/authors/id/A/AT/ATOOMIC/%{module}-%{version}.tar.gz

# Automatically added by buildreq on Tue Nov 16 2010
BuildRequires: perl-Memoize perl-Test-Pod perl-Test-Pod-Coverage

%description
Look up country of IP Address. This module make this off-line and the DB of IPs
is free and small.

%prep
%setup -q -n %{module}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Geo

%changelog
* Sun Jan 30 2022 Igor Vlasenko <viy@altlinux.org> 1:1.16-alt1.1
- automated CPAN update

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.151940-alt1
- automated CPAN update

* Sat Jan 03 2015 Igor Vlasenko <viy@altlinux.ru> 1.143630-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.141670-alt1
- automated CPAN update

* Mon Feb 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.140470-alt1
- automated CPAN update

* Tue Oct 15 2013 Igor Vlasenko <viy@altlinux.ru> 1.132870-alt1
- automated CPAN update

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.131650-alt1
- automated CPAN update

* Wed Oct 17 2012 Igor Vlasenko <viy@altlinux.ru> 1.122880-alt1
- automated CPAN update

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 1.121660-alt1
- automated CPAN update

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
