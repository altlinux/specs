%define _without_test 1
%define dist Time-Format_XS
Name: perl-%dist
Version: 1.03
Release: alt6

Summary: Companion module for Time::Format, to speed up time formatting
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
Source1: ppport.h
Patch1: %name-%version-perl518.patch
Patch2: Time-Format_XS-1.03-add-declarations.patch
Patch3: Time-Format_XS-1.03-fix-segfault.patch

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-DateTime perl-devel

%description
This is a companion module to Time::Format.  It contains a version
of the time_format function written in C, so it is much faster.

%prep
%setup -q -n %dist-%version
cp -f %{SOURCE1} .
%patch1 -p2
%patch2 -p1
%patch3 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_autolib/Time
%perl_vendor_archlib/Time

%changelog
* Wed Jun 02 2021 Igor Vlasenko <viy@altlinux.org> 1.03-alt6
- disabled tests (random fail chance) for perl 5.32 rebuild

* Tue Mar 19 2019 Igor Vlasenko <viy@altlinux.ru> 1.03-alt5
- fixed segfault (closes: #36167) (closes: #36226)

* Mon Feb 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.03-alt4
- fixed undeclared functions in format.c

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1.03-alt3.2
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.03-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.03-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.03-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.03-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt3
- built for perl 5.18
- fixed tests

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.03-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.03-alt1.1
- rebuilt with perl 5.12

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 1.03-alt1
- New version 1.03

* Thu Mar 15 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.02-alt1
- Initial build for ALT Linux Sisyphus

* Wed Mar 14 2007 Nikolay A. Fetisov <naf@altlinux.ru> 1.02-alt0
- Initial build
