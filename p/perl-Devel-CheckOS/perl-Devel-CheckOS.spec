%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Devel-CheckOS
Version:        1.81
Release:        alt1
Summary:        Check what OS we're running on
License:        GPLv2 or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Devel-CheckOS/
Source0:        http://www.cpan.org/authors/id/D/DC/DCANTRELL/Devel-CheckOS-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(strict.pm)
# Run-time:
BuildRequires:  perl(Data/Compare.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(File/Find/Rule.pm)
BuildRequires:  perl(vars.pm)
# Tests:
BuildRequires:  perl(Cwd.pm)
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(Test/More.pm)
# Optional tests:
BuildRequires:  perl(Test/Pod.pm)
Requires:       perl(Data/Compare.pm) >= 1.21
Requires:       perl(File/Find/Rule.pm) >= 0.28

# Remove unversioned requires


Source44: import.info
%filter_from_requires /^perl\\(Data.Compare.pm\\)$/d
%filter_from_requires /^perl\\(File.Find.Rule.pm\\)$/d

%description
Devel::CheckOS provides a more friendly interface to $^O, and also lets you
check for various OS families such as Unix, which includes things like Linux,
*BSD, AIX, HPUX, Solaris etc.

%prep
%setup -q -n Devel-CheckOS-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ARTISTIC.txt CHANGELOG GPL2.txt README TODO
%{_bindir}/use-devel-assertos
%{perl_vendor_privlib}/*
%{_mandir}/man1/use-devel-assertos.1*

%changelog
* Thu Feb 01 2018 Igor Vlasenko <viy@altlinux.ru> 1.81-alt1
- automated CPAN update

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 1.80-alt1
- automated CPAN update

* Mon Oct 31 2016 Igor Vlasenko <viy@altlinux.ru> 1.79-alt1
- automated CPAN update

* Wed Apr 01 2015 Igor Vlasenko <viy@altlinux.ru> 1.76-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.73-alt1_2
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.73-alt1_1
- update to new release by fcimport

* Mon Aug 04 2014 Igor Vlasenko <viy@altlinux.ru> 1.73-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1_2
- update to new release by fcimport

* Tue Jun 03 2014 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1_1
- update to new release by fcimport

* Tue Apr 22 2014 Igor Vlasenko <viy@altlinux.ru> 1.72-alt1
- automated CPAN update

* Wed Oct 23 2013 Igor Vlasenko <viy@altlinux.ru> 1.71-alt2_3
- Sisyphus build

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1_3
- update to new release by fcimport

* Mon Feb 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.71-alt1_1
- update to new release by fcimport

* Thu Oct 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.64-alt1_7
- new fc release

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.64-alt1_5
- fc import

