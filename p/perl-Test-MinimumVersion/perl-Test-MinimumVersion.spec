# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:		perl-Test-MinimumVersion
Version:	0.101082
Release:	alt1_1
Summary:	Check whether your code requires a newer perl
License:	GPL+ or Artistic
Group:		Development/Perl
URL:		http://search.cpan.org/dist/Test-MinimumVersion/
Source0:	http://search.cpan.org/CPAN/authors/id/R/RJ/RJBS/Test-MinimumVersion-%{version}.tar.gz

BuildArch:	noarch

BuildRequires:	perl(base.pm)
BuildRequires:  perl(CPAN/Meta.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(File/Find/Rule.pm)
BuildRequires:	perl(File/Find/Rule/Perl.pm)
BuildRequires:	perl(Perl/MinimumVersion.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Tester.pm)
BuildRequires:	perl(YAML/Tiny.pm)
BuildRequires:	perl(version.pm)
BuildRequires:	perl(warnings.pm)
Source44: import.info

%description
Check whether your code requires a newer perl than you think.

%prep
%setup -q -n Test-MinimumVersion-%{version}
find -type f -exec chmod -x {} \;

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} ';'
find $RPM_BUILD_ROOT -type d -depth -exec rmdir {} 2>/dev/null ';'
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%doc LICENSE
%{perl_vendor_privlib}/Test

%changelog
* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 0.101082-alt1_1
- update to new release by fcimport

* Tue Dec 15 2015 Igor Vlasenko <viy@altlinux.ru> 0.101082-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.101081-alt1_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.101081-alt1_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.101081-alt1_2
- update to new release by fcimport

* Thu Jan 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.101081-alt1_1
- update to new release by fcimport

* Tue Dec 03 2013 Igor Vlasenko <viy@altlinux.ru> 0.101081-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.101080-alt2_12
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.101080-alt2_11
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 0.101080-alt2_10
- update to new release by fcimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.101080-alt2_9
- moved to Sisyphus

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 0.101080-alt1_9
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.101080-alt1_8
- update to new release by fcimport

* Tue May 29 2012 Igor Vlasenko <viy@altlinux.ru> 0.101080-alt1_6
- fc import

