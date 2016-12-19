# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
Name:           perl-Color-Library
Version:        0.021
Release:        alt2_9
Summary:        Easy-to-use and comprehensive named-color library
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Color-Library/
Source0:        http://www.cpan.org/authors/id/R/RO/ROKR/Color-Library-%{version}.tar.gz
# Fix POD syntax, CPAN RT#86023
Patch0:         Color-Library-0.021-pod-fixes.patch
BuildArch:      noarch
BuildRequires:  findutils
BuildRequires:  perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Run-time:
BuildRequires:  perl(base.pm)
BuildRequires:  perl(Class/Accessor/Fast.pm)
BuildRequires:  perl(Class/Data/Inheritable.pm)
BuildRequires:  perl(Module/Pluggable.pm)
BuildRequires:  perl(overload.pm)
# Tests:
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Most.pm)
Requires:       perl(overload.pm)
Source44: import.info

%description
Color::Library is an easy-to-use and comprehensive named-color
dictionary. Currently provides coverage for WWW (SVG, HTML, CSS) colors,
X11 colors, and more.

%prep
%setup -q -n Color-Library-%{version}
%patch0 -p1

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor
make %{?_smp_mflags}

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
find $RPM_BUILD_ROOT -type f -name .packlist -delete
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc Changes README
%{perl_vendor_privlib}/*

%changelog
* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.021-alt2_9
- update to new release by fcimport

* Tue Mar 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.021-alt2_8
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.021-alt2_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.021-alt2_6
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.021-alt2_4
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.021-alt2_3
- update to new release by fcimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 0.021-alt2_2
- moved to Sisyphus for Slic3r (by dd@ request)

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1_2
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.021-alt1_1
- update to new release by fcimport

* Fri Apr 12 2013 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_13
- update from fc import

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_12
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1_10
- fc import

