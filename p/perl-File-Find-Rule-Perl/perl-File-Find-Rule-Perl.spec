# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(Config.pm) perl(Fcntl.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-File-Find-Rule-Perl
Version:        1.13
Release:        alt3_1
Summary:        Common rules for searching for Perl things
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/File-Find-Rule-Perl/
Source0:        http://search.cpan.org/CPAN/authors/id/A/AD/ADAMK/File-Find-Rule-Perl-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl(constant.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Find/Rule.pm)
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(File/Spec/Functions.pm)
BuildRequires:  perl(File/Spec/Unix.pm)
BuildRequires:  perl(Params/Util.pm)
BuildRequires:  perl(Parse/CPAN/Meta.pm)
BuildRequires:  perl(Test/More.pm)
# For improved tests
%if !%{defined perl_bootstrap}
BuildRequires:  perl(Perl/MinimumVersion.pm)
BuildRequires:  perl(Test/MinimumVersion.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/CPAN/Meta.pm)
%endif
Source44: import.info

%description
Common rules for searching for Perl things.

%prep
%setup -q -T -c
%setup -q -T -D -a0

%build
cd File-Find-Rule-Perl-%{version}
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}
cd ..

%install
cd File-Find-Rule-Perl-%{version}
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
cd ..
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
%if !%{defined perl_bootstrap}
cd File-Find-Rule-Perl-%{version}
make test AUTOMATED_TESTING=1
cd ..
%endif

%files
%doc File-Find-Rule-Perl-%{version}/Changes File-Find-Rule-Perl-%{version}/LICENSE
%{perl_vendor_privlib}/File

%changelog
* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_1
- no bootstrap

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.13-alt2_1
- moved to Sisyphus (bootstrap)

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.13-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1_5
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.12-alt1_2
- fc import

