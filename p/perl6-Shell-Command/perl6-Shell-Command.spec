Name: perl6-Shell-Command
Version: 0.1
Release: alt1.8a6381c
Summary: Shell::Command Perl 6 module 

Group: Development/Other
License: MIT
URL: https://github.com/tadzik/Shell-Command

Source: %name-%version.tar

Packager: Vladimir Lettiev <crux@altlinux.ru>

BuildRequires: rakudo perl6-File-Find

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
perl6 -Ilib t/*.t

%install
mkdir -p %buildroot%_datadir/perl6/vendor/lib
cp -r lib/* %buildroot%_datadir/perl6/vendor/lib

%files
%_datadir/perl6/vendor/lib/Shell/Command.pm
%doc README LICENSE

%changelog
* Wed Oct 28 2015 Vladimir Lettiev <crux@altlinux.ru> 0.1-alt1.8a6381c
- commit 8a6381c
- initial build


