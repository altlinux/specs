%define module Source-Package

Name: perl-%module
Version: 0.03
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: %module-%version.tar
Url: http://search.cpan.org/dist/%module

BuildRequires: perl-devel perl-RPM
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
* Fri Apr 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.03-alt1
- added Source::Package::Pair

* Fri Apr 18 2014 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added Source::Package::Comparator

* Wed Aug 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first build for Sisyphus
