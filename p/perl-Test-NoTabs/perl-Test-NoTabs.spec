# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl-podlators
# END SourceDeps(oneline)
Name:		perl-Test-NoTabs
Version:	1.4
Release:	alt1_5
Summary:	Check the presence of tabs in your project
Group:		Development/Other
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/Test-NoTabs/
Source0:	http://search.cpan.org/CPAN/authors/id/B/BO/BOBTFISH/Test-NoTabs-%{version}.tar.gz
BuildArch:	noarch
# Module Build
BuildRequires:	perl
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(Config.pm)
BuildRequires:	perl(Cwd.pm)
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
BuildRequires:	perl(ExtUtils/Manifest.pm)
BuildRequires:	perl(Fcntl.pm)
BuildRequires:	perl(File/Path.pm)
BuildRequires:	perl(FileHandle.pm)
BuildRequires:	perl(Parse/CPAN/Meta.pm)
BuildRequires:	perl(YAML/Tiny.pm)
BuildRequires:	tar > 1.15.1
# Module Runtime
BuildRequires:	perl(File/Find.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(FindBin.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(vars.pm)
BuildRequires:	perl(warnings.pm)
# Test Suite
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(Test/More.pm)
# Optional Tests
BuildRequires:	perl(Test/Pod.pm)
BuildRequires:	perl(Test/Pod/Coverage.pm)
Source44: import.info
# Runtime

%description
This module scans your project/distribution for any perl files (scripts,
modules, etc.) for the presence of tabs.

%prep
%setup -q -n Test-NoTabs-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir --skip INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/Test/

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_4
- update to new release by fcimport

* Sun Dec 27 2015 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1_3
- update to new release by fcimport

* Mon Feb 02 2015 Igor Vlasenko <viy@altlinux.ru> 1.4-alt1
- automated CPAN update

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_9
- update to new release by fcimport

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_8
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_7
- update to new release by fcimport

* Tue Jul 16 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_6
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_5
- update to new release by fcimport

* Tue Dec 11 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt2_4
- moved to Sisyphus (Tapper dep)

* Sat Nov 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_4
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.3-alt1_3
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 1.1-alt1_3
- fc import

