## SPEC file for Perl module IO::Socket::Timeout

%define real_name IO-Socket-Timeout

Name: perl-IO-Socket-Timeout
Version: 0.31
Release: alt1

Summary: Perl IO::Socket with read/write timeout

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/IO-Socket-Timeout/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Fri May 29 2015
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-JSON-PP perl-Module-Load perl-Parse-CPAN-Meta perl-Term-ANSIColor perl-Test-SharedFork perl-devel perl-parent
BuildRequires: perl-Module-Build-Tiny perl-PerlIO-via-Timeout perl-Test-TCP

%description
Perl module IO::Socket::Timeout provides a way to set a timeout
on the socket, but the timeout will be used only for connection,
not for reading / writing operations.

This module provides a way to set a timeout on read / write
operations on an IO::Socket instance, or any IO::Socket::*
modules, like IO::Socket::INET.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/IO/Socket/Timeout*

%changelog
* Tue Aug 25 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.31-alt1
- New version

* Fri May 29 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.29-alt1
- Initial build for ALT Linux Sisyphus
