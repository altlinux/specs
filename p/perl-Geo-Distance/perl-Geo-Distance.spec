%define dist Geo-Distance
Name: perl-%dist
Version: 0.17
Release: alt1

Summary: Calculate Distances and Closest Locations
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: perl-DBD-SQLite perl-Math-Complex perl-Test-Script

%description
This perl library aims to provide as many tools to make it as simple as
possible to calculate distances between geographic points, and anything
that can be derived from that.  Currently there is support for finding
the closest locations within a specified distance, to find the closest
number of points to a specified point, and to do basic point-to-point
distance calculations.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Geo

%changelog
* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 0.17-alt1
- initial revision
