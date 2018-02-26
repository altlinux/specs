%define module Geo-Coordinates-DecimalDegrees

Name: perl-%module
Version: 0.09
Release: alt1

Summary: Module to convert between degrees/minutes/seconds and decimal degrees
License: Perl
Group: Development/Perl

Url: %CPAN %module
Source: http://www.cpan.org/modules/by-module/Geo/%module-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Mar 23 2012
BuildRequires: perl-Test-Number-Delta perl-Test-Pod

%description
This module provides functions for converting latitudes and longitudes between
degrees/minutes/seconds and decimal degrees.

%prep
%setup -n %module-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%perl_vendor_privlib/Geo

%changelog
* Fri Mar 23 2012 Victor Forsiuk <force@altlinux.org> 0.09-alt1
- 0.09

* Mon Nov 22 2010 Igor Vlasenko <viy@altlinux.ru> 0.08-alt1.1
- repair after perl 5.12 upgrade using girar-nmu

* Mon Aug 31 2009 Victor Forsyuk <force@altlinux.org> 0.08-alt1
- Initial build.
