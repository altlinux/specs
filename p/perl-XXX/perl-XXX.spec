%filter_from_requires /^perl.Enbugger.pm./d
%define _unpackaged_files_terminate_build 1
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Test/Pod.pm) perl-podlators perl(YAML/PP.pm)
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-XXX
Version:        0.38
Release:        alt2
Summary:        See Your Data in the Nude
License:        GPL+ or Artistic
Group:          Development/Other
URL:            https://metacpan.org/release/XXX
Source0:        http://www.cpan.org/authors/id/I/IN/INGY/XXX-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(warnings.pm)
BuildRequires:  perl(YAML.pm)
Requires:       perl(Data/Dumper.pm)
Requires:       perl(YAML.pm)
Source44: import.info

%description
XXX.pm exports a function called XXX that you can put just about
anywhere in your Perl code to make it die with a YAML dump of the
arguments to its right.

The charm of XXX-debugging is that it is easy to type and rarely
requires parens and stands out visually so that you remember to remove
it.

XXX.pm also exports WWW, YYY and ZZZ which do similar debugging things.

To use Data::Dumper instead of YAML:
   use XXX -dumper;

%prep
%setup -q -n XXX-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=true
%make_build

%install
make pure_install DESTDIR=%{buildroot}
# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc CONTRIBUTING
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Oct 30 2023 Igor Vlasenko <viy@altlinux.org> 0.38-alt2
- forcibly removed Embugger from Requires.

* Sun Jul 11 2021 Igor Vlasenko <viy@altlinux.org> 0.38-alt1
- automated CPAN update

* Sat Jun 19 2021 Igor Vlasenko <viy@altlinux.org> 0.36-alt1
- automated CPAN update

* Wed Jan 22 2020 Igor Vlasenko <viy@altlinux.ru> 0.35-alt1
- automated CPAN update

* Mon Jun 17 2019 Igor Vlasenko <viy@altlinux.ru> 0.33-alt1
- automated CPAN update

* Fri Dec 07 2018 Igor Vlasenko <viy@altlinux.ru> 0.32-alt1
- automated CPAN update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_6
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_4
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_3
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1_2
- update to new release by fcimport

* Sat Jan 14 2017 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1
- automated CPAN update

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1_2
- update to new release by fcimport

* Tue May 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.30-alt1
- automated CPAN update

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.29-alt2_4
- update to new release by fcimport

* Tue Dec 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.29-alt2_3
- to sisyphus

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1_3
- update to new release by fcimport

* Wed Apr 08 2015 Igor Vlasenko <viy@altlinux.ru> 0.29-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.28-alt1_1
- update to new release by fcimport

* Wed Sep 10 2014 Igor Vlasenko <viy@altlinux.ru> 0.27-alt1_1
- update to new release by fcimport

* Mon Jul 07 2014 Igor Vlasenko <viy@altlinux.ru> 0.21-alt1_1
- update to new release by fcimport

* Mon Sep 02 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_7
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_6
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_5
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_4
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.18-alt1_2
- fc import

