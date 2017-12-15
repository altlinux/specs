# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Math-Libm
Version:        1.00
Release:        alt3_20.1
Summary:        Perl extension for the C math library, libm
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Math-Libm/
Source0:        http://www.cpan.org/authors/id/D/DS/DSLEWART/Math-Libm-%{version}.tar.gz
Source1:        Math-Libm-license.txt
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  perl(AutoLoader.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Exporter.pm)

 # Filters (not)shared c libs
Source44: import.info

%description
This module is a translation of the C math.h file. It exports the following
selected constants and functions:
M_1_PI M_2_PI M_2_SQRTPI M_E M_LN10 M_LN2 M_LOG10E
M_LOG2E M_PI M_PI_2 M_PI_4 M_SQRT1_2 M_SQRT2
acos acosh asin asinh atan atanh cbrt ceil cosh
erf erfc expm1 floor hypot j0 j1 jn lgamma_r
log10 log1p pow rint sinh tan tanh y0 y1 yn

%prep
%setup -q -n Math-Libm-%{version}
cp -p %{SOURCE1} license.txt

%build
%{__perl} Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=vendor OPTIMIZE="$RPM_OPT_FLAGS"
%make_build

%install
make pure_install DESTDIR=%{buildroot}

find %{buildroot} -type f -name .packlist -exec rm -f {} \;
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%check
make test

%files
%doc Changes README license.txt
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Math*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_20.1
- rebuild with new perl 5.26.1

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_20
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_18
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_17
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_16.1
- rebuild with new perl 5.24.1

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_16
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_15
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_14.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_14
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_12.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_12
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_10
- update to new release by fcimport

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.00-alt3_9
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 1.00-alt2_9
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_8
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.00-alt1_7
- initial fc import

