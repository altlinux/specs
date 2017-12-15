%define _unpackaged_files_terminate_build 1
%define dist libintl-perl
Name: perl-libintl
Version: 1.29
Release: alt1.1

Summary: High-Level Interface to Uniforum Message Translation
License: LGPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source0: http://www.cpan.org/authors/id/G/GU/GUIDO/%{dist}-%{version}.tar.gz

# avoid rpmdb bloat
%add_findprov_skiplist */Locale/RecodeData/*

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Encode perl-devel

%description
The module Locale::TextDomain provides a high-level interface
to Perl message translation.

%prep
%setup -q -n %{dist}-%{version}

# disable linking with -lintl -liconv
sed -i- '/LIBS/d' gettext_xs/Makefile.PL

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc	README FAQ README-oldversions README.md README.solaris README.win32 Changes
%dir	%perl_vendor_privlib/Locale
	%perl_vendor_privlib/Locale/*.pm
%doc	%perl_vendor_privlib/Locale/*.pod
%dir	%perl_vendor_privlib/Locale/Recode
	%perl_vendor_privlib/Locale/Recode/*.pm
%dir	%perl_vendor_privlib/Locale/RecodeData
	%perl_vendor_privlib/Locale/RecodeData/*.pm
	%perl_vendor_autolib/Locale

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1.1
- rebuild with new perl 5.26.1

* Thu Nov 23 2017 Igor Vlasenko <viy@altlinux.ru> 1.29-alt1
- automated CPAN update

* Tue Sep 26 2017 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1
- automated CPAN update

* Wed Aug 30 2017 Igor Vlasenko <viy@altlinux.ru> 1.27-alt1
- automated CPAN update

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1.1
- rebuild with new perl 5.24.1

* Mon Jun 13 2016 Igor Vlasenko <viy@altlinux.ru> 1.26-alt1
- automated CPAN update

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.25-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1.1
- rebuild with new perl 5.22.0

* Fri May 22 2015 Igor Vlasenko <viy@altlinux.ru> 1.24-alt1
- automated CPAN update

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1.1
- rebuild with new perl 5.20.1

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 1.23-alt1
- 1.20 -> 1.23
- search path patch merged upstream

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 1.20-alt2
- rebuilt for perl-5.16

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 1.20-alt1
- 1.16 -> 1.20
- built for perl-5.12

* Sun Nov 07 2010 Vladimir Lettiev <crux@altlinux.ru> 1.16-alt3.1
- rebuilt with perl 5.12

* Sun Oct 26 2008 Pavlov Konstantin <thresh@altlinux.ru> 1.16-alt3
- Fix FTBFS on current Sisyphus.

* Tue Oct 24 2006 Pavlov Konstantin <thresh@altlinux.ru> 1.16-alt1
- 1.16 version.

* Sun Apr 17 2005 Yuri N. Sedunov <aris@altlinux.ru> 1.11-alt2
- requires libdb4-devel for build.
- fixed default search path for .mo files. (#6285).

* Tue Jan 18 2005 Alexey Tourbin <at@altlinux.ru> 1.11-alt1
- initial revision
