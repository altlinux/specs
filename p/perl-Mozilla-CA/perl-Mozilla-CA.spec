## SPEC file for Perl module Mozilla::CA

Name: perl-Mozilla-CA
Version: 20120118
Release: alt1

Summary: Perl module provides CA cert bundle

License: %mpl
Group: Development/Perl
URL: http://search.cpan.org/dist/Mozilla-CA/

Packager: Nikolay A. Fetisov <naf@altlinux.ru>
BuildArch: noarch

%define real_name Mozilla-CA
Source: %real_name-%version.tar
Patch0: %real_name-%version-%release.patch

AutoReqProv: perl, yes
BuildRequires(pre): rpm-build-licenses
Requires: ca-certificates

# Automatically added by buildreq on Sat Jan 28 2012
BuildRequires: ca-certificates perl-devel

%description
Perl module Mozilla::CA provide a single function SSL_ca_file()
that returns the absolute path to the Mozilla's CA cert bundle
PEM file.

Note: this package use CA bundle from system-wide package
ca-certificates .


%prep
%setup  -n %real_name-%version
%patch0 -p1

%build
%perl_vendor_build

%install
%perl_vendor_install

%files
%doc README Changes
%perl_vendor_privlib/Mozilla/CA.pm

%exclude %perl_vendor_privlib/Mozilla/CA/*
%exclude %perl_vendor_privlib/Mozilla/mk-ca-bundle.pl

%changelog
* Sat Jan 28 2012 Nikolay A. Fetisov <naf@altlinux.ru> 20120118-alt1
- Initial build for ALT Linux Sisyphus

