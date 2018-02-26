## SPEC file for Perl module Mixin::Linewise

%define real_name Mixin-Linewise

Name: perl-Mixin-Linewise
Version: 0.003
Release: alt1

Summary: Perl module to work with handle-like string objects

License: %perl_license
Group: Development/Perl

URL: http://search.cpan.org/dist/Mixin-Linewise/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>

Source: %real_name-%version.tar

BuildArch: noarch

AutoReqProv: perl, yes
BuildPreReq: rpm-build-licenses

# Automatically added by buildreq on Sat Jan 28 2012
# optimized out: perl-Data-OptList perl-Params-Util perl-Sub-Install
BuildRequires: perl-IO-String perl-Sub-Exporter perl-devel

%description
Perl module Mixin::Linewise simplifies the way to deal with opening
files for IO, converting strings to handle-like objects, and all
that. With Mixin::Linewise::Readers and Mixin::Linewise::Writers,
you can just write a method to handle handles, and methods for
handling strings and filenames are added for you.


%prep
%setup -q -n %real_name-%version

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Mixin/Linewise*

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 0.003-alt1
- Initial build for ALT Linux Sisyphus
