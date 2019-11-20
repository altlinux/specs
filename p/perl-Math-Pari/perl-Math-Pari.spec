Epoch: 2
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(LWP/UserAgent.pm) perl(Net/FTP.pm) perl-podlators unzip
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%global extraversion	%{nil}
%global extrasuffix	%{nil}

Summary:	Perl interface to PARI
Name:		perl-Math-Pari
Version:	2.030518
Release:	alt1_3
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Math-Pari
Source0:	https://cpan.metacpan.org/modules/by-module/Math/Math-Pari-%{version}%{extraversion}%{?extrasuffix}.zip
Patch0:		Math-Pari-2.030518-system-pari.patch
Patch1:		Math-Pari-2.030506-docs-and-testsuite.patch
Patch3:		Math-Pari-2.030512-utf8.patch
Patch4:		Math-Pari-2.030506-escape-left-braces-in-regex.patch
Patch5:		Math-Pari-2.030518-MP_NOGNUPLOT.patch
Patch6:		Math-Pari-2.030509-optflags.patch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	gcc
BuildRequires:	libpari23-devel
BuildRequires:	perl-devel
BuildRequires:	perl-devel
BuildRequires:	rpm-build-perl
BuildRequires:	perl(Config.pm)
BuildRequires:	perl(Cwd.pm)
BuildRequires:	perl(ExtUtils/Constant.pm)
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(File/Basename.pm)
BuildRequires:	perl(File/Copy.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	sed
# Module Runtime
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(DynaLoader.pm)
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(overload.pm)
BuildRequires:	perl(subs.pm)
# Test Suite
# (no additional dependencies)
# Dependencies

# Enforce dependency against same version of pari that we're built for
Requires:	libpari23 = %(pkg-config --modversion libpari23 2>/dev/null || echo 0)
Source44: import.info

# Don't "provide" private Perl libs or the redundant unversioned perl(Math::Pari)

%description
This package is a Perl interface to the famous library PARI for numerical/
scientific/ number-theoretic calculations. It allows use of most PARI functions
as Perl functions, and (almost) seamless merging of PARI and Perl data.

%prep
%setup -q -n Math-Pari-%{version}%{extraversion}

# Create a directory structure for libpari23 like Math::Pari expects it to be
mkdir libpari23
ln -s $(pkg-config --cflags-only-I libpari23 | sed -e 's/-I//') libpari23/include
ln -s $(pkg-config --variable=paridir libpari23)/src libpari23/src

# Fix for using system pari library (with source available)
%patch0

# We want to build the docs and test suite too
%patch1

# Recode Changes file as UTF-8
%patch3

# Escape left braces in regexes (#1452519)
%patch4

# Fix operation of MP_NOGNUPLOT
%patch5

# Don't try to fiddle with compiler flags, we'll set them ourselves anyway
%patch6

%build
paridir=$(pkg-config --variable=paridir libpari23)
perl Makefile.PL \
	INSTALLDIRS=vendor \
	NO_PACKLIST=1 \
	NO_PERLLOCAL=1 \
	OPTIMIZE="$(pkg-config --cflags-only-I libpari23) %{optflags}" \
	paridir="${paridir}" \
	pariincludes=$(pwd)/libpari23 \
	parilibs="$(pkg-config --libs libpari23)"
%{make_build}

%install
%{makeinstall_std}
find %{buildroot} -type f -name '*.bs' -empty -delete
# %{_fixperms} -c %{buildroot}

%check
make test MP_NOGNUPLOT=1

%files
%doc Changes README
%dir %{perl_vendor_archlib}/Math/
%exclude %doc %{perl_vendor_archlib}/Math/libPARI.dumb.pod
%doc %{perl_vendor_archlib}/Math/libPARI.pod
%{perl_vendor_archlib}/Math/*.pm
%{perl_vendor_archlib}/auto/Math/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 2:2.030518-alt1_3
- update to new release by fcimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 2:2.030518-alt1_1
- new version

* Sat Apr 06 2019 Igor Vlasenko <viy@altlinux.ru> 2:2.030517-alt1
- automated CPAN update

* Fri Apr 05 2019 Igor Vlasenko <viy@altlinux.ru> 2:2.030516-alt1
- automated CPAN update

* Tue Apr 02 2019 Igor Vlasenko <viy@altlinux.ru> 2:2.030515-alt1_1
- new version

* Thu Mar 21 2019 Igor Vlasenko <viy@altlinux.ru> 2:2.030510-alt1
- automated CPAN update

* Sat Mar 02 2019 Igor Vlasenko <viy@altlinux.ru> 2:2.030509-alt1
- automated CPAN update

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 2:2.030508-alt1
- automated CPAN update

* Thu Feb 28 2019 Igor Vlasenko <viy@altlinux.ru> 2:2.030507-alt2_2
- clean up thanks to ldv

* Thu Feb 28 2019 Igor Vlasenko <viy@altlinux.ru> 2:2.030507-alt1_2
- new version

* Thu Jan 24 2019 Igor Vlasenko <viy@altlinux.ru> 1:2.01080900-alt2.2
- rebuild with new perl 5.28.1

* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1:2.01080900-alt2.1
- rebuild with new perl 5.26.1

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
