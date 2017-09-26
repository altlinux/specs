Name: perl6-Zef
Version: 0.1.29
Release: alt1
Epoch: 1
Summary: Perl 6 module manager

Group: Development/Other
License: MIT
URL: https://github.com/ugexe/zef

# Cloned from https://github.com/ugexe/zef
Source: %name-%version.tar

Packager: Vladimir Lettiev <crux@altlinux.org>

BuildPreReq: rakudo rpm-build-perl6

PreReq: rakudo
Requires: git-core curl

AutoReq: noperl
AutoProv: noperl

%def_enable debug

%description
%summary

%prep
%setup

%build

%install
mkdir -p %buildroot%_bindir
%perl6_vendor_install

ln -rsf %buildroot%perl6_vendorlib/bin/zef %buildroot%_bindir/zef

%check
%perl6_test

%files
%_bindir/zef
%exclude %perl6_vendorlib/bin/zef-j
%perl6_vendorlib/bin/*
%perl6_vendorlib/dist/*
%perl6_vendorlib/short/*
%perl6_vendorlib/sources/*
%perl6_vendorlib/resources/*
%perl6_vendorlib/precomp/*
%doc README.pod

%changelog
* Tue Sep 26 2017 Vladimir Lettiev <crux@altlinux.org> 1:0.1.29-alt1
- 0.1.29

* Fri Oct 07 2016 Vladimir Lettiev <crux@altlinux.ru> 1-alt1.1624a6c
- initial build

