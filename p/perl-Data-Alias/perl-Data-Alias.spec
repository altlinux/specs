%def_without test
%define _unpackaged_files_terminate_build 1
%define dist Data-Alias
Name: perl-%dist
Version: 1.20
Release: alt1.1.1

Summary: Comprehensive set of aliasing operations
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/Z/ZE/ZEFRAM/Data-Alias-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Filter perl-Module-Install perl-Test-Pod

%description
Data::Alias is a module that allows you to apply "aliasing semantics" to
a section of code, causing aliases to be made whereever Perl would normally
make copies instead.  You can use this to improve efficiency and readability,
when compared to using references.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Data
%perl_vendor_autolib/Data

%changelog
* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1.1.1
- disabled tests til new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1.1
- rebuild with new perl 5.22.0

* Mon Oct 26 2015 Igor Vlasenko <viy@altlinux.ru> 1.20-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1.1
- rebuild with new perl 5.20.1

* Mon Sep 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

* Tue Aug 27 2013 Vladimir Lettiev <crux@altlinux.ru> 1.17-alt2
- built for perl 5.18

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1
- automated CPAN update

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1.16-alt1
- 1.15 -> 1.16
- rebuilt for perl-5.14

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.15-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1
- automated CPAN update

* Mon Jan 24 2011 Alexey Tourbin <at@altlinux.ru> 1.11-alt1
- 1.08 -> 1.11

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 1.08-alt1
- new version 1.08
- built with perl 5.12

* Wed Apr 21 2010 Alexey Tourbin <at@altlinux.ru> 1.07-alt1
- initial revision
