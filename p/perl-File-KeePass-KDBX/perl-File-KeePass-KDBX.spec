## SPEC file for Perl module File::KeePass::KDBX

%define real_name File-KeePass-KDBX

%define _unpackaged_files_terminate_build 1

Name: perl-File-KeePass-KDBX
Version: 0.902
Release: alt1

Summary: Perl module to read and write KDBX files

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/File-KeePass-KDBX

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 15 2023
# optimized out: libgpg-error perl perl-B-Hooks-EndOfScope perl-CPAN-Meta-Requirements perl-Compress-Raw-Zlib perl-Crypt-Rijndael perl-CryptX perl-Devel-GlobalDestruction perl-Digest-SHA perl-Encode perl-IO-Compress perl-Iterator-Simple perl-JSON-PP perl-JSON-XS perl-Module-Implementation perl-Module-Load perl-Module-Loaded perl-Module-Runtime perl-Package-Stash perl-Package-Stash-XS perl-Parse-CPAN-Meta perl-Ref-Util perl-Scope-Guard perl-Sub-Exporter-Progressive perl-Time-Piece perl-Try-Tiny perl-Types-Serialiser perl-Variable-Magic perl-XML-LibXML perl-boolean perl-common-sense perl-devel perl-namespace-clean perl-parent python-modules python2-base python3-base sh4
BuildRequires: perl-CPAN-Meta perl-File-KDBX perl-File-KDBX-XS perl-File-KeePass perl-JSON perl-Ref-Util-XS perl-Test-Deep

%description
Perl module File::KeePass::KDBX is a File::KeePass compatibility
shim for File::KDBX. It presents the same interface as File::KeePass
but uses File::KDBX for database storage, file parsing, etc.
It is meant to be a drop-in replacement for File::KeePass.

%prep
%setup -q -n %real_name-%version

%build
# Some mess with timestamps when testing inside BTE
%ifdef __BTE
    rm -f -- t/keepass-base.t
    rm -f -- t/keepass-kdbx.t
%endif

%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/File/KeePass/KDBX*

%changelog
* Sun Jan 15 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.902-alt1
- Initial build for ALT Linux Sisyphus
