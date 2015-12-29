Name: perl6-File-Find
Version: 0.1
Release: alt2.d3e2be7
Summary: File::Find Perl 6 module

Group: Development/Other
License: Artistic 2
URL: https://github.com/tadzik/File-Find

Source: %name-%version.tar

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: rakudo rpm-build-perl6

BuildArch: noarch

AutoReq: noperl
AutoProv: noperl

%description
File::Find - Get a lazy list of a directory tree

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
* Tue Dec 29 2015 Vladimir Lettiev <crux@altlinux.ru> 0.1-alt2.d3e2be7
- commit d3e2be7
- install with rpm-build-perl6

* Wed Oct 28 2015 Vladimir Lettiev <crux@altlinux.ru> 0.1-alt1.cfc6865
- commit cfc6865
- initial build


