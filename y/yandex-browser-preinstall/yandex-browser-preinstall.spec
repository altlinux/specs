Name: yandex-browser-preinstall
Version: 0.4
Release: alt2%ubt

Summary: Set correct environment for Yandex.Browser
License: GPL
Group: Networking/WWW

Url: https://browser.yandex.ru/
Packager: Nazarov Denis <nenderus@altlinux.org>
BuildArch: noarch

Source0: yandex-browser
Source1: yandex-browser-beta

BuildPreReq: rpm-build-ubt

%description
Set correct environment for Yandex.Browser

%install
%__install -Dp -m0644 %SOURCE0 %buildroot%_sysconfdir/default/yandex-browser
%__install -Dp -m0644 %SOURCE1 %buildroot%_sysconfdir/default/yandex-browser-beta

%files
%_sysconfdir/default/yandex-browser
%_sysconfdir/default/yandex-browser-beta

%changelog
* Thu Mar 15 2018 Nazarov Denis <nenderus@altlinux.org> 0.4-alt2%ubt
- No arch

* Thu Mar 15 2018 Nazarov Denis <nenderus@altlinux.org> 0.4-alt1%ubt
- Temporary remove fix playable video with H.264 codec

* Sat Oct 28 2017 Nazarov Denis <nenderus@altlinux.org> 0.3-alt2
- Fix post-install unowned files

* Sat Oct 28 2017 Nazarov Denis <nenderus@altlinux.org> 0.3-alt1
- Fix playable video with H.264 codec
- Remove require on libgcrypt11 (now use libgcrypt20)

* Sat Jul 02 2016 Nazarov Denis <nenderus@altlinux.org> 0.2-alt1
- Add require on libgcrypt11

* Thu Oct 30 2014 Nazarov Denis <nenderus@altlinux.org> 0.1-alt1
- Initial release for ALT Linux
