%define real_name Graphics-Primitive

Name: perl-%real_name
Version: 0.67
Release: alt1

Summary: Device and library agnostic graphic primitives

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/G/GP/GPHAT/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel
BuildRequires: perl-Moose perl-MooseX-Clone perl-MooseX-Storage
BuildRequires: perl-Forest perl-Geometry-Primitive perl-Graphics-Color
BuildRequires: perl-Data-Visitor perl-JSON-Any

%description
Graphics::Primitive is a device- and library-agnostic drawing abstraction
providing components, containers, brushes, paths, paints, fonts and layout
operations. It is the rendering substrate used by charting and graphics
drivers (such as Graphics::Primitive::Driver::Cairo) to describe what to
draw without being tied to a specific backend.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Graphics/Primitive*

%changelog
* Tue Jul 28 2026 Vitaly Lipatov <lav@altlinux.ru> 0.67-alt1
- initial build for Sisyphus
