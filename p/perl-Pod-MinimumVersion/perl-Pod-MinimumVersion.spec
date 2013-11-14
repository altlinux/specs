# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Exporter.pm) perl(FindBin.pm) perl(Pod/Simple/HTML.pm) perl(Scalar/Util.pm) perl(Smart/Comments.pm) perl(base.pm) perl(overload.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-Pod-MinimumVersion
Version:        50
Release:        alt3_9
Summary:        Perl version for POD directives used
License:        GPLv3+
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Pod-MinimumVersion/
Source0:        http://www.cpan.org/authors/id/K/KR/KRYDE/Pod-MinimumVersion-%{version}.tar.gz
BuildArch:      noarch
# See Makefile.PL for dependencies; META.yml is out-dated.
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(IO/String.pm)
BuildRequires:  perl(List/Util.pm)
BuildRequires:  perl(Pod/Parser.pm)
BuildRequires:  perl(version.pm)
# Tests only
BuildRequires:  perl(Data/Dumper.pm)
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
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes COPYING
%{perl_vendor_privlib}/*
%{_bindir}/*
%{_mandir}/man1/*

%changelog
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

