%define module Sys-Hostname-FQDN

Name: perl-%module
Version: 0.12
Release: alt1.1.1.1.1

Packager: Victor Forsiuk <force@altlinux.org>

Summary: Get the short or long hostname
License: Perl
Group: Development/Perl

URL: %CPAN %module
Source: http://www.cpan.org/authors/id/M/MI/MIKER/Sys-Hostname-FQDN-%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-devel

%description
Sys::Hostname::FQDN uses the host C library to discover the (usually) short
host name, then uses (perl) gethostbyname to extract the real hostname.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Sys
%perl_vendor_autolib/Sys

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1.1
- rebuild with new perl 5.20.1

* Tue Nov 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt4
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.11-alt3
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.11-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.10-alt1.1
- rebuilt with perl 5.12

* Thu Apr 08 2010 Victor Forsiuk <force@altlinux.org> 0.10-alt1
- 0.10

* Tue Dec 30 2008 Victor Forsyuk <force@altlinux.org> 0.09-alt1
- 0.09

* Thu Jul 05 2007 Victor Forsyuk <force@altlinux.org> 0.07-alt1
- Initial build.
