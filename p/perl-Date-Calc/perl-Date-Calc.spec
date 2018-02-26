%define dist Date-Calc
Name: perl-%dist
Version: 6.3
Release: alt3

Summary: %dist module for perl
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Wed Oct 05 2011 (-bi)
BuildRequires: perl-Bit-Vector perl-Date-Calc-XS perl-devel

%description
This package consists of a C library (intended to make life easier for C
developers) and a Perl module to access this library from Perl.

The library provides all sorts of date calculations based on the Gregorian
calendar (the one used in all western countries today), thereby complying
with all relevant norms and standards: ISO/R 2015-1971, DIN 1355 and, to
some extent, ISO 8601 (where applicable).

The package is designed as an efficient (and fast) toolbox, not a bulky
ready-made application. It provides extensive documentation and examples
of use, multi-language support and special functions for business needs.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	CHANGES.txt CREDITS.txt README.txt
%dir	%perl_vendor_privlib/Date
	%perl_vendor_privlib/Date/*.pm
%doc	%perl_vendor_privlib/Date/*.pod
%dir	%perl_vendor_privlib/Date/Calc
	%perl_vendor_privlib/Date/Calc/*.pm
%doc	%perl_vendor_privlib/Date/Calc/*.pod
%dir	%perl_vendor_privlib/Date/Calendar
	%perl_vendor_privlib/Date/Calendar/*.pm
%doc	%perl_vendor_privlib/Date/Calendar/*.pod

%changelog
* Wed Oct 05 2011 Alexey Tourbin <at@altlinux.ru> 6.3-alt3
- rebuilt as plain src.rpm

* Fri Apr 30 2010 Alexey Tourbin <at@altlinux.ru> 6.3-alt2
- enabled dependency on Date::Calc::XS

* Fri Apr 30 2010 Alexey Tourbin <at@altlinux.ru> 6.3-alt1
- 5.4 -> 6.3

* Mon Apr 13 2009 Alexey Tourbin <at@altlinux.ru> 5.4-alt2
- rebuild

* Wed Oct 25 2006 Alexey Tourbin <at@altlinux.ru> 5.4-alt1
- 5.3 -> 5.4
- imported sources into git and built with gear
- use -fvisibility=hidden to hide underlying C library symbols
- use PERL_NO_GET_CONTEXT for some marginal performance gain
- for the same reason, use XSLoader instead of DynaLoader

* Sat Feb 19 2005 ALT QA Team Robot <qa-robot@altlinux.org> 5.3-alt2.1
- Rebuilt with rpm-build-perl-0.5.1.

* Mon Nov 04 2002 Stanislav Ievlev <inger@altlinux.ru> 5.3-alt2
- rebuild with new perl

* Mon Sep 30 2002 Igor Homyakov <homyakov at altlinux dot ru> 5.3-alt1
- 5.3

* Tue Sep 17 2002 Igor Homyakov <homyakov at altlinux dot ru> 5.1-alt1
- 5.1-alt1 
- cleanup spec file

* Wed Nov 14 2001 Igor Homyakov <homyakov@altlinux.ru> alt1 
- Build package for ALTLinux 
