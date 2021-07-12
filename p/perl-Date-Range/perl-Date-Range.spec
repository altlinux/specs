# BEGIN SourceDeps(oneline):
BuildRequires(pre): rpm-build-perl
BuildRequires: perl-podlators
# END SourceDeps(oneline)
# see https://bugzilla.altlinux.org/show_bug.cgi?id=10382
%define _localstatedir %{_var}
%define upstream_name    Date-Range
%define upstream_version 1.41

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt3_9

Summary:    Work with a range of dates
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Date/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires: perl(Date/Simple.pm)
BuildRequires: perl(ExtUtils/MakeMaker.pm)
BuildRequires: perl(Test/More.pm)
BuildArch: noarch
Source44: import.info

%description
Quite often, when dealing with dates, we don't just want to know
information about one particular date, but about a range of dates. For
example, we may wish to know whether a given date is in a particular range,
or what the overlap is between one range and another. This module lets you
ask such questions.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor

%make

%check
%make test

%install
%makeinstall_std

%files
%doc Changes META.yml README
%perl_vendor_privlib/*




%changelog
* Mon Jul 12 2021 Igor Vlasenko <viy@altlinux.org> 1.41-alt3_9
- to Sisyphus as perl-Finance-Quote dep

* Sat Feb 15 2020 Igor Vlasenko <viy@altlinux.ru> 1.41-alt2_9
- update by mgaimport

* Thu Oct 04 2018 Igor Vlasenko <viy@altlinux.ru> 1.41-alt2_8
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.41-alt2_7
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.41-alt2_6
- update by mgaimport

* Wed Dec 17 2014 Igor Vlasenko <viy@altlinux.ru> 1.41-alt2_5
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.41-alt2_4
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 1.41-alt2_3
- rebuild to get rid of unmets

* Mon Oct 21 2013 Igor Vlasenko <viy@altlinux.ru> 1.41-alt1_3
- mga update

* Wed Aug 07 2013 Igor Vlasenko <viy@altlinux.ru> 1.41-alt1_2
- mgaimport update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.41-alt1_1
- converted for ALT Linux by srpmconvert tools

