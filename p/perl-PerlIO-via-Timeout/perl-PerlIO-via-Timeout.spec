## SPEC file for Perl module PerlIO::via::Timeout

%define real_name PerlIO-via-Timeout

Name: perl-PerlIO-via-Timeout
Version: 0.32
Release: alt1

Summary: a PerlIO layer that adds read & write timeout to a handle

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/PerlIO-via-Timeout/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Fri May 29 2015
# optimized out: perl-CPAN-Meta perl-CPAN-Meta-Requirements perl-CPAN-Meta-YAML perl-Encode perl-ExtUtils-Config perl-ExtUtils-Helpers perl-ExtUtils-InstallPaths perl-JSON-PP perl-Module-Load perl-Parse-CPAN-Meta perl-Term-ANSIColor perl-Test-SharedFork perl-devel perl-parent
BuildRequires: perl-Module-Build-Tiny perl-Test-TCP

%description
Perl module PerlIO::via::Timeout implements a PerlIO layer, that
adds read / write timeout. This can be useful to avoid blocking
while accessing a handle (file, socket, ...), and fail after
some time.

The timeout is implemented by using <select> on the handle
before reading/writing.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/PerlIO/via/Timeout*

%changelog
* Sun Aug 30 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.32-alt1
- New version

* Fri May 29 2015 Nikolay A. Fetisov <naf@altlinux.ru> 0.30-alt1
- Initial build for ALT Linux Sisyphus
