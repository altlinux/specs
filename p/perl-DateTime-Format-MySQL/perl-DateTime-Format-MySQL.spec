%define _unpackaged_files_terminate_build 1
Epoch: 1
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(DateTime/Locale.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-DateTime-Format-MySQL
Version:        0.08
Release:        alt2.1
Summary:        Parse and format MySQL dates and times
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/DateTime-Format-MySQL
Source0:        http://www.cpan.org/authors/id/X/XM/XMIKEW/DateTime-Format-MySQL-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  coreutils
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(Module/Build.pm)
# Runtime
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Format/Builder.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
# Tests only
BuildRequires:  perl(Test/More.pm)
Source44: import.info
# Dependencies

%description
This module understands the formats used by MySQL for its DATE, DATETIME,
TIME, and TIMESTAMP data types. It can be used to parse these formats in order
to create DateTime objects, and it can take a DateTime object and produce a
string representing it in the MySQL format.

%prep
%setup -q -n DateTime-Format-MySQL-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# %{_fixperms} -c %{buildroot}

%check
./Build test

%files
%doc Changes README
%{perl_vendor_privlib}/DateTime/

%changelog
* Sat Aug 05 2023 Igor Vlasenko <viy@altlinux.org> 1:0.08-alt2.1
- automated CPAN update

* Tue Jun 08 2021 Igor Vlasenko <viy@altlinux.org> 0.0701-alt2
- fixed build

* Thu May 27 2021 Igor Vlasenko <viy@altlinux.org> 0.0701-alt1
- automated CPAN update

* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_12
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_7
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_5
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_3
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_2
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_1
- update to new release by fcimport

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_3
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_1
- update to new release by fcimport

* Thu Nov 13 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_22
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_21
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_20
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_19
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_18
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_17
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_17
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_15
- fc import

