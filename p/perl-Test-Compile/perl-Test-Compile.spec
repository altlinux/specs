%define _unpackaged_files_terminate_build 1
%define sname test-compile

Name: perl-Test-Compile
Version: 3.2.0
Release: alt1
Summary: Check whether Perl module files compile correctly
License: GPL+ or Artistic
Group: Development/Perl
Url: http://search.cpan.org/dist/Test-Compile/
Source0: http://www.cpan.org/authors/id/E/EG/EGILES/Test-Compile-v%{version}.tar.gz
BuildArch: noarch

BuildRequires: coreutils
BuildRequires: findutils
BuildRequires: make
BuildRequires: perl-devel
BuildRequires: perl-Package-Generator
BuildRequires: perl(ExtUtils/MakeMaker.pm)
# Run-time
# Devel::CheckOS is needed only on VMS. See Changes.
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(Test/Builder.pm)
BuildRequires: perl(UNIVERSAL/require.pm)
BuildRequires: perl(version.pm)
BuildRequires: perl(warnings.pm)
BuildRequires: perl(Test/Warnings.pm)
BuildRequires: perl-Module-Build
BuildRequires: perl-Devel-CheckOS
# Tests
# Test::More version is described in Changes
BuildRequires: perl(Test/More.pm)

%description
Test::Compile lets you check the validity of a Perl module file or Perl script
file, and report its results in standard Test::Simple fashion.

%prep
%setup -q -n Test-Compile-v%{version}

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendorlib/*

%changelog
* Mon Apr 03 2023 Igor Vlasenko <viy@altlinux.org> 3.2.0-alt1
- automated CPAN update

* Thu Jun 02 2022 Igor Vlasenko <viy@altlinux.org> 3.1.0-alt1
- automated CPAN update

* Wed Sep 01 2021 Igor Vlasenko <viy@altlinux.org> 3.0.1-alt1
- automated CPAN update

* Thu Jun 17 2021 Igor Vlasenko <viy@altlinux.org> 2.4.2-alt1
- automated CPAN update

* Thu Jul 23 2020 Igor Vlasenko <viy@altlinux.ru> 2.4.1-alt1
- automated CPAN update

* Tue Mar 31 2020 Igor Vlasenko <viy@altlinux.ru> 2.4.0-alt1
- automated CPAN update

* Mon Oct 28 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.1-alt1
- automated CPAN update

* Sun Oct 13 2019 Igor Vlasenko <viy@altlinux.ru> 2.3.0-alt1
- automated CPAN update

* Wed Jul 17 2019 Igor Vlasenko <viy@altlinux.ru> 2.2.2-alt1
- automated CPAN update

* Sun Jul 07 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.2-alt1
- automated CPAN update

* Fri Jun 28 2019 Igor Vlasenko <viy@altlinux.ru> 2.1.0-alt1
- automated CPAN update

* Sun Jun 23 2019 Igor Vlasenko <viy@altlinux.ru> 2.0.0-alt1
- automated CPAN update

* Tue Jun 19 2018 Alexandr Antonov <aas@altlinux.org> 1.3.0-alt1
- initial build for ALT
