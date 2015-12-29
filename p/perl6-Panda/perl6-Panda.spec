Name: perl6-Panda
Version: 2015.12
Release: alt1
Summary: Perl 6 module installer

Group: Development/Other
License: MIT
URL: https://github.com/tadzik/panda

# Cloned from https://github.com/tadzik/panda
Source: %name-%version.tar

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildPreReq: rakudo rpm-build-perl6
BuildRequires: perl6-Shell-Command perl6-JSON-Fast perl6-File-Find

BuildArch: noarch

PreReq: rakudo
Requires: perl6-Shell-Command perl6-JSON-Fast perl6-File-Find
Requires: /usr/bin/prove

AutoReq: noperl
AutoProv: noperl

%description
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
cp bin/panda %buildroot%_bindir
%perl6_vendor_install

%check
%perl6_test

%files
%_bindir/panda
%perl6_vendorlib/dist/*
%perl6_vendorlib/short/*
%perl6_vendorlib/sources/*
%doc LICENSE CONTRIBUTING.md README.md README.alt

%changelog
* Tue Dec 29 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.12-alt1
- 2015.12
- install with rpm-build-perl6

* Mon Nov 30 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.11-alt0.1
- git snapshot e9055fe

* Tue Oct 27 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.10-alt1
- initial build


