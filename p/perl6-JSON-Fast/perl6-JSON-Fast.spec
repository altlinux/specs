Name: perl6-JSON-Fast
Version: 0.3
Release: alt0.8ad8c77
Summary: JSON::Fast Perl 6 module 

Group: Development/Other
License: Artistic 2
URL: https://github.com/timo/json_fast

Source: %name-%version.tar

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: rakudo rpm-build-perl6
BuildArch: noarch

AutoReq: noperl
AutoProv: noperl

%description
%summary

%prep
%setup

%build

%check
%perl6_test

%install
%perl6_vendor_install

%files
%perl6_vendorlib/dist/*
%perl6_vendorlib/short/*
%perl6_vendorlib/sources/*
%doc LICENSE README.md

%changelog
* Tue Dec 29 2015 Vladimir Lettiev <crux@altlinux.ru> 0.3-alt0.8ad8c77
- 0.3
- install with rpm-build-perl6

* Wed Oct 28 2015 Vladimir Lettiev <crux@altlinux.ru> 0.2-alt1.e9e648e
- commit e9e648e
- initial build


