%define _unpackaged_files_terminate_build 1
%define dist Set-Object
Name: perl-%dist
Version: 1.38
Release: alt1

Summary: Unordered collections (sets) of Perl Objects
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/R/RU/RURBAN/%{dist}-%{version}.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
This modules implements a set of objects, that is, an unordered
collection of objects without duplication.

%prep
%setup -q -n %{dist}-%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes.pod README
%perl_vendor_archlib/Set
%perl_vendor_autolib/Set

%changelog
* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.38-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1.1
- rebuild with new perl 5.22.0

* Sun Oct 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.35-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1.1
- rebuild with new perl 5.20.1

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.34-alt1
- automated CPAN update

* Sun Dec 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.32-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.31-alt2
- built for perl 5.18

* Wed Jul 24 2013 Igor Vlasenko <viy@altlinux.ru> 1.31-alt1
- automated CPAN update

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1.28-alt3
- rebuilt for perl-5.16

* Fri Oct 07 2011 Alexey Tourbin <at@altlinux.ru> 1.28-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 1.27-alt1.1
- rebuilt with perl 5.12

* Tue Apr 20 2010 Alexey Tourbin <at@altlinux.ru> 1.27-alt1
- 1.25 -> 1.27

* Tue Sep 23 2008 Michael Bochkaryov <misha@altlinux.ru> 1.25-alt1
- 1.25 version
- fix directory ownership violation

* Sun Apr 20 2008 Michael Bochkaryov <misha@altlinux.ru> 1.22-alt1
- sub-classing interface added

* Tue Mar 27 2007 Sir Raorn <raorn@altlinux.ru> 1.21-alt1
- first build for ALT Linux Sisyphus

