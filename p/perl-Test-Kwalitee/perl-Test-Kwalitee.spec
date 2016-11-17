Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN/Meta/Requirements.pm) perl-podlators
# END SourceDeps(oneline)
Name:		perl-Test-Kwalitee
Version:	1.23
Release:	alt1_1
Summary:	Test the Kwalitee of a distribution before you release it
License:	GPL+ or Artistic
URL:		http://metacpan.org/module/Test::Kwalitee
Source0:	http://cpan.metacpan.org/authors/id/E/ET/ETHER/Test-Kwalitee-%{version}.tar.gz
BuildArch:	noarch
# Build
BuildRequires:	coreutils
BuildRequires:	perl
BuildRequires:	rpm-build-perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# Module
BuildRequires:	perl(Cwd.pm)
BuildRequires:	perl(Exporter.pm)
BuildRequires:	perl(Module/CPANTS/Analyse.pm)
BuildRequires:	perl(parent.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Test/Builder.pm)
BuildRequires:	perl(warnings.pm)
# Test Suite
BuildRequires:	perl(CPAN/Meta.pm)
BuildRequires:	perl(CPAN/Meta/Check.pm)
BuildRequires:	perl(File/Spec.pm)
BuildRequires:	perl(File/Temp.pm)
BuildRequires:	perl(lib.pm)
BuildRequires:	perl(Scalar/Util.pm)
BuildRequires:	perl(Test/Deep.pm)
BuildRequires:	perl(Test/More.pm)
BuildRequires:	perl(Test/Tester.pm)
BuildRequires:	perl(Test/Warnings.pm)
Source44: import.info
# Dependencies

%description
Kwalitee is an automatically-measurable gauge of how good your software
is. That's very different from quality, which a computer really can't
measure in a general sense (if you can, you've solved a hard problem in
computer science).

%prep
%setup -q -n Test-Kwalitee-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor NO_PERLLOCAL=1 NO_PACKLIST=1
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot}
# %{_fixperms} -c %{buildroot}

%check
make test

%files
%doc LICENSE
%doc Changes CONTRIBUTING README
%{_bindir}/kwalitee-metrics
%{perl_vendor_privlib}/Test/
%{_mandir}/man1/kwalitee-metrics.1*

%changelog
* Thu Nov 17 2016 Igor Vlasenko <viy@altlinux.ru> 1.23-alt1_1
- new version

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1_5
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1_4
- update to new release by fcimport

* Thu Dec 18 2014 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1_2
- update to new release by fcimport

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.22-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1_2
- update to new release by fcimport

* Fri Mar 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1_1
- update to new release by fcimport

* Wed Mar 05 2014 Igor Vlasenko <viy@altlinux.ru> 1.18-alt1
- automated CPAN update

* Thu Nov 14 2013 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_1
- Sisyphus build

* Thu Oct 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.15-alt1_1
- update to new release by fcimport

* Thu Sep 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.14-alt1_1
- update to new release by fcimport

* Fri Aug 02 2013 Igor Vlasenko <viy@altlinux.ru> 1.10-alt1_1
- update to new release by fcimport

* Tue May 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.06-alt1_1
- update to new release by fcimport

* Mon May 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_1
- update to new release by fcimport

* Wed Apr 10 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_1
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_15
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_14
- update to new release by fcimport

* Mon May 28 2012 Igor Vlasenko <viy@altlinux.ru> 1.01-alt1_12
- fc import

