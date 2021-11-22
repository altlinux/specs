%define module RPM-Devscripts-Versort

Name: perl-%module
Version: 0.01
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - rpm version comparator functions.
Group: Development/Perl
License: GPLv2+ or Artistic-2.0
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

BuildRequires: perl-devel perl-RPM-Vercmp

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
%perl_vendor_privlib/RPM*

%changelog
* Mon Nov 22 2021 Igor Vlasenko <viy@altlinux.org> 0.01-alt1
- new version

