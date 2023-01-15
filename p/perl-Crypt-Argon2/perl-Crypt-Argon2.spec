## SPEC file for Perl module Crypt::Argon2

%define real_name Crypt-Argon2

%define _unpackaged_files_terminate_build 1

Name: perl-Crypt-Argon2
Version: 0.012
Release: alt2

Summary: Perl interface to the Argon2 key derivation functions

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Crypt-Argon2

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 15 2023
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel libgpg-error perl perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-ExtUtils-CBuilder perl-IPC-Cmd perl-JSON-PP perl-Locale-Maketext-Simple perl-Module-Load perl-Module-Load-Conditional perl-Module-Metadata perl-Params-Check perl-Parse-CPAN-Meta perl-Perl-OSType perl-Pod-Escapes perl-Pod-Simple perl-devel perl-parent perl-podlators python-modules python2-base python3-base sh4
BuildRequires: perl-HTML-Parser perl-Module-Build

%description
Perl module Crypt::Argon2 implements the Argon2 key derivation
function, which is suitable to convert any password into
a cryptographic key. This is most often used to for secure
storage of passwords but can also be used to derive a encryption
key from a password. It offers variable time and memory costs
as well as output size.

To find appropriate parameters, the bundled program
argon2-calibrate can be used.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_archlib/Crypt/Argon2*
%perl_vendor_autolib/Crypt/Argon2*

%changelog
* Sun Jan 15 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.012-alt2
- Initial build for ALT Linux Sisyphus
