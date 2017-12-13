Name: dconf-locker
Version: 1.0
Release: alt1

Summary: a simple script to lock and unlock desktop configuration

License: MIT
Group: System/Base
Url: https://github.com/greno4ka/dconf-locker

Packager: Grigory Ustinov <grenka@altlinux.org>

Source: %name-%version.tar

Requires: xmllint

BuildArch: noarch

%prep
%setup

%description
%summary.

%install
install -Dp -m0755 %name %buildroot%_bindir/%name
install -Dp -m0644 %name-functions %buildroot%_bindir/%name-functions

%files
%_bindir/*

%changelog
* Thu Dec 07 2017 Grigory Ustinov <grenka@altlinux.org> 1.0-alt1
- Initial build for Sisyphus.
