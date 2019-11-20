Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Convert-NLS_DATE_FORMAT
Version:        0.06
Release:        alt1_21
Summary:        Convert Oracle NLS_DATE_FORMAT <-> strftime Format Strings
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Convert-NLS_DATE_FORMAT
Source0:        https://cpan.metacpan.org/authors/id/K/KO/KOLIBRIE/Convert-NLS_DATE_FORMAT-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(Module/Build/Tiny.pm)
BuildRequires:  perl(strict.pm)
# Runtime
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(warnings.pm)
# Tests only
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
Convert Oracle's NLS_DATE_FORMAT string into a strptime format string, or
the reverse.

%prep
%setup -q -n Convert-NLS_DATE_FORMAT-%{version}

%build
perl Build.PL --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc --no-dereference LICENSE
%doc Changes README.md
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_21
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_17
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_15
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_14
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_13
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_12
- update to new release by fcimport

* Tue Feb 16 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_10
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_4
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_3
- moved to Sisyphus (Tapper dep)

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_1
- fc import

