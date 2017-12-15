%define dist Devel-Caller
Name: perl-%dist
Version: 2.06
Release: alt2.1.1.1.1

Summary: Meatier versions of caller()
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RC/RCLAMP/Devel-Caller-%{version}.tar.gz

# Automatically added by buildreq on Sun Oct 09 2011
BuildRequires: perl-PadWalker perl-devel

%description
Devel::Caller module provides meatier versions of "caller" function.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/Devel
%perl_vendor_autolib/Devel

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.06-alt2.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.06-alt2.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.06-alt2.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.06-alt2.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 2.06-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 2.06-alt1
- automated CPAN update

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 2.05-alt2
- rebuilt for perl-5.16

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 2.05-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 2.05-alt1.1
- rebuilt with perl 5.12

* Wed Apr 21 2010 Alexey Tourbin <at@altlinux.ru> 2.05-alt1
- 2.03 -> 2.05

* Mon Jul 21 2008 Michael Bochkaryov <misha@altlinux.ru> 2.03-alt1
- first build for ALT Linux Sisyphus
