## SPEC file for Perl module Net::CUPS

Name: perl-Net-CUPS
Version: 0.64
Release: alt1.1

Summary: Perl interface to the Common Unix Printing System API
Summary(ru_RU.UTF-8): интерфейс Perl к API Common Unix Printing System

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/dist/Net-CUPS/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

%define real_name Net-CUPS
Source: %real_name-%version.tar

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sat Jul 30 2016
# optimized out: libcups-devel libgpg-error perl python-base python-modules python3
BuildRequires: cups-filters-devel perl-Encode perl-devel

%description
Perl module  Net::CUPS is an interface to the Common Unix Printing
System API.  It provides an ability  for calling most functions of 
the C CUPS API from Perl.

%description -l ru_RU.UTF-8
Модуль Perl  Net::CUPS  предоставляет интерфейс к  API Common Unix 
Printing System (CUPS). Он предоставляет возможность использования
большинства функций C API для CUPS из Perl.


%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes TODO examples
%exclude /.perl.req
%perl_vendor_autolib/Net
%perl_vendor_archlib/Net

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.64-alt1.1
- rebuild with new perl 5.26.1

* Sat Jun 10 2017 Nikolay A. Fetisov <naf@altlinux.org> 0.64-alt1
- New version

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.63-alt1.1
- rebuild with new perl 5.24.1

* Sun Nov 06 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.63-alt1
- New version

* Sat Jul 30 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.62-alt1
- New version

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.61-alt5.1
- rebuild with new perl 5.22.0

* Thu Nov 19 2015 Igor Vlasenko <viy@altlinux.ru> 0.61-alt5
- fix for cups > 2

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.61-alt4.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.61-alt4
- built for perl 5.18

* Thu Oct 18 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.61-alt3
- Fix build with CUPS 1.6 (Closes: 27848)

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.61-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.61-alt1.2
- rebuilt for perl-5.14

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 0.61-alt1.1
- rebuilt with perl 5.12

* Sat Oct 17 2009 Nikolay A. Fetisov <naf@altlinux.ru> 0.61-alt1
- New version 0.61

* Sun Dec 14 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.59-alt1
- New version 0.59

* Mon Apr 07 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.55-alt2
- Fix build with CUPS 1.3.7

* Thu Feb 28 2008 Nikolay A. Fetisov <naf@altlinux.ru> 0.55-alt1
- New version 0.55

* Sun Mar 25 2007 Nikolay A. Fetisov <naf@altlinux.ru> 0.51-alt1
- New version 0.51
  - Reworked the entire module into the new design

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.41-alt1
- Initial build for ALT Linux Sisyphus

* Thu Aug 10 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.41-alt0
- Initial build
