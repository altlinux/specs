# for perl 5.20.1 rebuild - let us wait for upstream to fix it
%define _without_test 1

%define dist PerlIO-Util
Name: perl-%dist
Version: 0.72
Release: alt5.1.1.1.1

Summary: A selection of general PerlIO utilities
License: Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz
# Patch from https://rt.cpan.org/Public/Bug/Display.html?id=74539
Patch: %name-0.72-refcnt.patch

# Automatically added by buildreq on Sat Oct 08 2011
BuildRequires: perl-Module-Install perl-autodie perl-threads

%description
PerlIO::Util provides general PerlIO utilities: utility layers and utility
methods.

%prep
%setup -q -n %dist-%version
%patch -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/PerlIO
%perl_vendor_autolib/PerlIO

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.72-alt5.1.1.1.1
- rebuild with new perl 5.26.1

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.72-alt5.1.1.1
- rebuild with new perl 5.24.1

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.72-alt5.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.72-alt5.1
- rebuild with new perl 5.20.1

* Sun Dec 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.72-alt5
- preparation for perl 5.20.1 update

* Wed Aug 28 2013 Vladimir Lettiev <crux@altlinux.ru> 0.72-alt4
- built for perl 5.18

* Fri Aug 31 2012 Vladimir Lettiev <crux@altlinux.ru> 0.72-alt3
- rebuilt for perl-5.16
- fixed test t/06_tee.t

* Sat Oct 08 2011 Alexey Tourbin <at@altlinux.ru> 0.72-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 0.72-alt1
- automated CPAN update

* Thu Nov 04 2010 Vladimir Lettiev <crux@altlinux.ru> 0.71-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 0.71-alt1
- automated CPAN update

* Mon Oct 06 2008 Igor Vlasenko <viy@altlinux.ru> 0.42-alt1.1
- NMU for unknown reason

* Sat Jun 21 2008 Michael Bochkaryov <misha@altlinux.ru> 0.42-alt1
- first build for ALT Linux Sisyphus
