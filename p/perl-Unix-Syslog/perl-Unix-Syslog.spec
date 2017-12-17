%define dist Unix-Syslog
Name: perl-%dist
Version: 1.1
Release: alt3.1.1.1.1

Summary: Perl interface to the UNIX system logger
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-devel

%description
This Module provides access to the system logger available on most
UNIX system via Perl's XSUBs (Perl's C interface).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Unix
%perl_vendor_autolib/Unix

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.1-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt3
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.1-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.1-alt1.1
- rebuilt with perl 5.12

* Wed Jun 18 2008 Alexey Shabalin <shaba@altlinux.ru> 1.1-alt1
- new version 1.1

* Wed Oct 10 2007 Alexey Shabalin <shaba@altlinux.ru> 1.0-alt1
- new version 1.0

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 0.100-alt0.1.1
- Rebuilt with rpm-build-perl-0.5.1.

* Tue Dec 02 2003 Alexey Shabalin <shaba@altlinux.ru> 0.100-alt0.1
- First release for ALT
