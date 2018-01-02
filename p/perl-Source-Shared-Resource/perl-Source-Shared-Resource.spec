%define module Source-Shared-Resource

Name: perl-%module
Version: 0.005
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - yet another framework for Resource module configuration
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

BuildRequires: perl-devel perl(Module/Build/Tiny.pm) perl-Source-Shared-CLI perl-DistroMap

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
%perl_vendor_privlib/S*

%changelog
* Tue Jan 02 2018 Igor Vlasenko <viy@altlinux.ru> 0.005-alt1
- run debug first

* Sat May 06 2017 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- shared verbose for containers

* Thu Feb 02 2017 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- added shared verbose

* Sat Jan 21 2017 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- new CLI 0.002

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version
