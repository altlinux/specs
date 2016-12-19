Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-Module-Build perl-podlators
# END SourceDeps(oneline)
Name:           perl-Convert-NLS_DATE_FORMAT
Version:        0.06
Release:        alt1_12
Summary:        Convert Oracle NLS_DATE_FORMAT <-> strftime Format Strings
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Convert-NLS_DATE_FORMAT/
Source0:        http://www.cpan.org/authors/id/K/KO/KOLIBRIE/Convert-NLS_DATE_FORMAT-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  perl
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
perl Build.PL --install_path bindoc=%_man1dir --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc LICENSE
%doc Changes README.md
%{perl_vendor_privlib}/*

%changelog
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

