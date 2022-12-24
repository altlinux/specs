Name: goverlay
Version: 0.9.1
Release: alt1

Summary: Graphical UI to help manage Linux overlays
License: GPLv3+
Group: System/Configuration/Hardware

Url: https://github.com/benjamimgois/goverlay
Source: https://github.com/benjamimgois/goverlay/archive/%version/%name-%version.tar.gz
Patch: goverlay-enable-debuginfo-generation.patch

#ExclusiveArch: x86_64
ExcludeArch: ppc64le armh
BuildRequires: lazarus rpm-build-fpc fpc libappstream-glib-devel qt5pas-devel

Requires: mangohud vulkan-tools vkBasalt
Requires: qt5pas


#Recommends: git
#Recommends: mesa-demos
#Recommends: vkbasalt
#Recommends: vulkan-tools

%description
GOverlay is an opensource project that aims to create a graphical UI to
help manage Linux overlays. Currently supported:

- MangoHUD
- vkBasalt

%prep
%setup

%build
#set_build_flags
%make_build

%install
%makeinstall_std prefix=%prefix

%files
%doc LICENSE
%_bindir/%name
#_desktopdir/%name.desktop
%_datadir/metainfo/*%name.metainfo.xml
%{_datadir}/applications/*.desktop
%_iconsdir/hicolor/*/apps/%name.png
%_man1dir/%name.1*
/usr/libexec/goverlay

%changelog
* Sat Dec 24 2022 Ilya Mashkin <oddity@altlinux.ru> 0.9.1-alt1
- 0.9.1
- Add Requires: vulkan-tools vkBasalt (Closes: #43372)

* Fri Jul 22 2022 Ilya Mashkin <oddity@altlinux.ru> 0.9-alt1
- 0.9

* Tue Mar 08 2022 Ilya Mashkin <oddity@altlinux.ru> 0.8.1-alt1
- 0.8.1

* Mon Feb 28 2022 Ilya Mashkin <oddity@altlinux.ru> 0.8-alt1
- 0.8

* Fri Dec 17 2021 Ilya Mashkin <oddity@altlinux.ru> 0.7.1-alt1
- 0.7.1

* Wed Dec 01 2021 Ilya Mashkin <oddity@altlinux.ru> 0.7-alt1
- 0.7
- ExclusiveArch: x86_64

* Thu Oct 28 2021 Ilya Mashkin <oddity@altlinux.ru> 0.6.4-alt1
- 0.6.4

* Thu Sep 16 2021 Ilya Mashkin <oddity@altlinux.ru> 0.6.3-alt1
- 0.6.3

* Fri Aug 27 2021 Ilya Mashkin <oddity@altlinux.ru> 0.6.2-alt1
- 0.6.2

* Sat Jul 31 2021 Ilya Mashkin <oddity@altlinux.ru> 0.6.1-alt1
- 0.6.1

* Thu Jun 24 2021 Ilya Mashkin <oddity@altlinux.ru> 0.5.1-alt1
- 0.5.1
- add more BR
- Update license to GPLv3+

* Wed Apr 21 2021 Michael Shigorin <mike@altlinux.org> 0.3.8-alt1
- initial build for ALT Sisyphus (thx Mageia)

* Fri Oct 16 2020 akien <akien> 0.3.8-1.mga8
+ Revision: 1636448
- Version 0.3.8
- Version 0.3.6

* Mon Jul 06 2020 akien <akien> 0.3.5-1.mga8
+ Revision: 1602481
- Version 0.3.5

* Fri Mar 13 2020 akien <akien> 0.2-1.mga8
+ Revision: 1556067
- Version 0.2

* Tue Mar 10 2020 akien <akien> 0.1.3-1.mga8
+ Revision: 1555273
- imported package goverlay

