%define module Source-Shared-Utils

Name: perl-%module
Version: 0.004
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - a small collection of utils for Source-Shared
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl(Module/Build/Tiny.pm)

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
* Sun Feb 10 2019 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- added Downloader

* Sat Sep 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- removed Source/Shared/Utils.pm

* Sat Sep 30 2017 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- added Source/Shared/Utils/GlobList.pm

* Wed Sep 27 2017 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version
