Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Term-Size-Perl
Version:        0.031
Release:        alt1_6
Summary:        Perl extension for retrieving terminal size (Perl version)
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Term-Size-Perl
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Term-Size-Perl-%{version}.tar.gz
# Build
BuildRequires:  gcc
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/CBuilder.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Runtime
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(strict.pm)
# Tests only
BuildRequires:  perl(Test/More.pm)

# although the resulting rpm appears to be noarch, the build is arch-dependent
# and produces different code for ppc and x86
%global  debug_package %nil
Source44: import.info
BuildArch: noarch

%description
Yet another implementation of Term::Size. Now in pure Perl, with the
exception of a C probe run on build time.

%prep
%setup -q -n Term-Size-Perl-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc --no-dereference LICENSE
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.031-alt1_6
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.031-alt1_2
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.031-alt1_1
- update to new release by fcimport

* Mon Feb 19 2018 Igor Vlasenko <viy@altlinux.ru> 0.031-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.029-alt3_26
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.029-alt3_24
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.029-alt3_23
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.029-alt3_22
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.029-alt3_21
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.029-alt3_19
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.029-alt3_17
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.029-alt3_16
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.029-alt3_15
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.029-alt3_14
- update to new release by fcimport

* Tue Aug 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.029-alt3_13
- fc import

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.029-alt3_12
- update to new release by fcimport

* Mon Nov 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.029-alt3_11
- sisyphus release

* Mon Sep 10 2012 Cronbuild Service <cronbuild@altlinux.org> 0.029-alt2_11
- rebuild with new perl

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.029-alt1_11
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.029-alt1_9
- fc import

