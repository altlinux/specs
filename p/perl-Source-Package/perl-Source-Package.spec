%define module Source-Package

Name: perl-%module
Version: 0.10
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: %module-%version.tar
Url: http://search.cpan.org/dist/%module

BuildRequires: perl-devel perl(RPM/Vercmp.pm)
#Requires: perl-RPM-Source-Editor > 0.801
Conflicts: perl-Source-Repository < 0.12

%description
%summary

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
#doc README
%perl_vendor_privlib/Source*

%changelog
* Wed Oct 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.10-alt1
- bugfix release

* Wed Oct 26 2016 Igor Vlasenko <viy@altlinux.ru> 0.09-alt1
- added rpm.org epoch comarators

* Tue Oct 04 2016 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1
- indirect RPM br:

* Mon Oct 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.07-alt1
- use RPM-Vercmp

* Mon Jun 30 2014 Igor Vlasenko <viy@altlinux.ru> 0.06-alt1
- new version

* Thu May 01 2014 Igor Vlasenko <viy@altlinux.ru> 0.05-alt1
- autodownload

* Fri Apr 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.04-alt1
- added Source::Package::Comparators::Raw

* Fri Apr 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added Source::Package::Pair

* Fri Apr 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added Source::Package::Comparator

* Wed Aug 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first build for Sisyphus
