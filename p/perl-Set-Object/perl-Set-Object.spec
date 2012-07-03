%define dist Set-Object
Name: perl-%dist
Version: 1.28
Release: alt2

Summary: Unordered collections (sets) of Perl Objects
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Fri Oct 07 2011
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
This modules implements a set of objects, that is, an unordered
collection of objects without duplication.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes.pod README
%perl_vendor_archlib/Set
%perl_vendor_autolib/Set

%changelog
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

