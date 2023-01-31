## SPEC file for Perl module Pass::OTP

%define real_name Pass-OTP

%define _unpackaged_files_terminate_build 1

Name: perl-Pass-OTP
Version: 1.5
Release: alt2

Summary: Perl implementation of HOTP / TOTP algorithms

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Pass-OTP

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 15 2023
# optimized out: libgpg-error perl perl-CPAN-Meta-Requirements perl-Digest-SHA perl-Encode perl-JSON-PP perl-Math-BigInt perl-Parse-CPAN-Meta perl-Pod-Escapes perl-Pod-Simple perl-parent perl-podlators python-modules python2-base python3-base sh4
BuildRequires: perl-CPAN-Meta perl-Convert-Base32 perl-Digest-HMAC perl-devel perl-podlators

%description
Perl module Pass::OTP provides implementation of HOTP and TOTP
algorithms according to the RFC 4226 and RFC 6238.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Pass/OTP*
%_bindir/oathtool
%_bindir/otptool
%_man1dir/oathtool.*
%_man1dir/otptool.*

%changelog
* Sun Jan 15 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.5-alt2
- Initial build for ALT Linux Sisyphus
