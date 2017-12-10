%define _unpackaged_files_terminate_build 1
%define dist Math-Pari
Name: perl-%dist
Version: 2.01080900
Release: alt2
Epoch: 1

Summary: Perl interface to PARI
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/I/IL/ILYAZ/modules/Math-Pari-%{version}.zip
Source1: http://pari.math.u-bordeaux.fr/pub/pari/unix/OLD/pari-2.3.5.tar.gz
# from fc perl-Math-Pari-2.010809-7
Patch0:		Math-Pari-2.010809b-no-fake-version.patch
Patch1:		Math-Pari-2.010802-docs-and-testsuite.patch
Patch2:		Math-Pari-2.01080605-include-path.patch
Patch3:		Math-Pari-2.010809b-utf8.patch
Patch4:		Math-Pari-2.010809b-escape-left-braces-in-regex.patch
Patch5:		Math-Pari-2.010809b-MP_NOGNUPLOT.patch

# Automatically added by buildreq on Wed Oct 19 2011
BuildRequires: perl-devel unzip

%description
This package is a Perl interface to famous library PARI for
numerical/scientific/number-theoretic calculations.  It allows use of
most PARI functions as Perl functions, and (almost) seamless merging
of PARI and Perl data. In what follows we suppose prior knowledge of
what PARI is (see <ftp://megrez.math.u-bordeaux.fr/pub/pari>, or
Math::libPARI).

%prep
%setup -q -n %dist-%version

# We want to build the docs and test suite too
%patch1 -p1

# Use <pari/pari.h> as per pari upstream documentation
#patch2

# Recode Changes file as UTF-8
%patch3

# Escape left braces in regexes (#1452519)
%patch4

# Fix operation of MP_NOGNUPLOT
%patch5


%build
# TODO: remove
export PERL_USE_UNSAFE_INC=1
%perl_vendor_build pari_tgz=%SOURCE1

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_archlib/Math
%perl_vendor_autolib/Math

%changelog
* Sun Dec 10 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.01080900-alt2
- added patches for perl 5.26

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.01080900-alt1.1
- rebuild with new perl 5.24.1

* Thu May 26 2016 Igor Vlasenko <viy@altlinux.ru> 1:2.01080900-alt1
- automated CPAN update

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1:2.010808-alt1.1.1
- rebuild with new perl 5.22.0

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.010808-alt1.1
- rebuild with new perl 5.20.1

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 1:2.010808-alt1
- automated CPAN update

* Fri May 02 2014 Igor Vlasenko <viy@altlinux.ru> 2.01080607-alt1
- automated CPAN update

* Thu Aug 29 2013 Vladimir Lettiev <crux@altlinux.ru> 2.01080605-alt4
- built for perl 5.18

* Sun Sep 02 2012 Vladimir Lettiev <crux@altlinux.ru> 2.01080605-alt3
- rebuilt for perl-5.16

* Wed Oct 19 2011 Alexey Tourbin <at@altlinux.ru> 2.01080605-alt2
- rebuilt for perl-5.14

* Mon Sep 19 2011 Igor Vlasenko <viy@altlinux.ru> 2.01080605-alt1
- automated CPAN update

* Sat Nov 06 2010 Vladimir Lettiev <crux@altlinux.ru> 2.01080604-alt1.1
- rebuilt with perl 5.12

* Tue Jul 13 2010 Igor Vlasenko <viy@altlinux.ru> 2.01080604-alt1
- automated CPAN update

* Sat Sep 06 2008 Vitaly Lipatov <lav@altlinux.ru> 2.010709-alt2
- fix directory ownership violation

* Sat Nov 11 2006 Vitaly Lipatov <lav@altlinux.ru> 2.010709-alt1
- new version (2.010709)
- fix build

* Mon Jun 05 2006 Vitaly Lipatov <lav@altlinux.ru> 2.010706-alt1
- new version (2.010706)

* Sun Dec 04 2005 Vitaly Lipatov <lav@altlinux.ru> 2.010702-alt1
- new version; TODO: what about linking with system libpari?
- add textrel=relaxed :(

* Thu Oct 06 2005 Vitaly Lipatov <lav@altlinux.ru> 2.010604-alt1
- new version

* Sat Aug 27 2005 Vitaly Lipatov <lav@altlinux.ru> 2.010603-alt1
- first build for ALT Linux Sisyphus
