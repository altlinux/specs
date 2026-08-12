%define real_name Graphics-Color

Name: perl-%real_name
Version: 0.31
Release: alt1

Summary: Device and library agnostic color spaces

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name
# Source-url: https://cpan.metacpan.org/authors/id/G/GP/GPHAT/%real_name-%version.tar.gz
Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel
BuildRequires: perl-Moose perl-MooseX-Aliases perl-MooseX-Clone perl-MooseX-Storage
BuildRequires: perl-MooseX-Types perl-Color-Library
BuildRequires: perl-Test-Number-Delta

%description
Graphics::Color provides device- and library-agnostic color representations
(RGB, HSL, CMYK, HSV, Lab, YIQ, etc.) with conversion between them. Built on
Moose, it is used by rendering and charting libraries that need a uniform
color abstraction independent of any specific backend.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc Changes LICENSE README
%perl_vendor_privlib/Graphics/Color*

%changelog
* Tue Jul 28 2026 Vitaly Lipatov <lav@altlinux.ru> 0.31-alt1
- initial build for Sisyphus
