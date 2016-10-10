Name: perl6-File-Which
Version: 0.1
Release: alt1.d1d9dbe
Summary: File::Which Perl 6 module

Group: Development/Other
License: Artistic 2
URL: https://github.com/azawawi/perl6-file-which

Source: %name-%version.tar

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: rakudo rpm-build-perl6

BuildArch: noarch

AutoReq: noperl
AutoProv: noperl

%description
Cross platform Perl 6 executable path finder (aka which on UNIX)

%prep
%setup

%build

%check
%perl6_test

%install
%perl6_vendor_install

%files
%perl6_vendorlib/dist/*
%perl6_vendorlib/sources/*
%perl6_vendorlib/short/*
%doc LICENSE README.md

%changelog
* Tue Sep 13 2016 Vladimir Lettiev <crux@altlinux.ru> 0.1-alt1.d1d9dbe
- commit d1d9dbe
- initial build

