Name: yandex-browser-preinstall
Version: 0.2
Release: alt1

Summary: Set correct environment for Yandex.Browser
License: GPL
Group: Networking/WWW

Url: https://browser.yandex.ru/
Packager: Nazarov Denis <nenderus@altlinux.org>
BuildArch: noarch

Source0: yandex-browser
Source1: yandex-browser-beta

# libgcrypt.so.11
Requires: libgcrypt11

Provides: libgcrypt.so.11

%description
Set correct environment for Yandex.Browser

%install
%__install -Dp -m0644 %SOURCE0 %buildroot%_sysconfdir/default/yandex-browser
%__install -Dp -m0644 %SOURCE1 %buildroot%_sysconfdir/default/yandex-browser-beta

%files
%_sysconfdir/default/yandex-browser
%_sysconfdir/default/yandex-browser-beta

%changelog
* Sat Jul 02 2016 Nazarov Denis <nenderus@altlinux.org> 0.2-alt1
- Add require on libgcrypt11

* Thu Oct 30 2014 Nazarov Denis <nenderus@altlinux.org> 0.1-alt1
- Initial release for ALT Linux
