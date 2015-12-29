Name: perl6-Shell-Command
Version: 0.1
Release: alt2.1a7eafc
Summary: Shell::Command Perl 6 module 

Group: Development/Other
License: MIT
URL: https://github.com/tadzik/Shell-Command

Source: %name-%version.tar

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: rakudo perl6-File-Find rpm-build-perl6

BuildArch: noarch

PreReq: rakudo
Requires: perl6-File-Find

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
%perl6_vendorlib/sources/*
%perl6_vendorlib/short/*
%doc README LICENSE

%changelog
* Tue Dec 29 2015 Vladimir Lettiev <crux@altlinux.ru> 0.1-alt2.1a7eafc
- commit 1a7eafc
- add rpm-build-perl6 macroses
- fixed install

* Wed Oct 28 2015 Vladimir Lettiev <crux@altlinux.ru> 0.1-alt1.8a6381c
- commit 8a6381c
- initial build


