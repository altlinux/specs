%define real_name Chart-Clicker

Name: perl-%real_name
Version: 2.90
Release: alt1

Summary: Powerful, extensible charting

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/G/GP/GPHAT/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel
BuildRequires: perl-Moose perl-Class-Load
BuildRequires: perl-DateTime perl-DateTime-Set
BuildRequires: perl-Color-Scheme
BuildRequires: perl-Geometry-Primitive perl-Graphics-Color
BuildRequires: perl-Graphics-Primitive perl-Graphics-Primitive-Driver-Cairo
BuildRequires: perl-Layout-Manager
BuildRequires: perl-Test-Exception perl-Test-Fatal

%description
Chart::Clicker is a powerful, extensible charting package for Perl that
creates pretty output in PNG, SVG, PDF and PostScript format. It leverages
Graphics::Primitive for drawing and supports many renderer types (line, bar,
area, pie, stacked, point, bubble) with flexible axes, decorations and
layouts.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README README.mkdn
%perl_vendor_privlib/Chart/Clicker*

%changelog
* Tue Jul 28 2026 Vitaly Lipatov <lav@altlinux.ru> 2.90-alt1
- initial build for Sisyphus
