%define dist Devel-Mallinfo
Name: perl-%dist
Version: 14
Release: alt1.1.1.1

Summary: Get mallinfo() malloc memory stats
License: GPLv3
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/K/KR/KRYDE/Devel-Mallinfo-%{version}.tar.gz

# Automatically added by buildreq on Mon Oct 10 2011
BuildRequires: perl-BSD-Resource perl-devel

%description
Devel::Mallinfo is an interface to the C library mallinfo() function
giving malloc memory allocation statistics.  This is meant for
development use, to give an idea of how much space your program and
any libraries are using from malloc().

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README examples
%perl_vendor_archlib/Devel
%perl_vendor_autolib/Devel

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 14-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 14-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 14-alt1.1
- rebuild with new perl 5.22.0

* Thu Dec 25 2014 Igor Vlasenko <viy@altlinux.ru> 14-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 13-alt1.1
- rebuild with new perl 5.20.1

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 13-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 12-alt2
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 12-alt1
- 11 -> 12
- built for perl-5.16

* Mon Oct 10 2011 Alexey Tourbin <at@altlinux.ru> 11-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 11-alt1
- automated CPAN update

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 3-alt2.1
- repair after perl 5.12 upgrade using girar-nmu

* Thu Sep 04 2008 Mikhail Pokidko <pma@altlinux.org> 3-alt2
- sisyphus_check fixes

* Thu May 29 2008 Mikhail Pokidko <pma@altlinux.org> 3-alt1
- first build for ALT Linux Sisyphus
