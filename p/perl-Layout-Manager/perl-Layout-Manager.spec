%define real_name Layout-Manager

Name: perl-%real_name
Version: 0.35
Release: alt1

Summary: 2D Layout Management

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/G/GP/GPHAT/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel
BuildRequires: perl-Moose perl-Geometry-Primitive perl-Graphics-Primitive

%description
Layout::Manager is a 2D layout management library for Perl. It provides
pluggable layout strategies (Flow, Compass, Grid, Absolute, Axis, Single)
that compute the size and position of Graphics::Primitive components within
a container, similar to layout managers in GUI toolkits.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes README
%perl_vendor_privlib/Layout/Manager*

%changelog
* Tue Jul 28 2026 Vitaly Lipatov <lav@altlinux.ru> 0.35-alt1
- initial build for Sisyphus
