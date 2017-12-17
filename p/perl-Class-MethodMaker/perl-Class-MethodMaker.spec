%define dist Class-MethodMaker
Name: perl-%dist
Version: 2.24
Release: alt1.1.1.1

Summary: Easy building of Perl Classes
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/S/SC/SCHWIGON/class-methodmaker/Class-MethodMaker-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-IPC-Run perl-autodie perl-devel

%description
This module solves the problem of having to continually write
accessor methods for your objects that perform standard tasks.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Class
%perl_vendor_autolib/Class

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 2.24-alt1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 2.24-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 2.24-alt1.1
- rebuild with new perl 5.22.0

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 2.24-alt1
- automated CPAN update

* Mon Jan 19 2015 Igor Vlasenko <viy@altlinux.ru> 2.22-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 2.21-alt1.1
- rebuild with new perl 5.20.1

* Mon Mar 17 2014 Igor Vlasenko <viy@altlinux.ru> 2.21-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 2.20-alt1
- automated CPAN update

* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 2.19-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 2.18-alt4
- built for perl 5.18

* Wed Aug 29 2012 Vladimir Lettiev <crux@altlinux.ru> 2.18-alt3
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 2.18-alt2
- rebuilt for perl-5.14

* Sat Apr 23 2011 Alexey Tourbin <at@altlinux.ru> 2.18-alt1
- 2.13 -> 2.18

* Mon Nov 08 2010 Vladimir Lettiev <crux@altlinux.ru> 2.13-alt1.1
- rebuilt with perl 5.12

* Tue Dec 16 2008 Alexey Tourbin <at@altlinux.ru> 2.13-alt1
- 2.07 -> 2.13

* Tue Jun 14 2005 Alexey Tourbin <at@altlinux.ru> 2.07-alt1
- initial revision (required for WWW::Bugzilla)
