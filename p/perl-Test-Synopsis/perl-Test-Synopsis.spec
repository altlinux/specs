# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# noarch, but to avoid debug* files interfering with manifest test:
%global debug_package %{nil}

Name:		perl-Test-Synopsis
Version:	0.15
Release:	alt1_3
Summary:	Test your SYNOPSIS code
Group:		Development/Other
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/Test-Synopsis/
Source0:	http://search.cpan.org/CPAN/authors/id/Z/ZO/ZOFFIX/Test-Synopsis-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module Runtime
BuildRequires:	perl(ExtUtils/Manifest.pm)
BuildRequires:	perl(parent.pm)
BuildRequires:	perl(Pod/Simple.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Test/Builder/Module.pm)
BuildRequires:	perl(warnings.pm)
# Test Suite
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(IO/Handle.pm)
BuildRequires:	perl(IPC/Open3.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(Test/Builder/Tester.pm)
BuildRequires:	perl(Test/More.pm)
# Extra Tests; can't run these when bootstrapping or in EL since many
# of these packages won't be available
%if 0%{!?perl_bootstrap:1} && 0%{!?rhel:1}
BuildRequires:	perl(Pod/Coverage/TrustPod.pm)
BuildRequires:	perl(Pod/Wordlist.pm)
BuildRequires:	perl(Test/CPAN/Changes.pm)
BuildRequires:	perl(Test/CPAN/Meta.pm)
BuildRequires:	perl(Test/CPAN/Meta/JSON.pm)
BuildRequires:	perl(Test/DistManifest.pm)
BuildRequires:	perl(Test/EOL.pm)
BuildRequires:	perl(Test/Kwalitee.pm)
BuildRequires:	perl(Test/MinimumVersion.pm)
BuildRequires:	perl(Test/Mojibake.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/NoTabs.pm)
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
BuildRequires:	perl(Test/Portability/Files.pm)
BuildRequires:	perl(Test/Spelling.pm), hunspell-en
BuildRequires:	perl(Test/Version.pm)
%endif
# Runtime
Requires:	perl(Test/Builder/Module.pm)
Source44: import.info

%description
Test::Synopsis is an (author) test module to find .pm or .pod files under your
lib directory and then make sure the example snippet code in your SYNOPSIS
section passes the perl compile check.

Note that this module only checks the perl syntax (by wrapping the code with
sub) and doesn't actually run the code.

%prep
%setup -q -n Test-Synopsis-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%check
make test
%if 0%{!?perl_bootstrap:1} && 0%{!?rhel:1}
make test TEST_FILES="$(echo $(find xt/ -name '*.t'))"
%endif

%files
%if 0%{?_licensedir:1}
%doc LICENSE
%else
%doc LICENSE
%endif
%doc Changes README README.md
%{perl_vendor_privlib}/Test/

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_3
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_1
- update to new release by fcimport

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1
- automated CPAN update

* Wed Feb 10 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1
- automated CPAN update

* Mon Dec 28 2015 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_4
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1
- update to new release by fcimport

* Sat Feb 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt3_19
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_19
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_17
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_16
- update to new release by fcimport

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_15
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_14
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt2_9
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_9
- fc import

