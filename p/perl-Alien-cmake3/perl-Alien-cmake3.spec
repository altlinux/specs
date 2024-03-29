%define _unpackaged_files_terminate_build 1
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Alien-cmake3
Version:        0.08
Release:        alt1
Summary:        Find or download or build cmake 3 or better
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Alien-cmake3
Source0:        http://www.cpan.org/authors/id/P/PL/PLICEASE/Alien-cmake3-%{version}.tar.gz
# This is an Alien::Build plugin, it stores data about architecture specific
# files, therefore this an architecture specific package, yet there is no XS
# code, so debuginfo generation and dependency on perl-devel is disabled.
%global debug_package %{nil}
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl
BuildRequires:  perl(Alien/Build/MM.pm)
BuildRequires:  perl(alienfile.pm)
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(Config.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Which.pm)
BuildRequires:  perl(Path/Tiny.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  ctest cmake
BuildRequires:  perl(Alien/Base.pm)
BuildRequires:  perl(base.pm)
# Tests:
BuildRequires:  perl(Test2/V0.pm)
BuildRequires:  perl(Test/Alien.pm)
Requires:       ctest cmake
Requires:       perl(Alien/Base.pm) >= 0.920

# Remove under-specified dependencies

Source44: import.info
%filter_from_requires /^perl(Alien.Base.pm)/d

%description
This Perl Alien distribution provides an external dependency on the build tool
cmake version 3.0.0 or better.

%prep
%setup -q -n Alien-cmake3-%{version}

%build
unset ALIEN_CMAKE_FROM_SOURCE
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1 NO_PERLLOCAL=1
%{make_build}

%install
%{makeinstall_std}
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README author.yml
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Alien*

%changelog
* Sun Jul 18 2021 Igor Vlasenko <viy@altlinux.org> 0.08-alt1
- automated CPAN update

* Thu Jun 10 2021 Igor Vlasenko <viy@altlinux.org> 0.06-alt1
- automated CPAN update

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_1
- update to new release by fcimport

* Tue Nov 19 2019 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_3
- update to new release by fcimport

* Thu Dec 28 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_1
- new version

