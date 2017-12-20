Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-Convert-UU
Version:        0.5201
Release:        alt3_18
Summary:        Perl module for uuencode and uudecode
License:        GPL+ or Artistic
URL:            http://search.cpan.org/dist/Convert-UU/
Source0:        http://www.cpan.org/authors/id/A/AN/ANDK/Convert-UU-%{version}.tar.gz
BuildArch:      noarch
BuildRequires:  perl-DBM perl-I18N-Collate perl-I18N-LangTags perl-NEXT perl-POSIX-1003 perl-Term-ReadLine-Gnu perl-Tie-File perl-Tie-RefHash perl-base perl-devel perl-threads perl-unicore
BuildRequires:  rpm-build-perl
BuildRequires:  perl(ExtUtils/MakeMaker.pm)
BuildRequires:  sed
# Run-time
BuildRequires:  perl(Carp.pm)
BuildRequires:  perl(Exporter.pm)
BuildRequires:  perl(strict.pm)
BuildRequires:  perl(warnings.pm)
# Tests
BuildRequires:  perl(File/Spec.pm)
BuildRequires:  perl(Test/More.pm)
BuildRequires:  perl(Test/Pod.pm)
BuildRequires:  perl(Test/Pod/Coverage.pm)
# ext-uu.t needs sharutils, otherwise it's skipped
BuildRequires:  sharutils
Source44: import.info

%description
%{summary}.

%prep
%setup -q -n Convert-UU-%{version}
sed -i 's|local\/perl5\.002_01\/||' puudecode

%build
perl Makefile.PL INSTALLMAN1DIR=%_man1dir INSTALLDIRS=perl NO_PACKLIST=1
%make_build

%install
make pure_install DESTDIR=$RPM_BUILD_ROOT
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
make test

%files
%doc ChangeLog README
%{_bindir}/puudecode
%{_bindir}/puuencode
%{perl_vendor_privlib}/*
%{_mandir}/man1/*

%changelog
* Wed Dec 20 2017 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt3_18
- fixed build with new perl 5.26

* Sun Nov 05 2017 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt2_18
- to Sisyphus as perl-PDL dep

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt1_18
- update to new release by fcimport

* Thu Aug 03 2017 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt1_17
- update to new release by fcimport

* Wed Mar 15 2017 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt1_16
- update to new release by fcimport

* Sun May 29 2016 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt1_15
- update to new release by fcimport

* Wed Mar 02 2016 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt1_14
- update to new release by fcimport

* Mon Sep 21 2015 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt1_13
- update to new release by fcimport

* Tue Sep 16 2014 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt1_11
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt1_10
- update to new release by fcimport

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt1_9
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt1_8
- update to new release by fcimport

* Wed Feb 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt1_7
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt1_6
- update to new release by fcimport

* Wed May 30 2012 Igor Vlasenko <viy@altlinux.ru> 0.5201-alt1_4
- fc import

