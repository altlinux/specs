# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Pod/Simple/HTML.pm) perl(Smart/Comments.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-Pod-MinimumVersion
Version:        50
Release:        alt3_16
Summary:        Perl version for POD directives used
License:        GPLv3+
Group:          Development/Other
URL:            http://search.cpan.org/dist/Pod-MinimumVersion/
Source0:        http://www.cpan.org/authors/id/K/KR/KRYDE/Pod-MinimumVersion-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  coreutils
BuildRequires:  findutils
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(strict.pm)
# inc/my_pod2html not executed
# Run-time:
# Getopt::Long not used at tests
BuildRequires:  perl(IO/String.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(overload.pm)
BuildRequires:  perl(Pod/Parser.pm)
BuildRequires:  perl(vars.pm)
BuildRequires:  perl(version.pm)
# Tests:
BuildRequires:  perl(Data/Dumper.pm)
# Devel::FindRef not used
# Devel::StackTrace not used
BuildRequires:  perl(Exporter.pm)
# Scalar::Util not used
BuildRequires:  perl(Test.pm)
Requires:       perl(IO/String.pm) >= 1.02
# This module has been divided from perl-Perl-Critic-Pulp
Conflicts:      perl-Perl-Critic-Pulp < 49
Source44: import.info

%description
Pod::MinimumVersion parses the POD in a Perl script, module, or document,
and reports what version of Perl is required to process the directives in
it with pod2man etc.

%prep
%setup -q -n Pod-MinimumVersion-%{version}

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
%doc COPYING
%doc Changes
%{perl_vendor_privlib}/*
%{_bindir}/*
%{_mandir}/man1/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 50-alt3_16
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 50-alt3_15
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 50-alt3_13
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 50-alt3_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 50-alt3_10
- update to new release by fcimport

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 50-alt3_9
- Sisyphus build

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 50-alt2_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 50-alt2_8
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 50-alt2_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 50-alt2_6
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 50-alt2_4
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 50-alt1_4
- fc import

