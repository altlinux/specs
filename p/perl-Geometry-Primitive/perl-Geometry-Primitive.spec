%define real_name Geometry-Primitive

Name: perl-%real_name
Version: 0.24
Release: alt1

Summary: Primitive Geometry Entities

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/G/GP/GPHAT/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel
BuildRequires: perl-Moose perl-MooseX-Clone perl-MooseX-Storage perl-Check-ISA perl-JSON-Any

%description
Geometry::Primitive is a library of geometric primitives (points, lines,
polygons, circles, arcs, rectangles, etc.) for use by other modules that
need to describe shapes. It is device- and backend-agnostic and built on
top of Moose.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Geometry/Primitive*

%changelog
* Tue Jul 28 2026 Vitaly Lipatov <lav@altlinux.ru> 0.24-alt1
- initial build for Sisyphus
