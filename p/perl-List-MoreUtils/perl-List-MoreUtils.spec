%define _unpackaged_files_terminate_build 1
%define dist List-MoreUtils
Name: perl-%dist
Version: 0.415
Release: alt1.1

Summary: Provide the stuff missing in List::Util
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/R/RE/REHSACK/List-MoreUtils-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-ExtUtils-CBuilder perl(Exporter/Tiny.pm)

%description
List::MoreUtils provides some trivial but commonly needed functionality
on lists which is not going to go into List::Util.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README*
%perl_vendor_archlib/List
%perl_vendor_autolib/List

%changelog
* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.415-alt1.1
- rebuild with new perl 5.24.1

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.415-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.413-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 0.413-alt1
- automated CPAN update

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 0.404-alt1
- automated CPAN update

* Mon Dec 29 2014 Igor Vlasenko <viy@altlinux.ru> 0.402-alt1
- automated CPAN update

* Mon Dec 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.401-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.33-alt4.1
- rebuild with new perl 5.20.1

* Sun Aug 25 2013 Vladimir Lettiev <crux@altlinux.ru> 0.33-alt4
- built for perl 5.18

* Tue Aug 28 2012 Vladimir Lettiev <crux@altlinux.ru> 0.33-alt3
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 0.33-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- automated CPAN update

* Sat Dec 18 2010 Alexey Tourbin <at@altlinux.ru> 0.30-alt1
- 0.22 -> 0.30

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.22-alt1.1
- rebuilt with perl 5.12

* Thu Aug 31 2006 Alexey Tourbin <at@altlinux.ru> 0.22-alt1
- 0.10 -> 0.22

* Thu Sep 08 2005 Alexey Tourbin <at@altlinux.ru> 0.10-alt1
- initial revision (for PPI)
