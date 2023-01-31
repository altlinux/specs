## SPEC file for Perl module File::KDBX

%define real_name File-KDBX

%define _unpackaged_files_terminate_build 1

Name: perl-File-KDBX
Version: 0.906
Release: alt2

Summary: Perl module to work with KeePassXC (KDBX4) database files

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/File-KDBX

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 15 2023
# optimized out: libgpg-error perl perl-B-Hooks-EndOfScope perl-CPAN-Meta-Requirements perl-Compress-Raw-Zlib perl-Convert-Base32 perl-Crypt-Rijndael perl-Digest-HMAC perl-Digest-SHA perl-Encode perl-IO-Compress perl-JSON-PP perl-JSON-XS perl-Locale-Maketext-Simple perl-Math-BigInt perl-Module-Implementation perl-Module-Load perl-Module-Load-Conditional perl-Module-Metadata perl-Module-Runtime perl-Package-Stash perl-Package-Stash-XS perl-Params-Check perl-Parse-CPAN-Meta perl-Sub-Exporter-Progressive perl-Time-Piece perl-Try-Tiny perl-Types-Serialiser perl-Unicode-Normalize perl-Variable-Magic perl-common-sense perl-devel perl-parent python-modules python2-base python3-base sh4
BuildRequires: perl-CPAN-Meta perl-Crypt-Argon2 perl-CryptX perl-Devel-GlobalDestruction perl-File-KDBX-XS perl-File-KeePass perl-IPC-Cmd perl-Iterator-Simple perl-JSON perl-Module-Loaded perl-POSIX-1003 perl-Pass-OTP perl-Ref-Util perl-Ref-Util-XS perl-Scope-Guard perl-Test-Deep perl-Test-Fatal perl-Test-Warnings perl-Unicode-Collate perl-XML-LibXML perl-boolean perl-namespace-clean

%description
Perl module File::KDBX provides everything you need to work with
KDBX (KeepPass) and KDBX4 (KeePassXC) databases - a hierarchical
object database which is commonly used to store secret information
securely.

This module allow to query entries, create new entries, delete
entries, modify entries and more. The distribution also includes
various parsers and generators for serializing and persisting
databases.


%prep
%setup -q -n %real_name-%version

# Fix typo in requirements:
sed -e 's/Crypt::Stream::Serpent/Crypt::Cipher::Serpent/' -i META.json t/00-report-prereqs.dd
sed -e 's/Crypt::Stream::Twofish/Crypt::Cipher::Twofish/' -i META.json t/00-report-prereqs.dd

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/File/KDBX*
#%%perl_vendor_archlib/File/KDBX*
#%%perl_vendor_autolib/File/KDBX*

%changelog
* Sun Jan 15 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.906-alt2
- Initial build for ALT Linux Sisyphus
