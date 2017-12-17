%define dist SGML-Parser-OpenSP
Name: perl-%dist
Version: 0.994
Release: alt3.1.1.1.1

Summary: Parse SGML documents using OpenSP
License: Perl
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: gcc-c++ libOpenSP-devel perl-Class-Accessor perl-Test-Exception perl-Test-Pod

%description
This module provides an interface to the OpenSP SGML parser.
OpenSP and this module are event based. As the parser recognizes
parts of the document (say the start or end of an element),
then any handlers registered for that type of an event
are called with suitable parameters.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/SGML
%perl_vendor_autolib/SGML

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.994-alt3.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.994-alt3.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.994-alt3.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.994-alt3.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.994-alt3
- built for perl 5.18

* Sat Sep 01 2012 Vladimir Lettiev <crux@altlinux.ru> 0.994-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.994-alt1.2
- rebuilt for perl-5.14

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 0.994-alt1.1
- rebuilt with perl 5.12

* Sat Sep  6 2008 Sergey Kurakin <kurakin@altlinux.ru> 0.994-alt1
- 0.994
- license changed (was: Artistic or GPL)

* Fri Apr 25 2008 Sergey Kurakin <kurakin@altlinux.ru> 0.991-alt1
- first build for AltLinux Sisyphus
