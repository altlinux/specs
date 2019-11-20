Group: Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Test-FailWarnings
Version:        0.008
Release:        alt1_17
Summary:        Add test failures if warnings are caught
License:        ASL 2.0 

URL:            https://metacpan.org/release/Test-FailWarnings
Source0:        https://cpan.metacpan.org/authors/id/D/DA/DAGOLDEN/Test-FailWarnings-%{version}.tar.gz

BuildArch:      noarch
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Test/More.pm)
# Tests:
BuildRequires:  perl(Capture/Tiny.pm)
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(IPC/Open3.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(List/Util.pm)


Source44: import.info

%description
This module hooks $SIG{__WARN__} and converts warnings to Test::More's
fail() calls. It is designed to be used with done_testing, when you don't
need to know the test count in advance.

%prep
%setup -q -n Test-FailWarnings-%{version}

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
%doc Changes CONTRIBUTING LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_17
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_13
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_11
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_10
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_9
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_8
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_6
- update to new release by fcimport

* Tue Jan 13 2015 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_4
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_2
- update to new release by fcimport

* Tue Oct 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1_1
- update to new release by fcimport

* Fri Sep 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- automated CPAN update

* Fri Sep 06 2013 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_1
- Sisyphus build

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_2
- update to new release by fcimport

* Fri Aug 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_1
- fc import

