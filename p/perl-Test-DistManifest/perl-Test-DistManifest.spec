Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Build.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# noarch, but to avoid debug* files interfering with manifest test:
%global debug_package %{nil}

Name:           perl-Test-DistManifest
Version:        1.014
Release:        alt1_15
Summary:        Author test that validates a package MANIFEST
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-DistManifest
Source0:        https://cpan.metacpan.org/modules/by-module/Test/Test-DistManifest-%{version}.tar.gz
BuildArch:      noarch
# Build:
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Spec/Unix.pm)
BuildRequires:  perl(Module/Manifest.pm)
BuildRequires:  perl(Test/Builder.pm)
# Tests only:
BuildRequires:  perl(if.pm)
BuildRequires:  perl(Test/Builder/Tester.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info
# Test::Warnings not used without $ENV{AUTHOR_TESTING}
# Dependencies:

%description
This Perl module provides a simple method of testing that a MANIFEST matches
the distribution.

%prep
%setup -q -n Test-DistManifest-%{version}

%build
PERL_MM_FALLBACK_SILENCE_WARNING=1 perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{makeinstall_std}
# %{_fixperms} -c %{buildroot}

%check
make test

%files
%doc --no-dereference LICENSE
%doc Changes CONTRIBUTING README examples/
%{perl_vendor_privlib}/Test/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 1.014-alt1_15
- update to new release by fcimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 1.014-alt1_12
- update to new release by fcimport

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.014-alt1
- automated CPAN update

* Wed Feb 11 2015 Igor Vlasenko <viy@altlinux.ru> 1.013-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1_6
- Sisyphus build

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1_3
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.012-alt1_1
- fc import

