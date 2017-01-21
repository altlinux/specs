%define module Source-Shared-CLI

Name: perl-%module
Version: 0.002
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - yet another framework for CLI module configuration
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
%perl_vendor_build INSTALLMAN1DIR=%_man1dir

%install
%perl_vendor_install

%files
#doc Changes
#doc README
%perl_vendor_privlib/S*

%changelog
* Sat Jan 21 2017 Igor Vlasenko <viy@altlinux.ru> 0.002-alt1
- new version

* Wed Jan 18 2017 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version
