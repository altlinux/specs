%define real_name Alien-libcmark_gfm

Name: perl-%real_name
Version: 3.0
Release: alt1

Summary: Find or Build libcmark-gfm

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/%real_name

# Source-url: https://cpan.metacpan.org/authors/id/D/DH/DHARDISON/%real_name-%version.tar.gz
Source: %real_name-%version.tar

# Alien::Build installs the module and share data under the arch vendor path
BuildRequires(pre): rpm-build-perl rpm-build-licenses
BuildRequires: perl-devel perl-Alien-Build perl-Alien-Build-Git libcmark-gfm-devel

%description
Alien::libcmark_gfm provides a Perl distribution for libcmark-gfm, the
CommonMark parsing library with GitHub extensions. In system mode it uses
the libcmark-gfm provided by the operating system.

%prep
%setup -q -n %real_name-%version

%build
# prefer system libcmark-gfm via pkg-config; avoid Alien download (offline hasher)
export ALIEN_INSTALL_TYPE=system
%perl_vendor_build

%install
export ALIEN_INSTALL_TYPE=system
%perl_vendor_install

%files
%doc Changes
%perl_vendor_archlib/Alien*
%perl_vendor_archlib/auto/Alien
%perl_vendor_archlib/auto/share/dist/Alien-libcmark_gfm

%changelog
* Mon Jul 27 2026 Vitaly Lipatov <lav@altlinux.ru> 3.0-alt1
- initial build for Sisyphus
