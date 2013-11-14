# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Encode.pm) perl(English.pm) perl(open.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
%define fedora 19
# We need to patch the test suite if we have an old version of Test::More
%global old_test_more %(perl -MTest::More -e 'print (($Test::More::VERSION < 0.88) ? 1 : 0);' 2>/dev/null || echo 0)

# PPI can't handle the unicode byte order mark in t/bom.pl prior to version 1.204_02
%global old_ppi %(perl -MPPI -e 'print (($PPI::VERSION < 1.204_02) ? 1 : 0);' 2>/dev/null || echo 0)

# noarch, but to avoid debug* files interfering with manifest test:
%global debug_package %{nil}

Name:		perl-Test-Mojibake
Version:	0.8
Release:	alt2_4
Summary:	Check your source for encoding misbehavior
Group:		Development/Perl
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/Test-Mojibake/
Source0:	http://search.cpan.org/CPAN/authors/id/S/SY/SYP/Test-Mojibake-%{version}.tar.gz
Patch0:		Test-Mojibake-0.4-no-Test::Version.patch
Patch1:		Test-Mojibake-0.8-old-Test::More.patch
BuildArch:	noarch
# ===================================================================
# Module build requirements
# ===================================================================
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# ===================================================================
# Module requirements
# ===================================================================
BuildRequires:	perl(File/Spec/Functions.pm)
BuildRequires:	perl(Pod/Usage.pm)
BuildRequires:	perl(Test/Builder.pm)
# ===================================================================
# Optional module requirements
# ===================================================================
BuildRequires:	perl(Unicode/CheckUTF8.pm)
# ===================================================================
# Regular test suite requirements
# ===================================================================
BuildRequires:	perl(Test/Builder/Tester.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Script.pm)
# ===================================================================
# Author/Release test requirements
#
# Don't run these tests or include their requirements if we're
# bootstrapping, as many of these modules require each other for
# their author/release tests.
# ===================================================================
%if 0%{!?perl_bootstrap:1}
BuildRequires:	perl(Pod/Coverage/TrustPod.pm)
BuildRequires:	perl(Test/CPAN/Meta.pm)
BuildRequires:	perl(Test/DistManifest.pm)
BuildRequires:	perl(Test/EOL.pm)
BuildRequires:	perl(Test/HasVersion.pm)
BuildRequires:	perl(Test/Kwalitee.pm)
BuildRequires:	perl(Test/MinimumVersion.pm)
BuildRequires:	perl(Test/NoTabs.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
BuildRequires:	perl(Test/Portability/Files.pm)
BuildRequires:	perl(Test/Synopsis.pm)
# Modules only available from EL-6
%if 0%{?fedora} || 0%{?rhel} > 5
BuildRequires:	perl(Test/Perl/Critic.pm) perl(Perl/Critic.pm)
BuildRequires:	perl(Test/Vars.pm)
%endif
# Modules only available from EL-7
%if 0%{?fedora} || 0%{?rhel} > 6
BuildRequires:	perl(Perl/Critic/Policy/Modules/ProhibitModuleShebang.pm)
BuildRequires:	perl(Test/CPAN/Changes.pm)
#BuildRequires:	perl(Test/Version.pm)
%endif
# Modules only available from F-18, EL-7
%if 0%{?fedora} > 17 || 0%{?rhel} > 6
BuildRequires:	perl(Test/Pod/LinkCheck.pm)
%endif
%endif
# ===================================================================
# Runtime requirements
# ===================================================================
# Unicode::CheckUTF8 is an optional requirement that significantly speeds up
# this module
Requires:	perl(Unicode/CheckUTF8.pm)
Source44: import.info

%description
Many modern text editors automatically save files using UTF-8 codification.
However, the perl interpreter does not expect it by default. Whilst this does
not represent a big deal on (most) backend-oriented programs, Web framework
(Catalyst, Mojolicious) based applications will suffer so-called Mojibake
(literally: "unintelligible sequence of characters"). Even worse: if an editor
saves BOM (Byte Order Mark, U+FEFF character in Unicode) at the start of a
script with the executable bit set (on Unix systems), it won't execute at all,
due to shebang corruption.

Avoiding codification problems is quite simple:

 * Always use utf8/use common::sense when saving source as UTF-8
 * Always specify =encoding utf8 when saving POD as UTF-8
 * Do neither of above when saving as ISO-8859-1
 * Never save BOM (not that it's wrong; just avoid it as you'll barely
   notice its presence when in trouble)

However, if you find yourself upgrading old code to use UTF-8 or trying to
standardize a big project with many developers, each one using a different
platform/editor, reviewing all files manually can be quite painful, especially
in cases where some files have multiple encodings (note: it all started when I
realized that gedit and derivatives are unable to open files with character
conversion tables).

Enter the Test::Mojibake ;)

%prep
%setup -q -n Test-Mojibake-%{version}

# Test::Version not always available
%patch0

# We need to patch the test suite if we have an old version of Test::More
%if %{old_test_more}
%patch1 -p1
%endif

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%check
# PPI can't handle the unicode byte order mark in t/bom.pl prior to version 1.204_02
%if %{old_ppi}
mv t/release-minimum-version.t ./
sed -i -e 's|t/release-minimum-version.t|release-minimum-version.t|' MANIFEST
%endif
make test %{!?perl_bootstrap:AUTHOR_TESTING=1 RELEASE_TESTING=1}
%if %{old_ppi}
mv ./release-minimum-version.t t/
sed -i -e 's|release-minimum-version.t|t/release-minimum-version.t|' MANIFEST
%endif

%files
%doc Changes LICENSE README
%{_bindir}/scan_mojibake
%{perl_vendor_privlib}/Test/
%{_mandir}/man1/scan_mojibake.1*

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt2_4
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_2
- update to new release by fcimport

* Mon Feb 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.8-alt1_1
- update to new release by fcimport

* Wed Oct 03 2012 Igor Vlasenko <viy@altlinux.ru> 0.7-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.4-alt1_4
- update to new release by fcimport

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 0.3-alt1_4
- fc import

