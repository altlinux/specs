Name: apt-conf-yandex-browser
Version: 1.0
Release: alt1

Summary: Official repository of Yandex Browser
License: Public-Domain
Group: System/Base

Url: https://browser.yandex.ru/

ExclusiveArch: x86_64

Source: %name-%version.tar

Requires: apt-https
Requires: apt-gpgkeys-pki
Requires: libxcbutil-cursor

%description
%{summary}.

%prep
%setup

%install
%__install -Dp -m0644 yandex-browser-sources.list %buildroot%_sysconfdir/apt/sources.list.d/yandex-browser.list
install -Dpm0644 yandex-browser-vendors.list %buildroot%_sysconfdir/apt/vendors.list.d/yandex-browser.list
install -Dpm0644 yandex-browser.asc %buildroot%_datadir/pki/apt-gpg/sources/yandex-browser.asc

%files
%config(noreplace) %_sysconfdir/apt/sources.list.d/yandex-browser.list
%_sysconfdir/apt/vendors.list.d/yandex-browser.list
%_datadir/pki/apt-gpg/sources/yandex-browser.asc

%changelog
* Tue Jun 09 2026 Nazarov Denis <nenderus@altlinux.org> 1.0-alt1
- Initial build for ALT Linux

