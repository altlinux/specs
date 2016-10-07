Name: perl6-Zef
Version: 1
Release: alt1.1624a6c
Summary: Perl 6 module manager

Group: Development/Other
License: MIT
URL: https://github.com/ugexe/zef

# Cloned from https://github.com/ugexe/zef
Source: %name-%version.tar

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildPreReq: rakudo rpm-build-perl6

BuildArch: noarch

PreReq: rakudo
Requires: git-core curl

AutoReq: noperl
AutoProv: noperl

%description
%summary

%prep
%setup
# default install to HOME
sed -i 's/site/home/' resources/config.json

%build

%install
mkdir -p %buildroot%_bindir
perl6 -Ilib bin/zef --install-to=inst#%buildroot%perl6_vendorlib install .
ln -sf \
    $(relative  %buildroot%perl6_vendorlib/bin/zef %buildroot%_bindir/zef) \
    %buildroot%_bindir/zef

%check
%perl6_test

%files
%_bindir/zef
%perl6_vendorlib/bin/*
%perl6_vendorlib/dist/*
%perl6_vendorlib/short/*
%perl6_vendorlib/sources/*
%perl6_vendorlib/resources/*
%doc README.pod

%changelog
* Fri Oct 07 2016 Vladimir Lettiev <crux@altlinux.ru> 1-alt1.1624a6c
- initial build

