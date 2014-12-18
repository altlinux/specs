# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Build/Tiny.pm) perl(Pod/Coverage/TrustPod.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-experimental
Version:        0.013
Release:        alt1_2
Summary:        Experimental features made easy
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/experimental/
Source0:        http://www.cpan.org/authors/id/L/LE/LEONT/experimental-%{version}.tar.gz
# Replace Build.PL to not require Module::Build::Tiny because experimental is
# a core dual-lived module and Module::Build::Tiny is not.
Source1:        Makefile.PL
BuildArch:      noarch
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(feature.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(version.pm)
BuildRequires:  perl(warnings.pm)
# Tests:
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(IO/Handle.pm)
BuildRequires:  perl(IPC/Open3.pm)
BuildRequires:  perl(Test/More.pm)
Source44: import.info

%description
This pragma provides an easy and convenient way to enable or disable
experimental features.

%prep
%setup -q -n experimental-%{version}
cp %{SOURCE1} .

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
%doc Changes LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1_2
- update to new release by fcimport

* Tue Dec 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.013-alt1
- automated CPAN update

* Tue Jul 08 2014 Igor Vlasenko <viy@altlinux.ru> 0.008-alt1
- automated CPAN update

* Mon Jun 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_2
- perl dependency for Language-Expr

* Tue Apr 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.007-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_3
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_2
- update to new release by fcimport

* Fri Aug 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1_1
- fc import

