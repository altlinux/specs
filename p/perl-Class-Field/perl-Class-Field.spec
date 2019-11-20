Group: Development/Other
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Class-Field
Version:        0.24
Release:        alt1_3
Summary:        Class Field Accessor Generator
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/Class-Field
Source0:        https://cpan.metacpan.org/authors/id/I/IN/INGY/Class-Field-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Data/Dumper.pm)
BuildRequires:  perl(Encode.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(File/Find.pm)
BuildRequires:  perl(lib.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(utf8.pm)
BuildRequires:  perl(warnings.pm)


Source44: import.info

%description
Class::Field exports two subroutines, field and const. These functions are
used to declare fields and constants in your class.

%prep
%setup -q -n Class-Field-%{version}


%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc --no-dereference LICENSE
%doc Changes README
%{perl_vendor_privlib}/Class*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_3
- update to new release by fcimport

* Sat May 25 2019 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_1
- update to new release by fcimport

* Wed Feb 13 2019 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1
- automated CPAN update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_8
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_6
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_5
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_4
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_3
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_2
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_1
- update to new release by fcimport

* Mon Sep 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1
- automated CPAN update

* Wed Aug 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.22-alt1
- automated CPAN update

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_9
- update to new release by fcimport

* Wed Oct 16 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt2_8
- build for Sisyphus (required for perl update)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_8
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_7
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_6
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_5
- update to new release by fcimport

* Wed May 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.15-alt1_3
- fc import

