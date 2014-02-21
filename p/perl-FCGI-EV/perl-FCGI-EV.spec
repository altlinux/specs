## SPEC file for Perl module FCGI::EV

%define real_name FCGI-EV

Name: perl-FCGI-EV
Version: 1.0.9
Release: alt1

Summary:  Perl FastCGI protocol implementation for use in EV-based applications

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/FCGI-EV/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Fri Feb 21 2014
# optimized out: perl-Devel-Symdump perl-EV perl-Pod-Coverage perl-Pod-Escapes perl-Pod-Parser perl-Pod-Simple perl-common-sense perl-devel
BuildRequires: perl-EV-ADNS perl-IO-Stream perl-Test-Pod perl-Test-Pod-Coverage

%description
Perl module FCGI::EV implements FastCGI protocol for use
in EV-based applications.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/FCGI/EV*

%changelog
* Fri Feb 21 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.9-alt1
- Initial build for ALT Linux Sisyphus
