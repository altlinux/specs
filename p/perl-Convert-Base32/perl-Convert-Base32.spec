## SPEC file for Perl module Convert::Base32

%define real_name Convert-Base32

%define _unpackaged_files_terminate_build 1

Name: perl-Convert-Base32
Version: 0.06
Release: alt2

Summary: Perl module for encoding and decoding of base32 strings

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/Convert-Base32

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 15 2023
# optimized out: libgpg-error perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-Sub-Uplevel perl-devel perl-parent python-modules python2-base python3-base sh4
BuildRequires: perl-CPAN-Meta perl-Test-Exception

%description
Perl module Convert::Base32 provides functions to convert string
from / to Base32 encoding, specified in RACE internet-draft.
The Base32 encoding is designed to encode non-ASCII characters
 in DNS-compatible host name parts.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Convert/Base32*

%changelog
* Sun Jan 15 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.06-alt2
- Initial build for ALT Linux Sisyphus
