%define dist Geo-Point
Name: perl-%dist
Version: 0.93
Release: alt1

Summary: Geographical structures
License: GPL or Artistic
Group: Development/Perl

URL: %CPAN %dist
Source: %dist-%version.tar.gz

BuildArch: noarch

# Automatically added by buildreq on Fri Nov 11 2011
BuildRequires: perl-Geo-Distance perl-Geo-Proj4 perl-Math-Polygon perl-Test-Pod

%description
Geo::Point tries to abstract coordinate systems.  It does not try
to solve all the problems itself, but will call-out for helper modules
when computation has to be done.

%prep
%setup -q -n %dist-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc ChangeLog README
%perl_vendor_privlib/Geo

%changelog
* Fri Nov 11 2011 Alexey Tourbin <at@altlinux.ru> 0.93-alt1
- initial revision
