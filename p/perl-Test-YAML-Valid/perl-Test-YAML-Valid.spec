# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Carp.pm) perl(Config.pm) perl(Cwd.pm) perl(Exporter.pm) perl(File/Basename.pm) perl(File/Find.pm) perl(File/Spec.pm) perl(File/Spec/Functions.pm) perl(FileHandle.pm) perl(FindBin.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(Socket.pm) perl(base.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Test-YAML-Valid
Version:        0.04
Release:        alt2_21
Summary:        Lets you test the validity of YAML files in unit tests
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Test-YAML-Valid/
Source0:        http://www.cpan.org/authors/id/J/JR/JROCKWAY/Test-YAML-Valid-%{version}.tar.gz
# Fix building on Perl without "." in @INC, CPAN RT#120438
Patch0:         Test-YAML-Valid-0.04-Fix-building-on-Perl-without-.-in-INC.patch
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(YAML.pm)
BuildRequires:  perl(YAML/XS.pm)
BuildRequires:  perl(YAML/Tiny.pm)
BuildRequires:  perl(YAML/Syck.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(CPAN.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(Test/Builder/Tester.pm)
Requires:       perl(YAML.pm)
Requires:       perl(YAML/Syck.pm)
Source44: import.info

%description
Lets you test the validity of YAML files inside your
(Test::Builder-based) unit tests.

%prep
%setup -q -n Test-YAML-Valid-%{version}
%patch0 -p1

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
%make_build

%install

make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT

find $RPM_BUILD_ROOT -type f -name .packlist -exec rm -f {} \;
find $RPM_BUILD_ROOT -depth -type d -exec rmdir {} 2>/dev/null \;

# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%dir %{perl_vendor_privlib}/Test/
%dir %{perl_vendor_privlib}/Test/YAML/
%{perl_vendor_privlib}/Test/YAML/Valid.pm

%changelog
* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_21
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_19
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_18
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_17
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_16
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_14
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_13
- update to new release by fcimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt2_12
- moved to Sisyphus for Slic3r (by dd@ request)

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_12
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_11
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_10
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_9
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1_7
- fc import

