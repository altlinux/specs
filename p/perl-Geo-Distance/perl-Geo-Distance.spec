%define dist Geo-Distance
Name: perl-%dist
Version: 0.20
Release: alt1

Summary: Calculate Distances and Closest Locations
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: http://www.cpan.org/authors/id/B/BL/BLUEFEET/Geo-Distance-%{version}.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: perl-DBD-SQLite perl-Math-Complex perl-Test-Script perl(Test/Fatal.pm)

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
* Tue Oct 23 2012 Igor Vlasenko <viy@altlinux.ru> 0.20-alt1
- automated CPAN update

* Wed Sep 26 2012 Igor Vlasenko <viy@altlinux.ru> 0.19-alt1
- automated CPAN update

* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 0.17-alt1
- initial revision
