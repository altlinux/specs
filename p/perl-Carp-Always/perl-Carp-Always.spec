Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Carp-Always
Version:        0.16
Release:        alt1_4
Summary:        Warn and die in Perl noisily with stack backtraces
License:        GPL+ or Artistic

URL:            https://metacpan.org/release/Carp-Always
Source0:        https://cpan.metacpan.org/authors/id/F/FE/FERREIRA/Carp-Always-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
# Run-time
BuildRequires:  perl(Carp.pm)
# Tests
BuildRequires:  perl(Test/Base.pm)
BuildRequires:  perl(Test/More.pm)
# Optional tests
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)


Source44: import.info

%description
This module is meant as a debugging aid. It can be used to make a script
complain loudly with stack backtraces when warn()ing or die()ing.


%prep
%setup -q -n Carp-Always-%{version}


%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor NO_PACKLIST=1
%make_build

# Recode
iconv -f iso8859-1 -t utf8 README >README.utf8
touch -r README README.utf8
mv README.utf8 README


%install
make pure_install PERL_INSTALL_ROOT=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*


%check
make test


%files
%doc Changes README
%{perl_vendor_privlib}/*


%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_4
- update to new release by fcimport

* Wed Oct 10 2018 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1_1
- update to new release by fcimport

* Tue Aug 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.16-alt1
- automated CPAN update

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_13
- update to new release by fcimport

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_11
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_10
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_9
- update to new release by fcimport

* Tue Jul 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_8
- update to new release by fcimport

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_7
- update to new release by fcimport

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_5
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_3
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_2
- update to new release by fcimport

* Wed Dec 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt2_1
- Sisyphus build

* Wed Nov 20 2013 Igor Vlasenko <viy@altlinux.ru> 0.13-alt1_1
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_4
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_3
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_2
- update to new release by fcimport

* Tue Oct 09 2012 Igor Vlasenko <viy@altlinux.ru> 0.12-alt1_1
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.11-alt1_3
- update to new release by fcimport

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1_6
- fc import

