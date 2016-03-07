Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/Run/CmdLine/Iface.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-String-Random
Version:        0.29
Release:        alt1_3
Summary:        Perl module to generate random strings based on a pattern
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/String-Random/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SH/SHLOMIF/String-Random-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(parent.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(warnings.pm)


Source44: import.info

%description
This module makes it trivial to generate random strings.


%prep
%setup -q -n String-Random-%{version}


%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build


%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*


%check
./Build test


%files
%doc Changes README TODO
%{perl_vendor_privlib}/*


%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1_3
- update to new release by fcimport

* Mon Dec 28 2015 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1_3
- update to new release by fcimport

* Tue Apr 07 2015 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1_1
- update to new release by fcimport

* Mon Jan 26 2015 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_2
- update to new release by fcimport

* Tue Feb 25 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1_1
- update to new release by fcimport

* Wed Feb 05 2014 Igor Vlasenko <viy@altlinux.ru> 0.26-alt1
- automated CPAN update

* Thu Jan 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_1
- update to new release by fcimport

* Fri Jan 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Thu Dec 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Tue Dec 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt2_17
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_17
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_16
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_15
- update to new release by fcimport

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_14
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_13
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1_11
- fc import

