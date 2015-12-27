# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Scalar/Util.pm) perl-Module-Build perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-MockModule
Version:        0.11
Release:        alt1_1
Summary:        Override subroutines in a module for unit testing
Group:          Development/Perl
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Test-MockModule/
Source0:        http://search.cpan.org/CPAN/authors/id/S/SI/SIMONFLK/Test-MockModule-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(CGI.pm)
BuildRequires:  perl(Test/More.pm), perl(Test/Pod.pm), perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Module/Build.pm), perl(SUPER.pm)
Source44: import.info

%description
%{summary}.

%prep
%setup -q -n Test-MockModule-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor
./Build

%install
./Build install destdir=$RPM_BUILD_ROOT create_packlist=0
chmod -R u+w $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README.md
%doc LICENSE
%{perl_vendor_privlib}/Test

%changelog
* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Thu Oct 29 2015 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_3
- new version

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_22
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_21
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_20
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_19
- update to new release by fcimport

* Sun Feb 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_18
- update to new release by fcimport

* Sat Oct 27 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_17
- picked up by robot, thanks to enp@

* Fri Oct 26 2012 Eugene Prokopiev <enp@altlinux.ru> 0.05-alt1
- initial build for ALT Linux Sisyphus

