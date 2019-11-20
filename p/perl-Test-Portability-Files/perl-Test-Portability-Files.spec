Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Pod/Coverage/TrustPod.pm) perl(Test/CPAN/Changes.pm) perl(Test/CPAN/Meta.pm) perl(Test/CPAN/Meta/JSON.pm) perl(Test/EOL.pm) perl(Test/Kwalitee.pm) perl(Test/MinimumVersion.pm) perl(Test/Mojibake.pm) perl(Test/NoTabs.pm) perl(Test/Perl/Critic.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl(Test/Synopsis.pm) perl(Test/Version.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Test-Portability-Files
Version:        0.10
Release:        alt1_4
Summary:        Check file names portability
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Test-Portability-Files
Source0:        https://cpan.metacpan.org/authors/id/A/AB/ABRAXXA/Test-Portability-Files-%{version}.tar.gz
BuildArch:      noarch
# Build
BuildRequires:  rpm-build-perl
BuildRequires:  perl-devel
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Runtime
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/Manifest.pm)
BuildRequires:  perl(File/Basename.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(IPC/Open3.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(utf8.pm)
Source44: import.info
# Dependencies

%description
This module is used to check the portability across operating systems of
the names of the files present in the distribution of a module. The tests
use the advice given in "Files and Filesystems" in perlport. The author of
a distribution can select which tests to execute.

%prep
%setup -q -n Test-Portability-Files-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} -c %{buildroot}

%check
make test

%files
%doc --no-dereference LICENSE
%doc Changes README
%{perl_vendor_privlib}/Test/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_4
- update to new release by fcimport

* Sat Feb 09 2019 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_1
- update to new release by fcimport

* Mon Jan 21 2019 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_3
- update to new release by fcimport

* Mon May 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_2
- update to new release by fcimport

* Mon Jan 01 2018 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_4
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_1
- update to new release by fcimport

* Sun Sep 25 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- automated CPAN update

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_7
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_6
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_2
- update to new release by fcimport

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1_1
- update to new release by fcimport

* Tue Sep 24 2013 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- automated CPAN update

* Tue Sep 17 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt2_20
- Sisyphus build; switch to fc import

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_20
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_19
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_18
- update to new release by fcimport

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_17
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_16
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1_14
- fc import

