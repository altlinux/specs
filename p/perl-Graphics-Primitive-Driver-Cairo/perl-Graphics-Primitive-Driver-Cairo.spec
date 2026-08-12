%define real_name Graphics-Primitive-Driver-Cairo

Name: perl-%real_name
Version: 0.47
Release: alt1

Summary: Cairo backend for Graphics::Primitive

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/G/GP/GPHAT/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel
BuildRequires: perl-Cairo perl-Moose
BuildRequires: perl-Geometry-Primitive perl-Graphics-Primitive perl-Graphics-Color perl-Text-Flow

%description
Graphics::Primitive::Driver::Cairo is a Cairo rendering driver for the
Graphics::Primitive drawing abstraction. It turns Graphics::Primitive
components, paths, brushes and paints into Cairo drawing operations,
producing PNG, SVG, PDF and PostScript output.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/Graphics/Primitive/Driver/Cairo*

%changelog
* Tue Jul 28 2026 Vitaly Lipatov <lav@altlinux.ru> 0.47-alt1
- initial build for Sisyphus
