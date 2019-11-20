Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:       perl-Text-Password-Pronounceable 
Version:    0.30
Release:    alt1_22
# lib/Text/Password/Pronounceable.pm -> GPL+ or Artistic
License:    GPL+ or Artistic 
Summary:    Generate pronounceable passwords 
Source0:    https://cpan.metacpan.org/authors/id/T/TS/TSIBLEY/Text-Password-Pronounceable-%{version}.tar.gz
Url:        https://metacpan.org/release/Text-Password-Pronounceable
BuildArch:  noarch
BuildRequires: coreutils
BuildRequires: perl-devel
BuildRequires: rpm-build-perl
BuildRequires: perl(inc/Module/Install.pm)
BuildRequires: perl(Module/Install/Metadata.pm)
BuildRequires: perl(Module/Install/WriteAll.pm)
BuildRequires: sed
# Run-time:
BuildRequires: perl(Carp.pm)
BuildRequires: perl(strict.pm)
BuildRequires: perl(warnings.pm)
# Tests:
BuildRequires: perl(Test/More.pm)
# Optional tests:
BuildRequires: perl(Test/Pod.pm)
BuildRequires: perl(Test/Pod/Coverage.pm)
Source44: import.info

%description
This module generates pronounceable passwords, based on the English
digraphs by D. Edwards.

%prep
%setup -q -n Text-Password-Pronounceable-%{version}
# Remove bundled modules
rm -r ./inc/*
sed -i -e '/^inc\//d' MANIFEST

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README 
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_22
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_18
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_16
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_15
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_13
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_12
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_10
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_1
- fc import

