%define dist BDB
Name: perl-%dist
Version: 1.91
Release: alt1.1.1.1.1
Epoch: 1

Summary: Asynchronous Berkeley DB access
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/M/ML/MLEHMANN/BDB-%{version}.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: libdb4-devel perl-common-sense perl-devel

%description
See the BerkeleyDB documentation
(http://www.oracle.com/technology/documentation/berkeley-db/db/index.html).
The BDB API is very similar to the C API (the translation has been very
faithful).

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/BDB*
%perl_vendor_autolib/BDB

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.91-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:1.91-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1:1.91-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.91-alt1.1
- rebuild with new perl 5.20.1

* Mon Apr 14 2014 Igor Vlasenko <viy@altlinux.ru> 1:1.91-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1:1.9-alt2
- built for perl 5.18

* Thu Aug 30 2012 Vladimir Lettiev <crux@altlinux.ru> 1:1.9-alt1
- 1,89 -> 1.9
- built for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.89-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 1.89-alt1
- automated CPAN update

* Fri Nov 05 2010 Vladimir Lettiev <crux@altlinux.ru> 1.88-alt1.1
- rebuilt with perl 5.12

* Fri Jul 16 2010 Igor Vlasenko <viy@altlinux.ru> 1.88-alt1
- automated CPAN update

* Fri Sep 05 2008 Michael Bochkaryov <misha@altlinux.ru> 1.71-alt1
- 1.71 version
- fix directory ownership violation
- spec file cleanup

* Thu Jul 17 2008 Michael Bochkaryov <misha@altlinux.ru> 1.6-alt1
- first build for ALT Linux Sisyphus

