# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(App/pod2pdf.pm) perl(CPAN.pm) perl(JSON.pm) perl(LWP/Simple.pm) perl(Module/Build.pm) perl(Net/FTP.pm) perl(Parse/CPAN/Meta.pm) perl(YAML/Tiny.pm) perl-podlators
# END SourceDeps(oneline)
Name:           perl-Test-utf8
Version:        1.01
Release:        alt1_5
Summary:        Handy utf8 tests
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Test-utf8/
Source0:        http://www.cpan.org/authors/id/M/MA/MARKF/Test-utf8-%{version}.tar.gz
BuildArch:      noarch
# Module Build
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Module Runtime
BuildRequires:  perl(base.pm)
BuildRequires:  perl(charnames.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/Builder.pm)
BuildRequires:  perl(warnings.pm)
# Test Suite
BuildRequires:  perl(Test/Builder/Tester.pm)
BuildRequires:  perl(Test/More.pm)
# Runtime


Source44: import.info

%description
This module is a collection of tests that's useful when dealing with utf8
strings in Perl.

%prep
%setup -q -n Test-utf8-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -exec rm -f {} \;
# %{_fixperms} %{buildroot}

%check
make test

%files
%doc CHANGES README
%{perl_vendor_privlib}/Test/

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_5
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_4
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_3
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_1
- update to new release by fcimport

* Tue Jan 14 2014 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1
- automated CPAN update

* Mon Aug 12 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_6
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_5
- update to new release by fcimport

* Fri Feb 22 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_4
- update to new release by fcimport

* Mon Dec 10 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_3
- moved to Sisyphus

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2_3
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt2_1
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_1
- fc import

