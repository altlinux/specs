%define _unpackaged_files_terminate_build 1
%define dist MRO-Define
Name: perl-%dist
Version: 0.02
Release: alt1.1.1.1.1

Summary: Define your own method resolution order
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/F/FL/FLORA/MRO-Define-%{version}.tar.gz

# Automatically added by buildreq on Wed Nov 16 2011
BuildRequires: perl-Variable-Magic perl-devel

%description
With recent versions of perl it is possible to change the method
resolution order (mro) of a given class either by using "use mro" as
shown in the synopsis, or by using the "mro::set_mro".

Perl itself comes with two MROs by default. The traditional Perl default
MRO (depth first search, DFS) and C3 MRO.

This module allows you to define custom method resolution orders in
addition to those perl already has.

%prep
%setup -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/MRO
%perl_vendor_autolib/MRO

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1.1
- rebuild with new perl 5.20.1

* Thu Sep 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- automated CPAN update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.01-alt5
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.01-alt4
- rebuilt for perl-5.16

* Wed Nov 16 2011 Alexey Tourbin <at@altlinux.ru> 0.01-alt3
- disabled build dependency on perl-Module-Install

* Sun Oct 09 2011 Alexey Tourbin <at@altlinux.ru> 0.01-alt2
- rebuilt for perl-5.14

* Thu Sep 29 2011 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial build for ALT Linux Sisyphus
