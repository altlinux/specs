%define module Gear-Remotes

Name: perl-%module
Version: 0.001
Release: alt1
BuildArch: noarch
Packager: Igor Yu. Vlasenko <viy@altlinux.org>

Summary: %module - Perl extension for quering Gear rules files
Group: Development/Perl
License: GPL or Artistic
Source: http://www.cpan.org/modules/by-module/RPM/%module-%version.tar.gz
Url: http://search.cpan.org/dist/%module

# Automatically added by buildreq on Wed Nov 06 2002
BuildRequires: perl-devel perl(Pod/Usage.pm) perl(Pod/Text.pm) perl(RPM/uscan.pm)
Requires: gear perl(Pod/Text.pm)

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
%perl_vendor_privlib/G*
%_bindir/*

%changelog
* Wed Jul 23 2014 Igor Vlasenko <viy@altlinux.ru> 0.001-alt1
- new version
