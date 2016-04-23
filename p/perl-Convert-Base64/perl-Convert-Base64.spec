## SPEC file for Perl module Convert::Base64

%define real_name Convert-Base64

Name: perl-Convert-Base64
Version: 0.001
Release: alt1

Summary: encoding and decoding of Base64 strings

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Convert-Base64/
#URL: git://github.com/robn/Convert-Base64

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

BuildRequires(pre): perl-devel rpm-build-licenses

# Automatically added by buildreq on Sat Apr 23 2016
# optimized out: python-base python-modules python3
BuildRequires: perl-Encode perl-devel

%description
Perl module Convert::Base64 provides functions to convert strings
to/from the Base64 encoding as described in RFC 4648.

Its implemented as a light wrapper over MIME::Base64.

%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Convert/Base64*

%changelog
* Sat Apr 23 2016 Nikolay A. Fetisov <naf@altlinux.ru> 0.001-alt1
- Initial build for ALT Linux Sisyphus
