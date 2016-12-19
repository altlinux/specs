Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Module/Build.pm) perl-podlators
# END SourceDeps(oneline)
Name:		perl-SUPER
Version:	1.20141117
Release:	alt2_6
Summary:	Sane superclass method dispatcher
License:	GPL+ or Artistic
URL:		http://search.cpan.org/dist/SUPER/
Source0:	http://search.cpan.org/CPAN/authors/id/C/CH/CHROMATIC/SUPER-%{version}.tar.gz
BuildArch:	noarch
# =============== Module Build =================
BuildRequires:	coreutils
BuildRequires:	findutils
BuildRequires:	perl
BuildRequires:	rpm-build-perl
BuildRequires:	perl(ExtUtils/MakeMaker.pm)
# =============== Module Runtime ===============
BuildRequires:	perl(Carp.pm)
BuildRequires:	perl(Scalar/Util.pm)
BuildRequires:	perl(strict.pm)
BuildRequires:	perl(Sub/Identify.pm)
BuildRequires:	perl(warnings.pm)
# =============== Test Suite ===================
BuildRequires:	perl(base.pm)
BuildRequires:	perl(lib.pm)
BuildRequires:	perl(Test/More.pm)
# =============== Module Runtime ===============
Requires:	perl(Scalar/Util.pm) >= 1.20
Requires:	perl(Sub/Identify.pm) >= 0.03
Source44: import.info

%description
When subclassing a class, you occasionally want to dispatch control to the
superclass - at least conditionally and temporarily. This module provides
an easier, cleaner way for class methods to access their ancestor's
implementation.

%prep
%setup -q -n SUPER-%{version}

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=%{buildroot}
find %{buildroot} -type f -name .packlist -delete
# %{_fixperms} %{buildroot}

%check
make test

%files
%if 0%{?_licensedir:1}
%doc LICENSE
%else
%doc LICENSE
%endif
%doc Changes README
%{perl_vendor_privlib}/SUPER.pm

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 1.20141117-alt2_6
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.20141117-alt2_4
- update to new release by fcimport

* Thu Oct 15 2015 Igor Vlasenko <viy@altlinux.ru> 1.20141117-alt2_3
- moved to Sisyphus

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 1.20141117-alt1_3
- update to new release by fcimport

* Tue Dec 23 2014 Igor Vlasenko <viy@altlinux.ru> 1.20141117-alt1_1
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.20120705-alt1_7
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.20120705-alt1_6
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.20120705-alt1_5
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.20120705-alt1_4
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 1.20120705-alt1_3
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 1.20120705-alt1_2
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 1.17-alt2_7
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 1.17-alt1_7
- fc import

