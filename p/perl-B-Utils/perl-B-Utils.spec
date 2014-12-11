%define dist B-Utils
Name: perl-%dist
Version: 0.25
Release: alt1.1

Summary: Helper functions for op tree manipulation
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/J/JJ/JJORE/B-Utils-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-ExtUtils-CBuilder perl-ExtUtils-Depends perl-Task-Weaken

%description
B::Utils - Helper functions for op tree manipulation

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_autolib/B
%perl_vendor_archlib/B

%changelog
* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1.1
- rebuild with new perl 5.20.1

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.21-alt2
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.21-alt1
- 0.15 -> 0.21
- built for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.15-alt1
- 0.07 -> 0.15
- built for perl-5.14

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.07-alt1.1
- rebuilt with perl 5.12

* Sun Jan 11 2009 Vitaly Lipatov <lav@altlinux.ru> 0.07-alt1
- initial build for ALT Linux Sisyphus
