## SPEC file for Perl module MIME::Base64::URLSafe

%define real_name MIME-Base64-URLSafe

Name: perl-MIME-Base64-URLSafe
Version: 0.01
Release: alt1

Summary: Perl extension for encode/decode URLs

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/MIME-Base64-URLSafe/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Fri Jan 27 2012
BuildRequires: perl-devel

%description
Perl module MIME::Base64::URLSafe is an URL-safe base64
encoder / decoder, compatible with python's 
urlsafe_b64encode / urlsafe_b64decode.  The codec uses
'-' and '/' instead of '+' and '/', which have special
 meanings when embedded in URL.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/MIME/Base64/URLSafe*

%changelog
* Fri Jan 27 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.01-alt1
- Initial build for ALT Linux Sisyphus
