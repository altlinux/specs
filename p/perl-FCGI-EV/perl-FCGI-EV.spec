## SPEC file for Perl module FCGI::EV

%define real_name FCGI-EV

Name: perl-FCGI-EV
Version: 2.0.0
Release: alt1

Summary:  Perl FastCGI protocol implementation for use in EV-based applications

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/FCGI-EV/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

# This one is missed by find-requires
Requires: perl(EV/ADNS.pm)

BuildRequires(pre): rpm-build-licenses

# Automatically added by buildreq on Sun Mar 20 2016
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-EV perl-Encode perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-JSON-PP perl-Module-Load perl-Parse-CPAN-Meta perl-Term-ANSIColor perl-common-sense perl-devel python3 python3-base
BuildRequires: perl-EV-ADNS perl-IO-Stream perl-Module-Build-Tiny

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
* Sun Mar 20 2016 Nikolay A. Fetisov <naf@altlinux.ru> 2.0.0-alt1
- New version

* Tue Feb 25 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.9-alt2
- Adding missed dependancy on EV::ADNS module

* Fri Feb 21 2014 Nikolay A. Fetisov <naf@altlinux.ru> 1.0.9-alt1
- Initial build for ALT Linux Sisyphus
