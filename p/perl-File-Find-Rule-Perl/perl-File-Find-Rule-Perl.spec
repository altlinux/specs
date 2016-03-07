# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-devel perl-podlators
# END SourceDeps(oneline)
Name:           perl-File-Find-Rule-Perl
Version:        1.15
Release:        alt1_5
Summary:        Common rules for searching for Perl things
License:        GPL+ or Artistic
Group:          Development/Perl
URL:            http://search.cpan.org/dist/File-Find-Rule-Perl/
Source0:        http://search.cpan.org/CPAN/authors/id/E/ET/ETHER/File-Find-Rule-Perl-%{version}.tar.gz
# Filter out the files rpm generates in sourcedir.
Patch0:         File-Find-Rule-Perl-1.15-fedora.patch
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
Source44: import.info

%description
Common rules for searching for Perl things.

%prep
%setup -q -n File-Find-Rule-Perl-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PACKLIST=1
make %{?_smp_mflags}

%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
chmod -R u+w $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes
%{perl_vendor_privlib}/File

%changelog
* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1_3
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_8
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_6
- update to new release by fcimport

* Tue Aug 20 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_5
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_3
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.13-alt3_2
- update to new release by fcimport

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

