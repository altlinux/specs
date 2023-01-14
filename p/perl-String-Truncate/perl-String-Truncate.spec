## SPEC file for Perl module String::Truncate

%define real_name String-Truncate

Name: perl-String-Truncate
Version: 1.100603
Release: alt1

Summary: Perl module for when strings are too long to be displayed in ...

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/String-Truncate/

Packager: Nikolay A. Fetisov <naf@altlinux.org>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sun Jan 22 2017
# optimized out: perl perl-Data-OptList perl-Params-Util perl-Sub-Install python-base python-modules python3-base
BuildRequires: perl-Encode perl-Sub-Exporter perl-devel

%description
Perl module String::Truncate handles the simple but common
problem of long strings and finite terminal width.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/String/Truncate*

%changelog
* Sat Jan 14 2023 Nikolay A. Fetisov <naf@altlinux.org> 1.100603-alt1
- New version

* Sun Jan 22 2017 Nikolay A. Fetisov <naf@altlinux.ru> 1.100602-alt3
- Initial build for ALT Linux Sisyphus
