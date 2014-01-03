%define _unpackaged_files_terminate_build 1
Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-String-Random
Version:        0.25
Release:        alt1
Summary:        Perl module to generate random strings based on a pattern
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/String-Random/
Source:        http://www.cpan.org/authors/id/S/SH/SHLOMIF/String-Random-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Test/More.pm)


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

