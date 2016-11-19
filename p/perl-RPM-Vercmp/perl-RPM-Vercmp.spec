%define module RPM-Vercmp

Name: perl-%module
Version: 0.02
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - rpm version comparator functions.
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

BuildRequires: perl-devel perl-RPM 

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
* Sat Nov 19 2016 Igor Vlasenko <viy@altlinux.ru> 0.02-alt1
- added export

* Mon Oct 03 2016 Igor Vlasenko <viy@altlinux.ru> 0.01-alt1
- initial commit

