## SPEC file for Perl module Config::IniHash

%define real_name Config-IniHash

Name: perl-Config-IniHash
Version: 3.01.01
Release: alt1

Summary: Perl extension for reading and writing INI files

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Config-IniHash/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses


# Automatically added by buildreq on Tue Oct 11 2011
# optimized out: perl-Encode perl-Log-Report perl-Pod-Escapes perl-Pod-Simple perl-YAML-Tiny perl-devel perl-podlators
BuildRequires: perl-Hash-Case perl-Hash-WithDefaults perl-Module-Build

%description
Perl module Config::IniHash provides support for reading 
and writing INI files.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Config/IniHash*

%changelog
* Tue Oct 11 2011 Nikolay A. Fetisov <naf@altlinux.ru> 3.01.01-alt1
- Initial build for ALT Linux Sisyphus
