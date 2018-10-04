%define upstream_name    Parse-EDID
%define upstream_version 1.0.7

Name:       perl-%{upstream_name}
Version:    %{upstream_version}
Release:    alt2

Summary:    Extended display identification data (EDID) parser
License:    GPL+ or Artistic
Group:      Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Parse/%{upstream_name}-%{upstream_version}.tar.gz
BuildRequires: perl(Test/Warn.pm)
BuildArch: noarch

BuildRequires(pre): rpm-build-perl
BuildRequires: perl(English.pm) perl(Exporter.pm) perl(ExtUtils/MakeMaker.pm) perl(Test/Kwalitee.pm) perl(Test/More.pm) perl(Test/Pod.pm) perl(Test/Pod/Coverage.pm)

%description
This module provides some function to parse Extended Display Identification
Data binary data structures.

Extended Display Identification Data (EDID) is a metadata format for
display devices to describe their capabilities to a video source. The
data format is defined by a standard published by the Video Electronics
Standards Association (VESA).

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
rm t/kwalite.t

%build
/usr/bin/perl Makefile.PL INSTALLDIRS=vendor
%make_build

%check
%make test

%install
%makeinstall_std

%files
%doc README META.yml META.json Changes
%perl_vendor_privlib/*

%changelog
* Tue Sep 25 2018 Andrey Cherepanov <cas@altlinux.org> 1.0.7-alt2
- Build for Sisyphus.

* Mon Aug 27 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_2
- update by mgaimport

* Sat Jul 14 2018 Igor Vlasenko <viy@altlinux.ru> 1.0.7-alt1_1
- update by mgaimport

* Wed Jul 27 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt2_5
- update by mgaimport

* Sun Feb 21 2016 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt2_4
- update by mgaimport

* Thu Oct 16 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt2_3
- update by mgaimport

* Tue Oct 07 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt2_2
- update by mgaimport

* Tue Sep 02 2014 Cronbuild Service <cronbuild@altlinux.org> 1.0.6-alt2_1
- rebuild to get rid of unmets

* Thu Feb 20 2014 Igor Vlasenko <viy@altlinux.ru> 1.0.6-alt1_1
- update by mgaimport

* Tue Nov 26 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_3
- mga update

* Sun Oct 13 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_2
- mga update

* Thu Jul 25 2013 Igor Vlasenko <viy@altlinux.ru> 1.0.4-alt1_1
- converted for ALT Linux by srpmconvert tools

