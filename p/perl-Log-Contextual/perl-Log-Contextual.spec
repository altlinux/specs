%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/PerlTidy.pm) perl(Test/Pod.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Log-Contextual
Version:        0.008000
Release:        alt1
Summary:        Simple logging interface with a contextual log
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Log-Contextual/
Source0:        http://www.cpan.org/authors/id/F/FR/FREW/Log-Contextual-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(B.pm)
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Data/Dumper/Concise.pm)
BuildRequires:  perl(Exporter/Declare.pm)
BuildRequires:  perl(Exporter/Declare/Export/Generator.pm)
BuildRequires:  perl(Moo.pm)
BuildRequires:  perl(Moo/Role.pm)
BuildRequires:  perl(Scalar/Util.pm)
# Optional run-time:
BuildRequires:  perl(Log/Log4perl.pm)
# Tests:
BuildRequires:  perl(File/Temp.pm)
BuildRequires:  perl(FindBin.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Test/Fatal.pm)
BuildRequires:  perl(Test/More.pm)
# Test::PerlTidy not used
# Test::Pod 1.41 not used
Requires:       perl(Exporter/Declare.pm) >= 0.111
Requires:       perl(Moo.pm) >= 1.003.0

# Filter under-specified depenedencies


Source44: import.info
%filter_from_requires /^perl\\(Exporter.Declare.pm\\)\\s*$/d
%filter_from_requires /^perl\\(Moo.pm\\)\\s*$/d

%description
This module is a simple interface to extensible logging. It is bundled with
a really basic logger, Log::Contextual::SimpleLogger, but in general you
should use a real logger instead of that. For something more serious but
not overly complicated, try Log::Dispatchouli.

%prep
%setup -q -n Log-Contextual-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc LICENSE
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Sat Nov 25 2017 Igor Vlasenko <viy@altlinux.ru> 0.008000-alt1
- automated CPAN update

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.007001-alt1_3
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.007001-alt1_2
- update to new release by fcimport

* Wed Aug 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.007001-alt1
- automated CPAN update

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.007000-alt1_2
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.007000-alt1_1
- update to new release by fcimport

* Wed Oct 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.007000-alt1
- automated CPAN update

* Mon Sep 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.006005-alt2_5
- to Sisyphus

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.006005-alt1_5
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.006005-alt1_4
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.006005-alt1_3
- update to new release by fcimport

* Wed Apr 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.006005-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.006004-alt1_2
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.006004-alt1_1
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.006003-alt1_2
- update to new release by fcimport

* Tue Mar 04 2014 Igor Vlasenko <viy@altlinux.ru> 0.006003-alt1_1
- update to new release by fcimport

* Thu Sep 19 2013 Igor Vlasenko <viy@altlinux.ru> 0.006000-alt1_1
- update to new release by fcimport

* Wed May 01 2013 Igor Vlasenko <viy@altlinux.ru> 0.005003-alt1_1
- initial fc import

