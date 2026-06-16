Name: goverlay
Version: 1.8.2
Release: alt1

Summary: Graphical UI to help manage Linux overlays
License: GPLv3+
Group: System/Configuration/Hardware

Url: https://github.com/benjamimgois/goverlay
Source: https://github.com/benjamimgois/goverlay/archive/%version/%name-%version.tar.gz
Patch: goverlay-enable-debuginfo-generation.patch

BuildRequires: lazarus rpm-build-fpc fpc libappstream-glib-devel qt6pas-devel

Requires: mangohud vulkan-tools vkBasalt
Requires: qt6pas

%description
Goverlay helps Linux gamers get the most out of their system by offering an easy graphical interface to configure MangoHud, 
vkBasalt, and OptiScaler. Whether you want performance monitoring, visual enhancements, or smarter upscaling, 
Goverlay makes everything accessible in just a few clicks.

%prep
%setup

%build
%make_build

%install
%makeinstall_std prefix=%prefix

%files
%doc LICENSE
%_bindir/%name
#_desktopdir/%name.desktop
%_datadir/metainfo/*%name.metainfo.xml
%{_datadir}/applications/*.desktop
%_iconsdir/hicolor/*/apps/*%name.png
%_man1dir/%name.1*
/usr/libexec/goverlay
%dir %_datadir/%name/assets/icons/
%_datadir/%name/assets/icons/*
%dir %_datadir/%name/data/icons/
%dir %_datadir/%name/data/icons/128x128/
%dir %_datadir/%name/data/icons/256x256/
%dir %_datadir/%name/data/icons/512x512/
%dir %_datadir/%name/data/icons/buttons/
%dir %_datadir/%name/data/icons/system/
%_datadir/%name/data/icons/*/*

%changelog
* Tue Jun 16 2026 Ilya Mashkin <oddity@altlinux.ru> 1.8.2-alt1
- 1.8.2

* Mon May 11 2026 Ilya Mashkin <oddity@altlinux.ru> 1.8.1-alt1
- 1.8.1

* Fri May 08 2026 Ilya Mashkin <oddity@altlinux.ru> 1.8.0-alt1
- 1.8.0

* Thu Mar 05 2026 Ilya Mashkin <oddity@altlinux.ru> 1.7.5-alt1
- 1.7.5

* Sat Feb 14 2026 Ilya Mashkin <oddity@altlinux.ru> 1.7.4-alt1
- 1.7.4

* Wed Jan 28 2026 Ilya Mashkin <oddity@altlinux.ru> 1.7.3-alt1
- 1.7.3

* Sat Jan 17 2026 Ilya Mashkin <oddity@altlinux.ru> 1.7.1-alt1
- 1.7.1

* Tue Jan 06 2026 Ilya Mashkin <oddity@altlinux.ru> 1.6.9-alt1
- 1.6.9

* Fri Dec 26 2025 Ilya Mashkin <oddity@altlinux.ru> 1.6.7-alt1
- 1.6.7

* Wed Dec 17 2025 Ilya Mashkin <oddity@altlinux.ru> 1.6.4-alt1
- 1.6.4
- Cleanup spec

* Sat Dec 13 2025 Ilya Mashkin <oddity@altlinux.ru> 1.6.2-alt1
- 1.6.2

* Wed Nov 19 2025 Ilya Mashkin <oddity@altlinux.ru> 1.6.1-alt1
- 1.6.1

* Tue Oct 14 2025 Ilya Mashkin <oddity@altlinux.ru> 1.5.2-alt1
- 1.5.2

* Mon Aug 18 2025 Ilya Mashkin <oddity@altlinux.ru> 1.4.1-alt1
- 1.4.1

* Mon Aug 04 2025 Ilya Mashkin <oddity@altlinux.ru> 1.4.0-alt1
- 1.4.0

* Mon Mar 03 2025 Ilya Mashkin <oddity@altlinux.ru> 1.3-alt1
- 1.3

* Mon Jan 13 2025 Ilya Mashkin <oddity@altlinux.ru> 1.2-alt1
- 1.2 (Closes: #51122, #51958)

* Sat Apr 06 2024 Ilya Mashkin <oddity@altlinux.ru> 1.1.1-alt1
- 1.1.1

* Tue Dec 19 2023 Ilya Mashkin <oddity@altlinux.ru> 1.0-alt1
- 1.0

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

