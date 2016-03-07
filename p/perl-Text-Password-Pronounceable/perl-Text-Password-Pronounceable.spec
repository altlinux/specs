# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl(inc/Module/Install.pm) perl-devel perl-podlators
# END SourceDeps(oneline)
Name:       perl-Text-Password-Pronounceable 
Version:    0.30
Release:    alt1_11
# lib/Text/Password/Pronounceable.pm -> GPL+ or Artistic
License:    GPL+ or Artistic 
Group:      Development/Perl
Summary:    Generate pronounceable passwords 
Source0:    http://search.cpan.org/CPAN/authors/id/T/TS/TSIBLEY/Text-Password-Pronounceable-%{version}.tar.gz
Url:        http://search.cpan.org/dist/Text-Password-Pronounceable
BuildArch:  noarch
BuildRequires: perl(Carp.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Test/More.pm)
Source44: import.info

%description
This module generates pronuceable passwords, based on the English
digraphs by D. Edwards.

%prep
%setup -q -n Text-Password-Pronounceable-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CHANGES README 
%{perl_vendor_privlib}/*

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_11
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_10
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_7
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_1
- fc import

