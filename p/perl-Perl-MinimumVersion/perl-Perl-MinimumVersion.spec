%define perl_bootstrap 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Fcntl.pm) perl(File/Spec/Functions.pm) perl-base perl-devel perl-podlators perl-File-Find-Rule-Perl
# END SourceDeps(oneline)
Name:           perl-Perl-MinimumVersion
Version:        1.28
Release:        alt2_8
Summary:        Find a minimum required version of perl for Perl code
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/Perl-MinimumVersion/
Source0:        http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/Perl-MinimumVersion-%{version}.tar.gz

BuildArch:      noarch

BuildRequires: perl(Cwd.pm)
BuildRequires: perl(File/Find.pm)
BuildRequires: perl(File/Path.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
# Run-time and tests:
BuildRequires: perl(List/Util.pm)
BuildRequires: perl(Params/Util.pm)
BuildRequires: perl(Perl/Critic/Utils.pm)
BuildRequires: perl(PPI.pm)
BuildRequires: perl(version.pm)
%if !%{defined perl_bootstrap}
BuildRequires: perl(Carp.pm)
BuildRequires: perl(Exporter.pm)
BuildRequires: perl(File/Find/Rule.pm)
BuildRequires: perl(File/Find/Rule/Perl.pm)
BuildRequires: perl(File/Spec.pm)
BuildRequires: perl(Getopt/Long.pm)
BuildRequires: perl(PPI/Util.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(Test/Script.pm)
%endif
Source44: import.info

%description
Find a minimum required version of perl for Perl code

%prep
%setup -q -n Perl-MinimumVersion-%{version}

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%if !%{defined perl_bootstrap}
make test
%endif

%files
%doc Changes LICENSE
%{_bindir}/*
%{perl_vendor_privlib}/Perl
%{_mandir}/man1/*

%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.28-alt2_8
- moved to Sisyphus (bootstrap)

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1_8
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1_7
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.28-alt1_4
- fc import

