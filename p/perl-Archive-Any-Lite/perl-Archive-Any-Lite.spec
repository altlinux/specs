Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(ExtUtils/MakeMaker/CPANfile.pm) perl-podlators
# END SourceDeps(oneline)
# fedora bcond_with macro
%define bcond_with() %{expand:%%{?_with_%{1}:%%global with_%{1} 1}}
%define bcond_without() %{expand:%%{!?_without_%{1}:%%global with_%{1} 1}}
# redefine altlinux specific with and without
%define with()         %{expand:%%{?with_%{1}:1}%%{!?with_%{1}:0}}
%define without()      %{expand:%%{?with_%{1}:0}%%{!?with_%{1}:1}}
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
# Run extra test
%if ! (0%{?rhel})
%bcond_without perl_Archive_Any_Lite_enables_extra_test
%else
%bcond_with perl_Archive_Any_Lite_enables_extra_test
%endif

Name:		perl-Archive-Any-Lite
Version:	0.11
Release:	alt1_12
Summary:	Simple CPAN package extractor 
License:	GPL+ or Artistic
URL:		https://metacpan.org/release/Archive-Any-Lite
Source0:	https://cpan.metacpan.org/modules/by-module/Archive/Archive-Any-Lite-%{version}.tar.gz
Patch0:		Archive-Any-Lite-0.08-EU:MM.patch
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	rpm-build-perl
BuildRequires:	perl-devel
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module
BuildRequires:	perl(Archive/Tar.pm)
BuildRequires:	perl(Archive/Zip.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(IO/Uncompress/Bunzip2.pm)
BuildRequires:	perl(IO/Zlib.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(warnings.pm)
# Test Suite
BuildRequires:	perl(File/Path.pm)
BuildRequires:	perl(File/Spec/Functions.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(FindBin.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/UseAllModules.pm)
# Optional Tests
%if %{with perl_Archive_Any_Lite_enables_extra_test}
BuildRequires:	perl(Parallel/ForkManager.pm)
%endif
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
# Runtime
Requires:	perl(IO/Uncompress/Bunzip2.pm)
Requires:	perl(IO/Zlib.pm)
Source44: import.info

%description
This is a fork of Archive::Any by Michael Schwern and Clint Moore. The main
difference is that this works properly even when you fork(), and may require
less memory to extract a tarball. On the other hand, this isn't pluggable
(it only supports file formats used in the CPAN toolchains), and it doesn't
check MIME types.

%prep
%setup -q -n Archive-Any-Lite-%{version}

# Build with ExtUtils::MakeMaker rather than ExtUtils::MakeMaker::CPANfile
%patch0

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
# %{_fixperms} -c %{buildroot}

%check
make test TEST_POD=1

%files
%doc --no-dereference LICENSE
%doc Changes README
%{perl_vendor_privlib}/Archive/

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_12
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_7
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_5
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_4
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_3
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_2
- update to new release by fcimport

* Sun May 08 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_1
- update to new release by fcimport

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_4
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1_2
- update to new release by fcimport

* Tue Aug 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_2
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_1
- update to new release by fcimport

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1_2
- Sisyphus build

* Mon Sep 09 2013 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- initial import by package builder

