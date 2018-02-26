%define dist SNMP-Simple
Name: perl-%dist
Version: 0.02
Release: alt1

Summary: shortcuts for when using SNMP
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar
BuildArch: noarch

BuildRequires: perl-devel perl-SNMP

%description
%summary

%prep
%setup -q -n %dist-%version
%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc examples README
%perl_vendor_privlib/SNMP/Simple.pm

%changelog
* Mon Apr 23 2012 Eugene Prokopiev <enp@altlinux.ru> 0.02-alt1
- first build for Sisyphus

