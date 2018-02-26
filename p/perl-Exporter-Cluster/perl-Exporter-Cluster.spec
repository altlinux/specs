## SPEC file for Perl module Exporter::Cluster

%define version    0.31
%define release    alt1

Name: perl-Exporter-Cluster
Version: %version
Release: alt1.1

Summary: Perl extension for easy multiple module imports
#Summary(ru_RU.UTF-8): расширение Perl для упрощения импорта подулей

License: GPL or Artistic
Group: Development/Perl
URL: http://search.cpan.org/~dhageman/Exporter-Cluster/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Exporter-Cluster
Source: http://search.cpan.org/CPAN/authors/id/D/DH/DHAGEMAN/%real_name-%version.tar.gz

AutoReqProv: perl, yes
BuildPreReq: perl-devel

%description
Perl module Exporter::Cluster is designed to allow the user to
develop a binding package  that allows multiple packages to be 
imported into the symbol table with single 'use' command.

%prep
%setup  -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Exporter/Cluster*

%changelog
* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.31-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Sat Sep 16 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.31-alt1
- Initial build for ALT Linux Sisyphus

* Thu Aug 10 2006 Nikolay A. Fetisov <naf@altlinux.ru> 0.31-alt0
- Initial build
