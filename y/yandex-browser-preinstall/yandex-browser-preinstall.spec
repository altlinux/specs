Name: yandex-browser-preinstall
Version: 0.3
Release: alt1

Summary: Set correct environment for Yandex.Browser
License: GPL
Group: Networking/WWW

Url: https://browser.yandex.ru/
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

Source0: yandex-browser
Source1: yandex-browser-beta

BuildRequires: chromium

%description
Set correct environment for Yandex.Browser

%install
%__install -Dp -m0644 %SOURCE0 %buildroot%_sysconfdir/default/yandex-browser
%__install -Dp -m0644 %SOURCE1 %buildroot%_sysconfdir/default/yandex-browser-beta

# Fix playable video with H.264 codec
%__mkdir_p %buildroot%_libexecdir/chromium-browser
%__ln_s %_libdir/chromium/libffmpeg.so %buildroot%_libexecdir/chromium-browser/libffmpeg.so

%files
%_sysconfdir/default/yandex-browser
%_sysconfdir/default/yandex-browser-beta
%_libexecdir/chromium-browser/libffmpeg.so

%changelog
* Sat Oct 28 2017 Nazarov Denis <nenderus@altlinux.org> 0.3-alt1
- Fix playable video with H.264 codec
- Remove require on libgcrypt11 (now use libgcrypt20)

* Sat Jul 02 2016 Nazarov Denis <nenderus@altlinux.org> 0.2-alt1
- Add require on libgcrypt11

* Thu Oct 30 2014 Nazarov Denis <nenderus@altlinux.org> 0.1-alt1
- Initial release for ALT Linux
