# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
# noarch, but to avoid debug* files interfering with manifest test:
%global debug_package %{nil}

Name:		perl-Test-Version
Version:	1.002003
Release:	alt2_1
Summary:	Check to see that versions in modules are sane
License:	Artistic 2.0
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Test-Version/
Source0:	http://search.cpan.org/CPAN/authors/id/X/XE/XENO/Test-Version-%{version}.tar.gz
Patch1:		Test-Version-1.002003-pod-spell.patch
BuildArch:	noarch
# ===================================================================
# Module build requirements
# ===================================================================
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# ===================================================================
# Module requirements
# ===================================================================
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(File/Find/Rule/Perl.pm)
BuildRequires:	perl(Module/Metadata.pm)
BuildRequires:	perl(parent.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(version.pm)
BuildRequires:	perl(warnings.pm)
# ===================================================================
# Regular test suite requirements
# ===================================================================
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(IO/Handle.pm)
BuildRequires:	perl(IPC/Open3.pm)
BuildRequires:	perl(Scalar/Util.pm)
BuildRequires:	perl(Test/Exception.pm)
BuildRequires:	perl(Test/Tester.pm)
# ===================================================================
# Author/Release test requirements
#
# Don't run these tests or include their requirements if we're
# bootstrapping, as many of these modules require each other for
# their author/release tests.
# ===================================================================
%if 0%{!?perl_bootstrap:1}
BuildRequires:	perl(English.pm)
BuildRequires:	perl(Pod/Coverage/TrustPod.pm)
BuildRequires:	perl(Pod/Wordlist.pm)
BuildRequires:	perl(Test/CPAN/Changes.pm)
BuildRequires:	perl(Test/CPAN/Meta.pm)
BuildRequires:	perl(Test/CPAN/Meta/JSON.pm)
BuildRequires:	perl(Test/DistManifest.pm)
BuildRequires:	perl(Test/EOL.pm)
BuildRequires:	perl(Test/MinimumVersion.pm)
BuildRequires:	perl(Test/Mojibake.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Perl/Critic.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
BuildRequires:	perl(Test/Pod/LinkCheck.pm)
BuildRequires:	perl(Test/Portability/Files.pm)
BuildRequires:	perl(Test/Synopsis.pm)
BuildRequires:	perl(Test/Vars.pm)
# RHEL-7+ package cannot BR: packages from EPEL
%if ! (0%{?rhel} >= 7)
BuildRequires:	hunspell-en
BuildRequires:	perl(Test/Spelling.pm)
%endif
%endif
Source44: import.info
# ===================================================================
# Runtime requirements
# ===================================================================

%description
This module's goal is to be a one stop shop for checking to see that your
versions across your dist are sane.

%prep
%setup -q -n Test-Version-%{version}

# Some spell checkers check "doesn" rather than "doesn't"
%patch1

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%check
make test %{!?perl_bootstrap:AUTHOR_TESTING=1 RELEASE_TESTING=1}

%files
%doc Changes CONTRIBUTING LICENSE README
%{perl_vendor_privlib}/Test/

%changelog
* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.002003-alt2_1
- Sisyphus build

* Tue Nov 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.002003-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.002001-alt1_13
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.002001-alt1_11
- update to new release by fcimport

* Fri Jun 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.002001-alt1_10
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.002001-alt1_9
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.002001-alt1_8
- update to new release by fcimport

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 1.002001-alt1_3
- fc import

