%define module RPM-Specfile-Multispec

Name: perl-%module
Version: 1.09
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - RPM::Specfile extension with subpackage support.
Group: Development/Perl
License: GPLv2+ or Artistic-2.0
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

BuildRequires: perl-devel perl-RPM-Specfile

%description
%summary
This module extends RPM::Specfile with subpackage support.

%prep
%setup -q -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes
#doc README
%perl_vendor_privlib/RPM*

%changelog
* Wed Dec 01 2021 Igor Vlasenko <viy@altlinux.org> 1.09-alt1
- separate distribution

