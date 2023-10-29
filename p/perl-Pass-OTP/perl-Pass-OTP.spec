## SPEC file for Perl module Pass::OTP

%define real_name Pass-OTP

%define _unpackaged_files_terminate_build 1

Name: perl-Pass-OTP
Version: 1.6
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

# Rename files to prevent file conflict with oathtool package
mv -- %buildroot%_bindir/oathtool      %buildroot%_bindir/oathtool.pl
mv -- %buildroot%_bindir/otptool       %buildroot%_bindir/otptool.pl
mv -- %buildroot%_man1dir/oathtool.1   %buildroot%_man1dir/oathtool.pl.1
mv -- %buildroot%_man1dir/otptool.1    %buildroot%_man1dir/otptool.pl.1
sed -e 's/oathtool /oathtool.pl /g' -i %buildroot%_man1dir/oathtool.pl.1
sed -e 's/otptool /otptool.pl /g'   -i %buildroot%_man1dir/otptool.pl.1

%files
%doc README Changes
%perl_vendor_privlib/Pass/OTP*
%_bindir/oathtool.pl
%_bindir/otptool.pl
%_man1dir/oathtool.pl.*
%_man1dir/otptool.pl.*

%changelog
* Sun Oct 29 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.6-alt2
- Ffix file conflict with oathtool package

* Thu Oct 26 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.6-alt1
- New version

* Sun Jan 15 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.5-alt2
- Initial build for ALT Linux Sisyphus
