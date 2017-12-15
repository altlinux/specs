# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Math-Factor-XS
Version:        0.40
Release:        alt3_19.1
Summary:        Factorize numbers and calculate matching multiplications
License:        GPL+ or Artistic
Group:          Development/Other
URL:            http://search.cpan.org/dist/Math-Factor-XS/
Source0:        http://www.cpan.org/authors/id/K/KR/KRYDE/Math-Factor-XS-%{version}.tar.gz
BuildRequires:  perl-devel
BuildRequires:  rpm-build-perl
BuildRequires:  perl(boolean.pm)
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(ExtUtils/CBuilder.pm)
BuildRequires:  perl(List/MoreUtils.pm)
BuildRequires:  perl(Math/BigInt.pm)
BuildRequires:  perl(Module/Build.pm)
BuildRequires:  perl(Params/Validate.pm)
BuildRequires:  perl(POSIX.pm)
BuildRequires:  perl(Scalar/Util.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(XSLoader.pm)

 # Filters (not)shared c libs
Source44: import.info

%description
Math::Factor::XS factorizes numbers by applying trial divisions.

%prep
%setup -q -n Math-Factor-XS-%{version}

%build
%{__perl} Build.PL --install_path bindoc=%_man1dir installdirs=vendor optimize="$RPM_OPT_FLAGS"

./Build

%install
./Build install destdir=%{buildroot} create_packlist=0
find %{buildroot} -type f -name '*.bs' -size 0 -exec rm -f {} \;

# %{_fixperms} %{buildroot}/*

%check
./Build test

%files
%doc Changes META.json README scripts
%{perl_vendor_archlib}/auto/*
%{perl_vendor_archlib}/Math*

%changelog
* Fri Dec 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.40-alt3_19.1
- rebuild with new perl 5.26.1

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.40-alt3_19
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.40-alt3_17
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.40-alt3_16
- update to new release by fcimport

* Fri Feb 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.40-alt3_15.1
- rebuild with new perl 5.24.1

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.40-alt3_15
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.40-alt3_14
- update to new release by fcimport

* Wed Nov 25 2015 Igor Vlasenko <viy@altlinux.ru> 0.40-alt3_13.1
- rebuild with new perl 5.22.0

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.40-alt3_13
- update to new release by fcimport

* Tue Dec 09 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt3_11.1
- rebuild with new perl 5.20.1

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt3_11
- update to new release by fcimport

* Wed Aug 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt3_10
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt3_9
- update to new release by fcimport

* Wed Feb 19 2014 Igor Vlasenko <viy@altlinux.ru> 0.40-alt3_8
- moved to Sisyphus for Slic3r (by dd@ request)

* Thu Sep 05 2013 Cronbuild Service <cronbuild@altlinux.org> 0.40-alt2_8
- rebuild to get rid of unmets

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1_8
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1_7
- update to new release by fcimport

* Fri Apr 26 2013 Igor Vlasenko <viy@altlinux.ru> 0.40-alt1_6
- initial fc import

