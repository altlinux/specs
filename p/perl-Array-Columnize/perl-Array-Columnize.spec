# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl(CPAN.pm) perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Array-Columnize
%define upstream_version 1.04

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt3_11

Summary:    Arrange list data in columns
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Array/%{upstream_name}-%{upstream_version}.tar.gz
# Not real packages:
%global __requires_exclude %{?__requires_exclude:%__requires_exclude|}^perl\\(Array::Columnize::(columnize|options)\\)$

BuildRequires: perl(Module/Build.pm)
BuildRequires: perl(Test/More.pm)
BuildRequires: perl(rlib.pm)
BuildRequires: perl(version.pm)
BuildArch:  noarch
Source44: import.info

%description
Array::Columnize displays the contents of arrays in columns.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Build.PL installdirs=vendor

./Build

%check
./Build test

%install
./Build install destdir=%{buildroot}

%files
%doc ChangeLog Changes META.json META.yml  SIGNATURE eg
%perl_vendor_privlib/*


%changelog
* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 1.04-alt3_11
- to Sisyphus as perl-Devel-Trepan dep

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_11
- update by mgaimport

* Fri Mar 15 2019 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_10
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_9
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_8
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_7
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_6
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.04-alt2_5
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 1.04-alt2_2
- rebuild to get rid of unmets

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_2
- mga update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.04-alt1_1
- mgaimport update

* Tue Jul 30 2013 Igor Vlasenko <viy@altlinux.ru> 1.02-alt1_1
- converted for ALT Linux by srpmconvert tools

