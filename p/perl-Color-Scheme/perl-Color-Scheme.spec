%define real_name Color-Scheme

Name: perl-%real_name
Version: 1.08
Release: alt1

Summary: Generate pleasant color schemes

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/R/RJ/RJBS/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel

%description
Color::Scheme is an object-oriented module for generating pleasant color
schemes (analogous, complementary, triadic, tetradic, etc.) from a base
color. It is a Perl port of the Color Scheme Designer engine.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE
%perl_vendor_privlib/Color/*

%changelog
* Tue Jul 28 2026 Vitaly Lipatov <lav@altlinux.ru> 1.08-alt1
- initial build for Sisyphus
