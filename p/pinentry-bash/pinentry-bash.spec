Summary: Simple PIN or passphrase entry dialog
Name: pinentry-bash
Version: 1.0
Release: alt1
Group: File tools
License: GPL-2
URL: https://github.com/legionus/pinentry-bash
BuildArch: noarch

Source0: %name-%version.tar

%description
This is simple PIN or passphrase entry dialog written in bash.

%prep
%setup

%install
mkdir -p -- %buildroot%_bindir
cp -- pinentry-bash %buildroot%_bindir/

%files
%_bindir/pinentry-bash

%changelog
* Tue Aug 03 2021 Alexey Gladkov <legion@altlinux.ru> 1.0-alt1
- First build.
