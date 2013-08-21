%define module Source-Package

Name: perl-%module
Version: 0.01
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for converting SRPM and spec files
Group: Development/Perl
License: GPL or Artistic
Source: %module-%version.tar
Url: http://search.cpan.org/dist/%module

BuildRequires: perl-devel  
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
#doc Changes
#doc README
%perl_vendor_privlib/Source*

%changelog
* Wed Aug 21 2013 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- first build for Sisyphus
