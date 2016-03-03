%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Cwd.pm) perl(ExtUtils/MakeMaker.pm) perl(File/Spec.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-DateTime-Format-MySQL
Version:        0.06
Release:        alt1
Summary:        Parse and format MySQL dates and times
Group:          Development/Perl
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/DateTime-Format-MySQL
Source:        http://www.cpan.org/authors/id/X/XM/XMIKEW/DateTime-Format-MySQL-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  perl
BuildRequires:  perl(Module/Build.pm)
# Module Runtime
BuildRequires:  perl(DateTime.pm)
BuildRequires:  perl(DateTime/Format/Builder.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(vars.pm)
# Test Suite
BuildRequires:  perl(Test/More.pm)
# Runtime
Requires:       perl(DateTime/Format/Builder.pm)
Source44: import.info

%description
This module understands the formats used by MySQL for its DATE, DATETIME,
TIME, and TIMESTAMP data types. It can be used to parse these formats in order
to create DateTime objects, and it can take a DateTime object and produce a
string representing it in the MySQL format.

%prep
%setup -q -n DateTime-Format-MySQL-%{version}

%build
perl Build.PL --install_path bindoc=%_man1dir --installdirs=vendor
./Build

%install
./Build install --destdir=%{buildroot} --create_packlist=0
# %{_fixperms} %{buildroot}

%check
./Build test

%files
%if 0%{?_licensedir:1}
%doc LICENSE
%else
%doc LICENSE
%endif
%doc Changes README
%{perl_vendor_privlib}/DateTime/

%changelog
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

