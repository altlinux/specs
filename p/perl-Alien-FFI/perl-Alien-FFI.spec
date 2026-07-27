%define real_name Alien-FFI

Name: perl-%real_name
Version: 0.27
Release: alt1

Summary: Build and make available libffi

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name

# Source-url: https://cpan.metacpan.org/authors/id/P/PL/PLICEASE/%real_name-%version.tar.gz
Source: %real_name-%version.tar

# Alien::Build installs the module and share data under the arch vendor path
BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Alien-Build perl-Alien-Build-Plugin-Download-GitHub
BuildRequires: libffi-devel pkg-config

%description
Alien::FFI provides a Perl distribution for libffi, the Portable Foreign
Function Interface Library. In system mode it uses the libffi provided by
the operating system.

%prep
%setup -q -n %real_name-%version

%build
# prefer system libffi via pkg-config; avoid Alien download (offline hasher)
export ALIEN_INSTALL_TYPE=system
%perl_vendor_build

%install
export ALIEN_INSTALL_TYPE=system
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/Alien*
%perl_vendor_archlib/auto/Alien
%perl_vendor_archlib/auto/share/dist/Alien-FFI

%changelog
* Sun Jul 26 2026 Vitaly Lipatov <lav@altlinux.ru> 0.27-alt1
- initial build for Sisyphus
