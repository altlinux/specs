Name: perl6-Panda
Version: 2015.10
Release: alt1
Summary: Perl 6 module installer

Group: Development/Other
License: MIT
URL: https://github.com/tadzik/panda

# Cloned from https://github.com/tadzik/panda
Source: %name-%version.tar

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildPreReq: rakudo
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
mkdir -p %buildroot%_datadir/perl6/vendor/lib
mkdir -p %buildroot%_bindir
cp bin/panda %buildroot%_bindir
cp -r lib/* %buildroot%_datadir/perl6/vendor/lib

%check
perl6 -Ilib t/*.t

%files
%_bindir/panda
%_datadir/perl6/vendor/lib/Panda*
%doc LICENSE CONTRIBUTING.md README.md

%changelog
* Tue Oct 27 2015 Vladimir Lettiev <crux@altlinux.ru> 2015.10-alt1
- initial build


