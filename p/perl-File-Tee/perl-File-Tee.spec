Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-File-Tee
Version:        0.07
Release:        alt3
Summary:        Replicate data sent to a Perl stream
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/File-Tee
Source0:        https://cpan.metacpan.org/modules/by-module/File/File-Tee-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
This module is able to replicate data written to a Perl stream into another
streams. It is the Perl equivalent of the shell utility tee(1).

%prep
%setup -q -n File-Tee-%{version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon May 23 2022 Andrew A. Vasilyev <andy@altlinux.org> 0.07-alt3
- initial build for ALT Sisyphus (from autoimports)

* Sat Feb 05 2022 Igor Vlasenko <viy@altlinux.org> 0.07-alt2_26
- update to new release by fcimport

* Mon Aug 02 2021 Igor Vlasenko <viy@altlinux.org> 0.07-alt2_25
- update to new release by fcimport

* Thu Jul 08 2021 Igor Vlasenko <viy@altlinux.org> 0.07-alt2_24
- update to new release by fcimport

* Wed Mar 17 2021 Igor Vlasenko <viy@altlinux.org> 0.07-alt2_23
- update to new release by fcimport

* Wed Jan 27 2021 Igor Vlasenko <viy@altlinux.ru> 0.07-alt2_22
- update to new release by fcimport

* Wed Sep 02 2020 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_22
- update to new release by fcimport

* Mon Jul 06 2020 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_21
- update to new release by fcimport

* Thu Mar 05 2020 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_20
- update to new release by fcimport

* Tue Aug 06 2019 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_19
- update to new release by fcimport

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_18
- update to new release by fcimport

* Fri Mar 01 2019 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_17
- update to new release by fcimport

* Wed Aug 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_16
- update to new release by fcimport

* Sun Jul 15 2018 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_15
- update to new release by fcimport

* Tue Feb 20 2018 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_14
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_12
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_11
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_10
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_9
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_8
- update to new release by fcimport

* Mon Oct 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_6
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_5
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_3
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_2
- initial fc import

