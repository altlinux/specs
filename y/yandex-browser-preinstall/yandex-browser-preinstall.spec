Name: yandex-browser-preinstall
Version: 1.0
Release: alt1

Summary: Set correct environment for Yandex.Browser
License: GPLv3
Group: Networking/WWW

Url: http://git.altlinux.org/people/nenderus/packages/yandex-browser-preinstall.git
Packager: Nazarov Denis <nenderus@altlinux.org>

ExclusiveArch: x86_64

Requires: yandex-browser-stable

%description
Set correct environment for Yandex.Browser

%files

%changelog
* Fri Aug 19 2022 Nazarov Denis <nenderus@altlinux.org> 1.0-alt1
- Only requires on yandex-browser-stable and nothing more

* Mon Apr 05 2021 Nazarov Denis <nenderus@altlinux.org> 0.4-alt4
- Add require on jq (ALT #39880)

* Tue Jan 15 2019 Nazarov Denis <nenderus@altlinux.org> 0.4-alt3
- Drop macro ubt (ALT #35904)

* Thu Mar 15 2018 Nazarov Denis <nenderus@altlinux.org> 0.4-alt2
- No arch

* Thu Mar 15 2018 Nazarov Denis <nenderus@altlinux.org> 0.4-alt1
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
