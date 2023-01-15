## SPEC file for Perl module File::KDBX::XS

%define real_name File-KDBX-XS

%define _unpackaged_files_terminate_build 1

Name: perl-File-KDBX-XS
Version: 0.900
Release: alt2

Summary: Perl module to speed up File::KDBX

License: %perl_license
Group: Development/Perl

URL: https://metacpan.org/release/File-KDBX-XS

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 15 2023
# optimized out: glibc-kernheaders-generic glibc-kernheaders-x86 libcrypt-devel libgpg-error perl perl-CPAN-Meta-Requirements perl-Encode perl-JSON-PP perl-Parse-CPAN-Meta perl-parent python-modules python2-base python3-base sh4
BuildRequires: perl-CPAN-Meta perl-devel

%description
Perl module File::KDBX::XS provides some speed improvement for
File::KDBX. There is no public interface.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
#%%perl_vendor_privlib/File/KDBX/XS*
%perl_vendor_archlib/File/KDBX/XS*
%perl_vendor_autolib/File/KDBX/XS*

%changelog
* Sun Jan 15 2023 Nikolay A. Fetisov <naf@altlinux.org> 0.900-alt2
- Initial build for ALT Linux Sisyphus
