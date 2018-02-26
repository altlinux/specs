# Spec file for Perl module File::KeePass

Name: perl-File-KeePass
Version: 0.03
Release: alt1

Summary: Perl interface to KeePass V1 database files

%define real_name File-KeePass

License: %perl_license
Group: Development/Perl
URL: http://search.cpan.org/~rhandom/File-KeePass/

Packager: Nikolay Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): perl-devel rpm-build-licenses


# Automatically added by buildreq on Mon May 09 2011
BuildRequires: perl-Crypt-Rijndael perl-Digest-SHA perl-devel

%description
Perl module File::KeePass provides interface to KeePass V1 database files.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes 
%perl_vendor_privlib/File/KeePass*

%changelog
* Sun May 29 2011 Nikolay A. Fetisov <naf@altlinux.ru> 0.03-alt1
- Initial build for ALT Linux Sisyphus
