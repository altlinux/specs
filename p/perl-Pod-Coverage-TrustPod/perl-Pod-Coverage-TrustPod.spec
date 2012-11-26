# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Pod-Coverage-TrustPod
Version:        0.100002
Release:        alt2_4
Summary:        Allow a module's pod to contain Pod::Coverage hints
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Pod-Coverage-TrustPod/
Source0:        http://www.cpan.org/authors/id/R/RJ/RJBS/Pod-Coverage-TrustPod-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Pod/Coverage/CountParents.pm)
BuildRequires:  perl(Pod/Eventual/Simple.pm)
BuildRequires:  perl(Pod/Find.pm)
# Tests:
BuildRequires:  perl(Carp/Heavy.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/More.pm)
# Optional tests:
BuildRequires:  perl(Test/Pod.pm)


Source44: import.info

%description
This is a Pod::Coverage subclass (actually, a subclass of
Pod::Coverage::CountParents) that allows the POD itself to declare certain
symbol names trusted.

%prep
%setup -q -n Pod-Coverage-TrustPod-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;


%check
RELEASE_TESTING=1 make test

%files
%doc Changes LICENSE README
%{perl_vendor_privlib}/*

%changelog
* Mon Nov 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.100002-alt2_4
- sisyphus release

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.100002-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.100002-alt1_3
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.100002-alt1_1
- fc import

