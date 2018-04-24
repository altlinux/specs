%define module Source-Shared-FindLocalMirror

Name: perl-%module
Version: 0.004
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Local Mirror locator for Source-Shared
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl(Module/Build/Tiny.pm) perl(Source/Shared/CLI.pm)

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
%_bindir/*
%perl_vendor_privlib/S*

%changelog
* Tue Apr 24 2018 Igor Vlasenko <viy@altlinux.ru> 0.004-alt1
- new version

* Sun Apr 22 2018 Igor Vlasenko <viy@altlinux.ru> 0.003-alt1
- new version

* Sat Apr 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- added script/altlinux-find-local-mirror

* Sat Apr 21 2018 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version
