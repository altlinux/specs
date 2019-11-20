Group: Development/Perl
# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(Data/Dumper.pm) perl(Module/Build.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
Name:           perl-MooseX-AttributeHelpers
Version:        0.25
Release:        alt1_12
Summary:        Extended Moose attribute interfaces
License:        GPL+ or Artistic
URL:            https://metacpan.org/release/MooseX-AttributeHelpers
Source0:        https://cpan.metacpan.org/authors/id/E/ET/ETHER/MooseX-AttributeHelpers-%{version}.tar.gz

BuildArch:      noarch
Requires:       sed

BuildRequires:  rpm-build-perl
BuildRequires:  perl(Module/Build/Tiny.pm)
BuildRequires:  perl(Moose.pm)
BuildRequires:  perl(Test/Exception.pm)
BuildRequires:  perl(Test/Moose.pm)
BuildRequires:  perl(Test/More.pm)

### auto-added reqs!
Requires:  perl(Moose.pm) >= 0.560


Source44: import.info

%description
While Moose attributes provide you with a way to name your accessors,
readers, writers, clearers and predicates, this library provides commonly
used attribute helper methods for more specific types of data.

%prep
%setup -q -n MooseX-AttributeHelpers-%{version}

%build
/usr/bin/perl Build.PL --installdirs=vendor
./Build
sed -i '1s,#!perl,#!%{__perl},' t/*.t

%install
./Build install --destdir=$RPM_BUILD_ROOT --create_packlist=0
# %{_fixperms} $RPM_BUILD_ROOT/*

%check
./Build test

%files
%doc Changes README t/
%doc --no-dereference LICENSE
%{perl_vendor_privlib}/MooseX*

%changelog
* Wed Nov 20 2019 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_12
- update to new release by fcimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_8
- update to new release by fcimport

* Mon Oct 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_6
- update to new release by fcimport

* Thu Mar 16 2017 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_3
- update to new release by fcimport

* Mon Dec 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_2
- update to new release by fcimport

* Sat Apr 09 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_1.1
- rebuild to restore role requires

* Mon Mar 07 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1_1
- update to new release by fcimport

* Thu Mar 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.25-alt1
- automated CPAN update

* Sun Sep 20 2015 Igor Vlasenko <viy@altlinux.ru> 0.24-alt1_1
- update to new release by fcimport

* Mon Oct 27 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt3_13
- update to new release by fcimport

* Tue Jul 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt3_12
- update to new release by fcimport

* Thu Mar 06 2014 Igor Vlasenko <viy@altlinux.ru> 0.23-alt3_11
- moved to Sisyphus as dependency

* Tue Aug 27 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2_11
- update to new release by fcimport

* Mon Aug 05 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2_10
- update to new release by fcimport

* Mon Mar 04 2013 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2_9
- update to new release by fcimport

* Tue Jul 31 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2_8
- update to new release by fcimport

* Fri May 25 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt2_6
- fc import

* Thu May 24 2012 Igor Vlasenko <viy@altlinux.ru> 0.23-alt1_6
- fc import

* Mon Dec 15 2008 Michael Bochkaryov <misha@altlinux.ru> 0.14-alt1
- 0.14 version

* Tue Jul 29 2008 Michael Bochkaryov <misha@altlinux.ru> 0.11-alt1
- first build for ALT Linux Sisyphus

