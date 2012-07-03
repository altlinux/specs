## SPEC file for Perl module File::ShareDir::Install

%define real_name File-ShareDir-Install

Name: perl-File-ShareDir-Install
Version: 0.04
Release: alt1

Summary: Perl extension for installing shared files

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/File-ShareDir-Install/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Fri Jan 27 2012
# optimized out: perl-Devel-Symdump perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-devel
BuildRequires: perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module File::ShareDir::Install allows you to install
read-only data files from a distribution. It is a companion
module to File::ShareDir, which allows you to locate these
files after installation.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/File/ShareDir/Install*

%changelog
* Fri Jan 27 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.04-alt1
- Initial build for ALT Linux Sisyphus
